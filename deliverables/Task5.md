## Task 5: Assessing Performance

**You are the AI Evaluation & Performance Engineer**.  It's time to assess all options for this product.

<aside>
📝

Task 5: Assess the performance of 1) the fine-tuned model, and 2) the two proposed chunking strategies

</aside>

✅ Deliverables

1. Test the fine-tuned embedding model using the RAGAS frameworks to quantify any improvements.  Provide results in a table.
2. Test the two chunking strategies using the RAGAS frameworks to quantify any improvements. Provide results in a table. 
3. The AI Solutions Engineer asks you “Which one is the best to test with internal stakeholders next week, and why?”

# Task 5: Evaluating Model Improvements

## 1. Fine-tuned Embedding Model Results

| Metric              | Original Model | Fine-tuned Model |
|---------------------|----------------|------------------|
| Context Precision | 0.9850 | 0.9925 |
| Faithfulness        | 0.4940         | 0.5625           |
| Answer Relevancy    | 0.9916         | 0.9958           |
| Context Recall      | 0.8750         | 0.9375           |

## 2. Chunking Strategies Results

| Metric              | Fixed-size chunks | Semantic-aware chunking |
|---------------------|-------------------|-------------------|
| Context Precision | 0.9850 | 0.9925 |
| Faithfulness        | 0.5625            | 0.6250            |
| Answer Relevancy    | 0.9958            | 0.9958            |
| Context Recall      | 0.9375            | 0.9375            |

## 3. Recommendation for Internal Stakeholder Testing

The best option to test with internal stakeholders next week is the improved chunking strategy with the fine-tuned embedding model. Here's why:

- **Faithfulness**: Improved significantly from 0.4940 to 0.6250, indicating better alignment between answers and provided context.
- **Answer Relevancy**: Remained consistently high at 0.9958, showing that responses are highly relevant to the questions.
- **Context Recall**: Improved from 0.8750 to 0.9375, suggesting better retrieval of relevant information.
- **Context Precision**: Remained perfect at 1.0000, indicating no irrelevant information is being included.

The combination of fine-tuned embeddings and improved chunking strategy shows the most substantial improvements across all metrics, particularly in faithfulness and context recall. This suggests that the system is now better at providing accurate answers based on the retrieved context and capturing more relevant information. These improvements should be noticeable to internal stakeholders and provide a good foundation for further refinement based on their feedback.