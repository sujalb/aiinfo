def test_rag_pipeline(rag_chain, questions):
    results = []
    for question in questions:
        response = rag_chain.invoke({"question": question})
        results.append({
            "question": question,
            "answer": response['response']
        })
        print(f"Question: {question}")
        print(f"Answer: {response['response']}\n")
    return results
