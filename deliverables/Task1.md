**Task 1: Dealing with the Data**

You identify the following important documents that, if used for context, you believe will help people understand what’s happening now:
    1. 2022: Blueprint for an AI Bill of Rights: Making Automated Systems Work for the American People (PDF)
    2. 2024: National Institute of Standards and Technology (NIST) Artificial Intelligent Risk Management Framework (PDF)

Your boss, the SVP of Technology, green-lighted this project to drive the adoption of AI throughout the enterprise. It will be a nice showpiece for the upcoming conference and the big AI initiative announcement the CEO is planning.


Task 1: Review the two PDFs and decide how best to chunk up the data with a single strategy to optimally answer the variety of questions you expect to receive from people.
Hint: Create a list of potential questions that people are likely to ask!




✅ Deliverables:

1. Describe the default chunking strategy that you will use.
<div style="color: green;">   
The default chunking strategy used is a combination of size-based splitting and thematic categorization. 
This strategy uses RecursiveCharacterTextSplitter with a chunk size of 1000 characters and an overlap of 200 characters. It then categorizes these chunks based on predefined themes.
</div>

2.  Articulate a chunking strategy that you would also like to test out.
    
<div style="color: green;">
A pure size-based chunking strategy without thematic categorization. This would involve splitting the text into fixed-size chunks without attempting to categorize them based on themes.
</div>



3. Describe how and why you made these decisions
<div style="color: green;">   
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
</div>





