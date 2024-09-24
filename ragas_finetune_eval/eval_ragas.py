from ragas import evaluate
from datasets import Dataset

def run_ragas_evaluation(test_data, metrics):
    test_dataset = Dataset.from_list(test_data)
    result = evaluate(test_dataset, metrics=metrics)
    return result

def prepare_ragas_data(questions, retriever, rag_chain):
    test_data = [
        {
            "question": q,
            "contexts": [c.page_content for c in retriever.get_relevant_documents(q)],
            "answer": rag_chain.invoke({"question": q})["response"]
        }
        for q in questions
    ]
    return test_data
