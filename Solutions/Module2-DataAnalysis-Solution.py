'''
Name: Module2-DataAnalysis-Solution.py
Date: January 5, 2016
Author: Amber McKenzie
Codemash 2016 - Precompiler
https://github.com/ab6/Codemash2016-NLPprecompiler.git

This module is designed to present NLP basics from the NLTK within a basic data analysis application.
It covers word tokenization, sentence tokenization, part-of-speech (pos) tagging, and named entitiy tagging.
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
    Extract entity names from named entity tree returned by NLTK ne_chunk method
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
docs = [(int(fileid[:4]), state_union.raw(fileid)) for fileid in state_union.fileids()]

#break text down into sentences, tokens
tokens = [(year, nltk.word_tokenize(text)) for year, text in docs]
sents = [(year, nltk.sent_tokenize(text.replace("\n", " "))) for (year, text) in docs]
senttokens = [(year, [nltk.word_tokenize(sent) for sent in entry]) for year, entry in sents]

#get counts of unique words and plot over time
unique = [(year, len(set(words))) for year, words in tokens]
years, wordcounts = zip(*unique)
plt.scatter(years, wordcounts)
# plt.show()

#get unique/total ratio
ratio = [(year, float(len(set(words)))/float(len(words))) for year, words in tokens]
years, lengths = zip(*ratio)
plt.scatter(years, lengths)
# plt.show()

#chunk text and extract entities
postags = [(year, nltk.pos_tag_sents(entry)) for year, entry in senttokens]
ne_tags = [(year, nltk.ne_chunk_sents(pos, binary=True)) for year, pos in postags]
entities = [(year, extract_entities(tagged)) for year, tagged in ne_tags]
entFreqs = [(year, nltk.FreqDist(entry)) for year, entry in entities]

#get freq dist of all entities
ents = [entityList for year, entityList in entities]
allentities = [item for sublist in ents for item in sublist]
allentfreq = nltk.FreqDist(allentities)

#make list of top 50 most frequent and prune individual docs to take out filtered words
filtered = allentfreq.keys()[:50]
pruned = [(year, list(set(entFreq.keys()) - set(filtered))) for year, entFreq in entFreqs]

for year, list in pruned:
    print (year)
    print (list)


