# Required Libraries
import fitz  # PyMuPDF
import os
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from qdrant_client import QdrantClient  # Import Qdrant client
import uuid  # Add this import at the top of your file
import json

# Load environment variables from .env file
load_dotenv()

# Initialize Qdrant client
qdrant_api_key = os.getenv("QDRANT_API_KEY")  # Get the Qdrant API key from environment variables
qdrant_client = QdrantClient(
    url="https://9266da83-dbfe-48d6-b2d8-cdf101299284.europe-west3-0.gcp.cloud.qdrant.io",
    api_key=qdrant_api_key,
    timeout=300  # 5 minutes timeout
)

# New function to load processed documents
def load_processed_docs():
    try:
        with open('processed_docs.json', 'r') as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

# New function to save processed documents
def save_processed_docs(processed_docs):
    with open('processed_docs.json', 'w') as f:
        json.dump(list(processed_docs), f)

# Modified function to create the Qdrant collection if it doesn't exist
def create_qdrant_collection(collection_name, vector_size):
    try:
        # Check if the collection already exists
        collection_info = qdrant_client.get_collection(collection_name)
        print(f"Collection '{collection_name}' already exists.")
    except Exception as e:
        # If the collection doesn't exist, create it
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config={
                "size": vector_size,
                "distance": "Cosine"
            }
        )
        print(f"Collection '{collection_name}' created successfully.")

# Modified function to store embeddings in Qdrant
def store_embeddings_in_qdrant(embedded_chunks, collection_name):
    points = []
    for theme, embeddings in embedded_chunks.items():
        for embedding in embeddings:
            points.append({
                "id": str(uuid.uuid4()),  # Generate a UUID for each point
                "vector": embedding,
                "payload": {"theme": theme}
            })
    
    # Batch upload points
    batch_size = 100
    for i in range(0, len(points), batch_size):
        batch = points[i:i+batch_size]
        try:
            qdrant_client.upsert(
                collection_name=collection_name,
                points=batch
            )
            print(f"Uploaded batch {i//batch_size + 1} to collection '{collection_name}'.")
        except Exception as e:
            print(f"Error uploading batch {i//batch_size + 1}: {e}")
    
    print(f"Finished uploading {len(points)} points to collection '{collection_name}'.")        

# Step 1: Extract Text from PDFs
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Step 2: Define Themes
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

# Step 3: Chunk the Text
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
    return thematic_chunks

# Step 4: Embed the Chunks
def embed_chunks(thematic_chunks):
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variables
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=openai_api_key)
    embedded_chunks = {theme: embeddings.embed_documents(chunks) for theme, chunks in thematic_chunks.items()}
    return embedded_chunks

# Modified main execution block
def main():
    resources_folder = "resources"
    processed_docs = load_processed_docs()
    new_docs_processed = False

    collection_name = "ai_info_collection"
    
    for filename in os.listdir(resources_folder):
        if filename.endswith(".pdf") and filename not in processed_docs:
            pdf_path = os.path.join(resources_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            thematic_chunks = chunk_text(text, themes)
            embedded_chunks = embed_chunks(thematic_chunks)

            # Ensure the collection exists
            if not new_docs_processed:
                vector_size = len(next(iter(embedded_chunks.values()))[0])
                create_qdrant_collection(collection_name, vector_size)

            # Store embeddings for this document
            store_embeddings_in_qdrant(embedded_chunks, collection_name)
            
            processed_docs.add(filename)
            new_docs_processed = True
            print(f"Processed and added embeddings for {filename}")

    if new_docs_processed:
        save_processed_docs(processed_docs)
        print("New documents processed and added to the collection.")
    else:
        print("No new documents to process.")

if __name__ == "__main__":
    main()