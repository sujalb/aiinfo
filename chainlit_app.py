import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import Qdrant as QdrantVectorStore
import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_qdrant import Qdrant




# Load environment variables
load_dotenv()

# Initialize Qdrant client
openai_api_key = os.getenv("OPENAI_API_KEY")
qdrant_api_key = os.getenv("QDRANT_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")

qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key
)

# Initialize OpenAI

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=openai_api_key)
llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# Initialize vector store
collection_name = "ai_info_collection"
vector_store = Qdrant(
    client=qdrant_client,
    collection_name=collection_name,
    embeddings=embeddings,
)

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome! Ask me anything about AI ethics, regulations, or policies.").send()

@cl.on_message
async def main(message: cl.Message):
    query = message.content
    print(f"Received query: {query}")  # Basic console logging

    try:
        docs = vector_store.similarity_search(query, k=3)
        print(f"Retrieved {len(docs)} documents")  # Basic console logging

        context = "\n".join(doc.page_content for doc in docs if doc.page_content)
        prompt = f"Based on the following context, answer the question: {query}\n\nContext: {context}"
        
        response = await llm.ainvoke(prompt)
        print(f"Generated response: {response}")  # Basic console logging

        await cl.Message(content=response.content).send()

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(f"Error: {error_message}")  # Basic console logging
        await cl.Message(content=error_message).send()
