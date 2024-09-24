import torch
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from huggingface_hub import hf_hub_download, list_repo_files
import os
from dotenv import load_dotenv
from safetensors import safe_open

def setup_rag_pipeline(training_documents, model_path, base_model_name, retriever_k, llm_model, llm_temperature):
    # Load environment variables
    load_dotenv()
    hf_token = os.getenv('HF_TOKEN')

    # Load the fine-tuned model directly
    fine_tuned_model = SentenceTransformer(model_path, use_auth_token=hf_token)
    
    # Create embeddings using the fine-tuned model
    fine_tuned_embeddings = HuggingFaceEmbeddings(model_name=model_path, model_kwargs={'device': 'cpu'})

    vectorstore = FAISS.from_documents(training_documents, fine_tuned_embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": retriever_k})

    RAG_PROMPT = """
    You are an AI assistant specializing in the EU AI Act. Given the context and question below, provide a concise and accurate answer. If the information is not in the context, state that you don't have enough information to answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    rag_prompt_template = ChatPromptTemplate.from_template(RAG_PROMPT)

    rag_llm = ChatOpenAI(model=llm_model, temperature=llm_temperature)

    rag_chain = (
        {"context": itemgetter("question") | retriever, "question": itemgetter("question")}
        | RunnablePassthrough.assign(context=itemgetter("context"))
        | {"response": rag_prompt_template | rag_llm | StrOutputParser(), "context": itemgetter("context")}
    )

    return rag_chain, retriever
