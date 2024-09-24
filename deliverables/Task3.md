## Task 3: Creating a Golden Test Data Set

**You are an AI Evaluation & Performance Engineer.**  The AI Systems Engineer who built the initial RAG system has asked for your help and expertise in creating a "Golden Data Set."



Task 3: Generate a synthetic test data set and baseline an initial evaluation

Using Ragas  [See File](../qa_generate_ans.py) I have generated [Test Set with Answers](../testset_with_answers.json)



✅ Deliverables:

1. Assess your pipeline using the RAGAS framework including key metrics faithfulness, answer relevancy, context precision, and context recall.  Provide a table of your output results.

Output : 

```
Evaluating: 100%|███████████████████████████████████████████████████████████████████████████████| 16/16 [00:13<00:00,  1.20it/s]
{'context_precision': 1.0000, 'faithfulness': 0.4940, 'answer_relevancy': 0.9916, 'context_recall': 0.8750}
```



Based on the RAGAS evaluation results provided, we can draw the following conclusions about the performance and effectiveness of the RAG pipeline:

* Context Precision (1.0000): This perfect score indicates that all the information retrieved and used to generate answers is highly relevant to the questions. The system is not including irrelevant or unnecessary information in its context.
* Faithfulness (0.4940): This relatively low score suggests that the generated answers are not always consistent with the provided context. There might be instances of hallucination or the model adding information not present in the retrieved context.
* Answer Relevancy (0.9916): The very high score indicates that the generated answers are highly relevant to the questions asked. The system is producing responses that address the queries effectively.
* Context Recall (0.8750): This good score suggests that the system is retrieving a significant portion of the relevant information needed to answer the questions. However, there's still room for improvement in capturing all necessary context.




1. What conclusions can you draw about performance and effectiveness of your pipeline with this information?

Conclusions:
1. The RAG system excels at retrieving relevant information and generating relevant answers.
2. The main area for improvement is faithfulness, as the system might be prone to generating information not strictly based on the retrieved context.
3. There's a slight gap in context recall, indicating that some relevant information might be missed during retrieval.
4. Overall, the system performs well in terms of relevance and precision but could benefit from improvements in faithfulness to the provided context.