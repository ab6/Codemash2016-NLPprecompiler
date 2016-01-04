import nltk
from nltk.corpus import gutenberg

#get the file ids for the corpus
ids = gutenberg.fileids()

#get the words and raw text for the first ebook
emmaWords = gutenberg.words("austen-emma.txt")
emmaText = gutenberg.raw([ids[0]])

#get the frequency distribution for the words in ebook
fdist = nltk.FreqDist([w.lower() for w in emmaWords])

