import os
from pathlib import Path

# Path to .env file
ENV_PATH = Path(__file__).parent.parent / '.env'

# Configuration settings for evaluation

# Model and data paths
FINE_TUNED_MODEL_PATH = "svb01/fine-tuned-embedding-model"
TRAINING_DATA_PATH = "../resources/NIST.AI.600-1.pdf"  # Adjust this path if needed

# RAG settings
RETRIEVER_K = 6
LLM_MODEL = "gpt-3.5-turbo"
LLM_TEMPERATURE = 0

# Evaluation settings
SAMPLE_QUESTIONS = [
    "What are the main objectives of the EU AI Act?",
    "How does the Act define high-risk AI systems?",
    "What are the transparency requirements for AI systems?",
    "How does the Act address AI in the workplace?"
]

# RAGAS metrics
RAGAS_METRICS = ["context_precision", "faithfulness", "answer_relevancy"]

# Chunk size for text splitting
CHUNK_SIZE = 750
CHUNK_OVERLAP = 20

BASE_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
