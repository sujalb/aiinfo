import os
import json
import asyncio
from dotenv import load_dotenv
import pandas as pd
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
from qa_system import generate_answer  # Import the QA system

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def generate_testset(generator, documents, test_size, distributions):
    return generator.generate_with_langchain_docs(
        documents, 
        test_size=test_size, 
        distributions=distributions
    )

async def main():
    # Load environment variables from .env file
    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")      

    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found in environment variables.")

    # Initialize OpenAI API key
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    openai.api_key = OPENAI_API_KEY  # Explicitly set the API key

    # Check if testset.json exists
    if os.path.exists("testset.json"):
        print("Loading existing testset from testset.json")
        with open("testset.json", "r") as f:
            testset_dict = json.load(f)
        df = pd.DataFrame(testset_dict)
    else:
        print("Generating new testset")
        # Load PDF documents
        documents = []
        pdf_dir = "resources"
        for filename in os.listdir(pdf_dir):
            if filename.lower().endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(pdf_dir, filename))
                docs = loader.load()
                for doc in docs:
                    doc.metadata['filename'] = filename
            documents.extend(docs)
        
        for document in documents:
            document.metadata['filename'] = document.metadata['source']

        # Initialize OpenAI models (using gpt-3.5-turbo for both to reduce costs)
        generator_llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
        critic_llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
        embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

        # Initialize the Testset Generator
        generator = TestsetGenerator.from_langchain(
            generator_llm,
            critic_llm,
            embeddings
        )

        try:
            # Generate testset with retry logic
            testset = generate_testset(
                generator,
                documents, 
                test_size=3,
                distributions={simple: 0.6, reasoning: 0.2, multi_context: 0.2}
            )
            
            # Convert testset to pandas DataFrame
            df = testset.to_pandas()
            
            # Save testset to JSON file
            testset_dict = df.to_dict(orient='records')
            with open("testset.json", "w") as f:
                json.dump(testset_dict, f, indent=2)
            print(f"New testset saved to testset.json")

        except Exception as e:
            print(f"An unexpected error occurred while generating testset: {e}")
            return

    try:
        # Generate new answers for each question using the existing QA system
        print("Generating new answers for all questions")
        df['answer'] = df['question'].apply(generate_answer)
        
        # Update JSON file with new answers
        testset_dict = df.to_dict(orient='records')
        with open("testset_with_answers.json", "w") as f:
            json.dump(testset_dict, f, indent=2)
        print(f"Testset with new answers saved to testset_with_answers.json")

        # Save testset with new answers to CSV file
        df.to_csv("testset_with_answers.csv", index=False)
        print(f"Testset with new answers saved to testset_with_answers.csv")

    except openai.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API after multiple attempts: {e}")
    except RuntimeError as e:
        print(f"Runtime error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
     asyncio.run(main())