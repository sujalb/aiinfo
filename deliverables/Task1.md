**Task 1: Dealing with the Data**

You identify the following important documents that, if used for context, you believe will help people understand what’s happening now:
    1. 2022: Blueprint for an AI Bill of Rights: Making Automated Systems Work for the American People (PDF)
    2. 2024: National Institute of Standards and Technology (NIST) Artificial Intelligent Risk Management Framework (PDF)

Your boss, the SVP of Technology, green-lighted this project to drive the adoption of AI throughout the enterprise. It will be a nice showpiece for the upcoming conference and the big AI initiative announcement the CEO is planning.


**Task 1: Review the two PDFs and decide how best to chunk up the data with a single strategy to optimally answer the variety of questions you expect to receive from people.
Hint: Create a list of potential questions that people are likely to ask!**

| Question | Potential Theme | Definition |
|----------|-----------------|------------|
| What measures are recommended to ensure AI systems are safe for public use? | Safe and Effective Systems | This is a core principle in the AI Bill of Rights, emphasizing the need for AI systems to be safe and effective for their intended use. |
| How can we evaluate the effectiveness of AI systems in real-world applications? | Safe and Effective Systems | |
| What safeguards are proposed to prevent AI from perpetuating biases? | Algorithmic Discrimination Protections | Both documents stress the importance of preventing bias and discrimination in AI systems |
| How can we detect and mitigate algorithmic discrimination in AI systems? | Algorithmic Discrimination Protections | |
| What guidelines are provided for protecting individual privacy in AI systems? | Data Privacy | This is a crucial aspect covered in the AI Bill of Rights, focusing on protecting individual privacy in AI systems |
| How should companies handle personal data when developing AI applications? | Data Privacy | |
| What level of transparency is required when deploying AI systems? | Notice and Explanation | This theme relates to the principle of providing clear information about when and how AI systems are being used, as outlined in the AI Bill of Rights. |
| How should organizations communicate to users that they're interacting with an AI? | Notice and Explanation | |
| In what situations should human alternatives to AI systems be mandatory? | Human Alternatives | The AI Bill of Rights emphasizes the importance of providing alternatives to AI systems when appropriate. |
| How can organizations balance AI automation with human oversight? | Human Alternatives | |
| What are the key steps in assessing and mitigating risks associated with AI systems? | Risk Management | This is a central theme in the NIST AI Risk Management Framework, focusing on identifying and mitigating risks associated with AI systems. |
| How often should AI risk assessments be conducted? | Risk Management | |
| What governance structures are recommended for overseeing AI development and deployment? | Governance | Both documents discuss the importance of proper governance structures for AI systems |
| Who should be responsible for ensuring AI systems comply with ethical guidelines? | Governance | |
| How can organizations build public trust in their AI systems? | Trustworthiness | This is an overarching theme in both documents, emphasizing the need for AI systems to be reliable, fair, and transparent. |
| What metrics can be used to measure the trustworthiness of an AI application? | Trustworthiness | |
| N/A | Unclassified | If a chunk doesn't match any predefined theme, it's added to the "Unclassified" category |





✅ Deliverables:

**1. Describe the default chunking strategy that you will use.**

The default chunking strategy used is a combination of size-based splitting and thematic categorization. 
This strategy uses RecursiveCharacterTextSplitter with a chunk size of 1000 characters and an overlap of 200 characters. It then categorizes these chunks based on predefined themes.

**2.  Articulate a chunking strategy that you would also like to test out.**
    

A pure size-based chunking strategy without thematic categorization. This would involve splitting the text into fixed-size chunks without attempting to categorize them based on themes.

**3. Describe how and why you made these decisions**

The default strategy was chosen for its simplicity and efficiency:

* Size-based splitting (1000 characters) ensures manageable chunk sizes for processing and embedding.
* The 200-character overlap helps maintain context between chunks.
* Thematic categorization allows for organized retrieval based on specific topics of interest.

This approach balances processing efficiency with maintaining semantic coherence within chunks.

The alternative pure size-based strategy:
* Ensures consistent chunk sizes, which can be beneficial for processing and embedding.
* Is simpler to implement and doesn't rely on predefined themes.
* May split semantic units, potentially affecting the coherence of individual chunks.'
* Could be more comprehensive, including all parts of the document regardless of theme.






