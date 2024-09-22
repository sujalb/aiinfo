import json
import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Get the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

# Load the local JSON file
with open("testset_with_answers.json", "r") as f:
    data = json.load(f)

# Convert the JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the pandas DataFrame to a Hugging Face Dataset
ai_ans = Dataset.from_pandas(df)

# Create a ChatOpenAI instance with the API key
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Now you can proceed with the evaluation
result = evaluate(
    ai_ans,
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
    ],
    llm=llm  # Pass the LLM instance here
)

print(result)