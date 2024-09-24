## Task 4: Fine-Tuning Open-Source Embeddings

**You are a Machine Learning Engineer.**  The AI Evaluation and Performance Engineer has asked for your help in fine-tuning the embedding model used in their recent RAG application build. 



Task 4: Generate synthetic fine-tuning data and complete fine-tuning of the open-source embedding model



✅ Deliverables

1. Swap out your existing embedding model for the new fine-tuned version.  Provide a link to your fine-tuned embedding model on the Hugging Face Hub.
2. How did you choose the embedding model for this application?


* The fine-tuned model is now available at https://huggingface.co/svb01/fine-tuned-embedding-model


**Model choice explanation**: "I chose the 'sentence-transformers/all-MiniLM-L6-v2' model as the base for fine-tuning because it provides a good balance between performance and efficiency. It's a lightweight model that performs well on a variety of tasks and is suitable for fine-tuning on domain-specific data. By fine-tuning this model on our thematic chunks, we create embeddings that are more tailored to our specific AI policy and regulation domain, potentially improving the performance of our RAG application."

Summary of how fine-tuning is working in fine_tune_model.py script:
* Data Preparation:
  * The script reads PDF files from a 'resources' folder.
  * It extracts text from these PDFs and chunks the text into smaller segments.
  * The chunks are categorized into predefined themes based on keyword matching.
* Synthetic Data Generation:
  * For each theme, the script generates synthetic question-answer pairs.
  * Questions are formulated as "What does this text say about [theme]?"
  * Answers are the text chunks associated with each theme.
  * This creates a dataset of InputExample objects for training.
* Model Initialization:
  * The script starts with a pre-trained model: "sentence-transformers/all-MiniLM-L6-v2".
  * This is a general-purpose sentence embedding model.
* Fine-tuning Process:
  * The fine_tune_model function sets up the training loop:
  * It creates a DataLoader for batch processing.
  * It uses MultipleNegativesRankingLoss as the training objective.
  * The model is trained for 3 epochs with a warmup of 100 steps.
  * The fine-tuning process adjusts the model's weights to better represent the specific domain of your data.
* Model Saving:
  * After fine-tuning, the model is saved locally to "fine_tuned_embedding_model".
  * It's then uploaded to the Hugging Face Hub under the repository "svb01/fine-tuned-embedding-model"