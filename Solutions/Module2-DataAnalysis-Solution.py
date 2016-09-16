'''
Name: Module2-DataAnalysis-Solution.py
Date: November 11, 2016
Author: Amber McKenzie
QCon San Francisco 2016
https://github.com/ab6/QConSF-2016.git

This module is designed to present NLP basics from the NLTK within a basic data analysis application.
It covers word tokenization, sentence tokenization, bigrams, part-of-speech (pos) tagging, and named entity tagging.
For additional information and prerequisites, see the readme on the github repo.

Notes:
-Code will take a while to run if run on the entire state-union corpus.
-Code will not proceed past the plots until each plot window is closed.
'''


import nltk
from nltk.corpus import state_union
import matplotlib.pyplot as plt

def extract_entity_names(t):
    '''
    Extract entity names from named entity tree returned by NLTK ne_chunk_sents method
    :param t: tree with pos and NE tags
    :return: list of named entities
    '''
    entity_names = []
    if hasattr(t, 'label'):
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]), )
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

def extract_entities(taggedText):
    '''
    Create map with entity and their counts
    :param taggedText: Parsed text (output of ne chunker) in tree form
    :return: dict of entities and their freq counts
    '''
    entity_names = []
    for tree in taggedText:
        entity_names.extend(extract_entity_names(tree))
    return entity_names


#get year and words for each file
extracted= [(state_union.raw(fileid), int(fileid[:4])) for fileid in state_union.fileids()]
docs, years = zip(*extracted)

#break text down into sentences, tokens
tokens = [nltk.word_tokenize(text) for text in docs]
sents = [nltk.sent_tokenize(text.replace("\n", " ")) for text in docs]
senttokens = [[nltk.word_tokenize(sent) for sent in entry] for entry in sents]

#get counts of unique words and plot over time
unique = [len(set(words)) for words in tokens]
plt.scatter(years, unique)
plt.show()

#get unique/total ratio
ratios = [(float(len(set(words)))/float(len(words))) for words in tokens]
plt.scatter(years, ratios)
plt.show()

#get top bigrams for each year
lower = [[word.lower() for word in words] for words in tokens]
bigrams = [nltk.FreqDist(nltk.bigrams(items)) for items in lower]
print ("Top 10 bigrams by year")
for bis, year in zip(bigrams, years):
    print (year, bis.keys()[:10])

#chunk text and extract entities
postags = [nltk.pos_tag_sents(entry) for entry in senttokens]
ne_tags = [nltk.ne_chunk_sents(pos, binary=True) for pos in postags]
ents = [extract_entities(tagged) for tagged in ne_tags]
entFreqs = [nltk.FreqDist(entry) for entry in ents]

#get freq dist of all entities
allentities = [item for sublist in ents for item in sublist]
allentfreq = nltk.FreqDist(allentities)

#make list of top 50 most frequent and prune individual docs to take out filtered words
filtered = allentfreq.keys()[:50]
pruned = [(list(set(entFreq) - set(filtered))) for entFreq in entFreqs]

print ("Top 10 entities by year")
for year, list in zip(years, pruned):
    print (year, pruned[:10])




