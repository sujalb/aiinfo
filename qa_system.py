import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import Qdrant

# Load environment variables
load_dotenv()

# Initialize Qdrant client
qdrant_api_key = os.getenv("QDRANT_API_KEY")
qdrant_client = QdrantClient(
    url="https://9266da83-dbfe-48d6-b2d8-cdf101299284.europe-west3-0.gcp.cloud.qdrant.io",
    api_key=qdrant_api_key
)

# Initialize OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_api_key)
llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# Initialize vector store
collection_name = "ai_info_collection"
vector_store = Qdrant(
    client=qdrant_client,
    collection_name=collection_name,
    embeddings=embeddings,
)

def generate_answer(query):
    docs = vector_store.similarity_search(query, k=3)
    context = "\n".join(doc.page_content for doc in docs if doc.page_content)
    prompt = f"Based on the following context, answer the question: {query}\n\nContext: {context}"
    response = llm.invoke(prompt)
    return response.content