from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from eval_config import CHUNK_SIZE, CHUNK_OVERLAP

def load_training_documents(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    
    return text_splitter.split_documents(data)

def load_sample_questions(questions):
    return questions
