import os
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import random
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz  # PyMuPDF
from dotenv import load_dotenv
from huggingface_hub import login, HfApi
import traceback

# Add this near the top of your file, after the imports


load_dotenv()
login(token=os.getenv("HF_TOKEN"), add_to_git_credential=True)

# Step 1: Extract Text from PDFs
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text    

def chunk_text(text, themes):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    thematic_chunks = {theme: [] for theme in themes}
    thematic_chunks["Unclassified"] = []  # Add an "Unclassified" category
    
    for chunk in chunks:
        theme_found = False
        for theme in themes:
            if theme.lower() in chunk.lower():
                thematic_chunks[theme].append(chunk)
                theme_found = True
                break
        if not theme_found:
            thematic_chunks["Unclassified"].append(chunk)
    
    print("Chunks per theme:")
    for theme, theme_chunks in thematic_chunks.items():
        print(f"  {theme}: {len(theme_chunks)}")
    
    return thematic_chunks
    # ... (same as in app.py)

# Function to generate synthetic fine-tuning data
def generate_synthetic_data(thematic_chunks, n_samples=1000):
    examples = []
    print(f"Total themes: {len(thematic_chunks)}")
    for theme, chunks in thematic_chunks.items():
        print(f"Theme: {theme}, Number of chunks: {len(chunks)}")
        if not chunks:
            print(f"Warning: No chunks for theme '{theme}'. Skipping this theme.")
            continue
        samples_per_theme = max(1, n_samples // len(thematic_chunks))
        for _ in range(samples_per_theme):
            chunk = random.choice(chunks)
            question = f"What does this text say about {theme.lower()}?"
            examples.append(InputExample(texts=[question, chunk]))
    print(f"Total examples generated: {len(examples)}")
    return examples

# Function to fine-tune the model
def fine_tune_model(model, train_examples, output_path):
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)
    train_loss = losses.MultipleNegativesRankingLoss(model)
    
    model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3, warmup_steps=100, output_path=output_path)
    return model

def main():
    resources_folder = "resources"
    themes = [
        "Safe and Effective Systems",
        "Algorithmic Discrimination Protections",
        "Data Privacy",
        "Notice and Explanation",
        "Human Alternatives",
        "Risk Management",
        "Governance",
        "Trustworthiness",
        "Unclassified"
    ]
    
    all_thematic_chunks = {}
    
    for filename in os.listdir(resources_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(resources_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            thematic_chunks = chunk_text(text, themes)
            all_thematic_chunks.update(thematic_chunks)
            print(f"Processed {filename}")

    # Fine-tune the model
    base_model = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(base_model)
    train_examples = generate_synthetic_data(all_thematic_chunks)
    fine_tuned_model_path = "fine_tuned_embedding_model"
    fine_tune_model(model, train_examples, fine_tuned_model_path)
    
    print("Fine-tuning completed. Model saved locally.")

def upload_model_to_hub():
    try:
        # Load the fine-tuned model
        fine_tuned_model_path = "fine_tuned_embedding_model"
        model = SentenceTransformer(fine_tuned_model_path)

        # Upload the fine-tuned model to Hugging Face Hub
        repo_id = "svb01/fine-tuned-embedding-model"
        
        print(f"Uploading model to existing repository: {repo_id}")
        
        # Use HfApi to upload files directly
        api = HfApi()
        
        # Upload each file in the model directory
        for root, _, files in os.walk(fine_tuned_model_path):
            for file in files:
                file_path = os.path.join(root, file)
                api.upload_file(
                    path_or_fileobj=file_path,
                    path_in_repo=file,
                    repo_id=repo_id,
                    commit_message=f"Upload {file}"
                )
        
        print("Fine-tuned model uploaded to Hugging Face Hub.")
    except Exception as e:
        print(f"Error uploading model to Hugging Face Hub: {str(e)}")
        print("Detailed error information:")
        print(traceback.format_exc())

if __name__ == "__main__":
    # Uncomment the function you want to run
    # main()  # Run this for fine-tuning
    upload_model_to_hub()  # Run this to upload the model
