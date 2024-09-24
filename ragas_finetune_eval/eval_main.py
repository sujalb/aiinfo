from eval_config import *
from eval_env_setup import load_env_variables
from eval_data_loader import load_training_documents, load_sample_questions
from eval_rag_setup import setup_rag_pipeline
from eval_rag_tester import test_rag_pipeline
from eval_ragas import run_ragas_evaluation, prepare_ragas_data

def main():
    # Load environment variables
    load_env_variables()

    # Load data
    training_documents = load_training_documents(TRAINING_DATA_PATH)
    sample_questions = load_sample_questions(SAMPLE_QUESTIONS)

    # Setup RAG pipeline
    rag_chain, retriever = setup_rag_pipeline(
        training_documents, 
        FINE_TUNED_MODEL_PATH,
        BASE_MODEL_NAME,
        RETRIEVER_K, 
        LLM_MODEL, 
        LLM_TEMPERATURE
    )

    # Test RAG pipeline
    test_results = test_rag_pipeline(rag_chain, sample_questions)

    # Prepare and run RAGAS evaluation
    ragas_data = prepare_ragas_data(sample_questions, retriever, rag_chain)
    ragas_results = run_ragas_evaluation(ragas_data, RAGAS_METRICS)

    print("RAGAS Evaluation Results:")
    print(ragas_results)

if __name__ == "__main__":
    main()
