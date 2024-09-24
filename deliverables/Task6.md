## Task 6: Managing Your Boss and User Expectations

**You are the SVP of Technology**.  Given the work done by your team so far, you're now sitting down with the AI Solutions Engineer.  You have tasked the solutions engineer to test out the new application with at least 50 different internal stakeholders over the next month.

1. What is the story that you will give to the CEO to tell the whole company at the launch next month?



**Story for the CEO to tell the whole company at the launch next month:**


"I'm excited to announce the launch of our innovative AI application, designed to navigate the complexities of AI ethics, regulations, and policies. Our technology team has developed a sophisticated system that combines advanced natural language processing with a robust knowledge base to provide accurate, context-aware responses to queries about AI governance.
Key features of our application include:

* A custom-trained embedding model that understands the nuances of AI policy documents
* A powerful vector database (Qdrant) for efficient storage and retrieval of information
* An intuitive chat interface powered by Chainlit, allowing users to ask questions in natural language
* Integration with OpenAI's advanced language models for generating human-like responses


Our application processes various PDF documents, categorizing information into themes such as 'Safe and Effective Systems', 'Algorithmic Discrimination Protections', and 'Data Privacy'. This thematic approach ensures that responses are tailored to specific areas of AI governance.

Over the next month, our AI Solutions Engineer will be conducting extensive testing with 50 internal stakeholders, ensuring that the application meets the diverse needs of our organization. This collaborative approach will help us refine and improve the system, making it an invaluable resource for our company as we navigate the evolving landscape of AI regulation.

This application demonstrates our commitment to staying at the forefront of AI technology while ensuring compliance with important regulatory frameworks. It's a testament to our team's innovation and our company's dedication to responsible AI development."



2. There appears to be important information not included in our build, for instance, the [270-day update](https://www.whitehouse.gov/briefing-room/statements-releases/2024/07/26/fact-sheet-biden-harris-administration-announces-new-ai-actions-and-receives-additional-major-voluntary-commitment-on-ai/) on the 2023 executive order on [Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/).  How might you incorporate relevant white-house briefing information into future versions?


Build a continous integration pipeline that will allow the white-house briefing information to be incorporated into Qdrant database. This can be easily achieved by using a trigger based approach . When a new file is added to the repository, the pipeline will be triggered to get the embeddings and add to the Qdrant database. 
