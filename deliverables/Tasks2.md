## Task 2: Building a Quick End-to-End Prototype

**You are an AI Systems Engineer**.  The SVP of Technology has tasked you with spinning up a quick RAG prototype for answering questions that internal stakeholders have about AI, using the data provided in Task 1.


Task 2: Build an end-to-end RAG application using an industry-standard open-source stack and your choice of commercial off-the-shelf models



✅ Deliverables:

**1. Build a prototype and deploy to a Hugging Face Space, and create a short (< 2 min) loom video demonstrating some initial testing inputs and outputs.**

https://www.loom.com/share/a052024b532048c5bfdcd0f19303fd27

**2. How did you choose your stack, and why did you select each tool the way you did?**

I chose this particular stack for my AI ethics, regulations, and policies Q&A system based on several key considerations:


* Qdrant: I selected Qdrant as my vector database because of its excellent performance in similarity search. For a RAG system, quick and accurate retrieval of relevant information is crucial, and Qdrant excels at this.


* OpenAI: I'm using OpenAI's models for both embeddings (text-embedding-3-small) and text generation (ChatOpenAI). I chose these because they offer state-of-the-art performance in natural language processing tasks. The embedding model helps create high-quality vector representations of my documents, while ChatGPT provides powerful language generation capabilities for answering user queries.


* LangChain: I integrated LangChain into my stack because it provides excellent abstractions for working with various AI components. It simplifies the process of connecting different parts of my system, from document loading to embedding generation and retrieval.


* Chainlit: For the user interface, I went with Chainlit. It's specifically designed for creating chat-based AI applications, which aligns perfectly with my goal of building an interactive Q&A system. Chainlit made it easy to deploy a user-friendly chat interface without having to build one from scratch.


* PyMuPDF (fitz): In my data processing script, I'm using PyMuPDF for extracting text from PDF files. I chose this library because it's efficient and reliable for PDF processing, which is essential given that many AI policy documents are in PDF format.

* RecursiveCharacterTextSplitter: I chose this LangChain utility for text chunking because it provides a smart way to break down large documents into manageable pieces for embedding and retrieval.


Overall, I selected this stack because it offers a balance of performance, ease of use, and flexibility. It allows me to efficiently process and store document information, retrieve relevant context, and generate accurate responses to user queries about AI ethics and policies. The combination of these tools also gives me room to scale and modify my system as needed in the future.