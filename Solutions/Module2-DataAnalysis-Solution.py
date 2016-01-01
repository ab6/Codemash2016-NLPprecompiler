import nltk
from nltk.corpus import state_union



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
    entCounts = nltk.FreqDist(entity_names)

    return (entCounts)


#get year and words for each file
docs = [(int(fileid[:4]), state_union.raw(fileid)) for fileid in state_union.fileids()[:2]]
text = state_union.raw("1945-Truman.txt")


#break text down into tokens, sentences and pos
tokens = [(year, nltk.word_tokenize(text)) for (year, text) in docs]

sents = [(year, nltk.sent_tokenize(text.replace("\n", " "))) for (year, text) in docs]

senttokens = [(year, [nltk.word_tokenize(sent) for sent in entry]) for year, entry in sents]

postags = [(year, nltk.pos_tag_sents(entry)) for year, entry in senttokens]

ne_tags = [(year, nltk.ne_chunk_sents(pos, binary=True)) for year, pos in postags]

entities = [(year, extract_entities(tagged)) for year, tagged in ne_tags]

# print (sents[0])
# print (senttokens[0])
# print (postags[0])
# print (ne_tags[0])
# print (entities[0])

