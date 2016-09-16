#Precompiler - Introduction to NLP using NLTK and Python
- Codemash 2016
- January 5th, 2016
- Amber McKenzie

##General Notes:
Many helpful resources are available online including:
- The Python 3 Reference: https://docs.python.org/3/reference/
- The NLTK Book: http://www.nltk.org/book/
- The NLTK Module Reference: http://www.nltk.org/api/nltk.html
  - Specifically useful for Module 2: http://www.nltk.org/_modules/nltk/corpus/reader/plaintext.html
- NLTK Data: http://www.nltk.org/nltk_data/

##Module 1 - Document Categorization via Naive-Bayes Classifier Model
In this module, we will explore document categorization based on word frequency distribution by using a simple classifier trained on a known corpus. We will then use a small subset of the data to test the accuracy of the model.  These techniques can be applied to other models and data sets.

The data for this application will be the Brown Corpus available via the Python NLTK package.  More information for each corpus in NLTK can be found on the NLTK.org website:
http://www.nltk.org/nltk_data/

To achieve this goal, do the following:
- Load the Brown Corpus documents word lists and categories
- Run a frequency distribution on all the words in the corpus
- Determine a set of words to be the feature set based on some threshold
- For each document, create a dict of each feature word that indicates if it exists in the document
- Pair the feature set (dict) for each document with the document category
- Shuffle the feature word-category pairings and split into two sets:
  - 80% into a training set
  - 20% into a test set
- Run the training set through a Naive-Bayes Classifier
- Run an accuracy test on the classifier using the created Naive-Bayes Classifier and the test set
- Print the resulting accuracy

###Module 1 Hints and Tricks
- The Brown Corpus is a CategorizedTaggedCorpusReader
- Words for the corpus can be accessed via the .words() function
- Passing an array of file ids will return all matching words
- Categories can be accessed via the .categories() function
- Passing an array of file ids will return all matching categories
- The Naive-Bayes Classifier is a simple classification algorithm
  - Available through NLTK: http://www.nltk.org/_modules/nltk/classify/naivebayes.html
- Use a smaller number of features while debugging. Once debugged, can up the number of features.

###Module 1 Walkthrough
- Load the Brown corpus data into word list/category pairs
- Load all words from the Brown corpus
- Run a frequency distribution on all the words to order words by number of appearances
- Chop off the ordered word list at an arbitrary number or find threshold in the frequency count that scales down the size of the word list to a manageable feature word set
- For each document, create a dict of every feature word with the value a boolean for the existence of the word in the document
- Create a list of tuples of the document feature word dicts and the document category
- Shuffle the tuple list using random.shuffle
- Break the shuffled tuple list into two lists: 
  - 20% into test 
  - 80% into training
- Use the NLTK Naive Bayes Classifier on the training set to generate a model
- Calculate the model accuracy by passing in the classifier and the test set into NLTK Classifier Analyze
- Print the calculated accuracy on the test set

###Module 1 Additional Goals
- Try filtering the feature word list using stopwords.  
  - How does this affect the accuracy?
- Break the Brown corpus documents into into imaginative and informative prose lists and run a model on each list in a similar fashion.
  - Is the accuracy any better for the separated document lists?
- Stem the document words to provide a more concise list. 
  - Is the accuracy any better?
