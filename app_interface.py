import streamlit as st
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant

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
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Set up Qdrant as a vector store
collection_name = "ai_info_collection"
vector_store = Qdrant(
    client=qdrant_client,
    collection_name=collection_name,
    embeddings=embeddings,
)

# Set up retrieval QA chain
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

# Streamlit interface
st.title("AI Information Assistant")

query = st.text_input("Ask a question about AI ethics, regulations, or policies:")

if query:
    response = qa_chain.run(query)
    st.write(response)
