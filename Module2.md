#Precompiler - Introduction to NLP using NLTK and Python
- Codemash 2016
- January 5th, 2016
- Amber McKenzie

##Module 2 - Data Analysis from Raw Text using NLTK
This module is designed to present NLP basics from NLTK within a basic data analysis application. It covers word tokenization, sentence tokenization, bigrams, part-of-speech (pos) tagging, and named entity tagging.

The data for this application will be the C-Span State of the Union Address Corpus available via the Python NLTK package.  More information for each corpus in NLTK can be found on the NLTK.org website:
http://www.nltk.org/nltk_data/

We will be importing the raw text from the NLTK state_union corpus and extracting the year for each document.  We will then use NLTK functions on the raw text (not the corpus-provided words and sentences) to accomplish the following:
- Plot the counts of unique words over time
- Plot ratio of unique-to-total words over time
- Print the top bigrams for each year
- Print the top entities for each year
- The provided helperFunctions.py file in the repository will assist in parsing the output for the nltk.ne_chunk_sents() method.  Analyze the provided functions to assess the required inputs and outputs to help guide your solution.

###Module 2 Hints and Tricks
- The State of the Union is a PlainTextCorpusReader
  - The text for each address can be accessed using the .raw() function for each fileid.  NLTK functions can be performed on this raw text to produce the desired output
- Remember to analyze the functions in helperFunctions.py and use them in your solution
  - The nltk.ne_chunk() and nltk.ne_chunk_sents() functions give different outputs. Pay attention to which function you are using when passing data into the functions in helperFunctions.py
- The matplotlib Python library will be used in this module.  
  - The documentation for the library can be found here: http://matplotlib.org/
  - Code will stop executing once a graph is shown until the graph is closed. Close each graph after you are finished viewing the results.
- The code will take some time to run if run on the entire corpus  

###Module 2 Walkthrough
- Get the year and text for each document in the corpus
- Break each text into tokenized sentences using NLTK functions
- Get counts of the unique words for each year and use matplotlib to create a graph
- Calculate the ratio of unique words to total words for each year and use matplotlib to create a graph
- Determine the top 10 bigrams for each year and print the output
- Use nltk.ne_chunk_sents() and the helper functions to do named entity tagging on the documents
- Generate a frequency distribution for entities across all documents
- Determine the top 50 entities from the full entity frequency distribution
- Prune out the common entities and display the top entities from each year

###Module 2 Additional Goals
- Look at the counts of different parts of speech (ex: adjectives vs. verbs). 
  - How does it change over time?
- Group the documents by president or political party rather than year. 
  - Do the document topics align?
- Refine the bigrams by filtering out stopwords or performing a collocation. 
  - How does the data change?
- Perform sentiment analysis on the documents.  
  - Can you think of any factors (historical events, political party, economic status) that would change the overall sentiment of the address?
