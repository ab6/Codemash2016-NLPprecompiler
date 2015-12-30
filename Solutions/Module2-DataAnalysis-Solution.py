import nltk
from nltk.corpus import state_union



def extract_entity_names(t):
    '''
    Extract entity names from named entity tree returned by NLTK's ne_chunk method
    :param t: tree with pos and NE tags
    :return: list of named entities
    '''
    entity_names = []
    if hasattr(t, 'node') and t.node:
        print ("1")
        if t.node == 'NE':
            print ("2")
            entity_names.append(' '.join([child[0] for child in t]), )
        else:
            for child in t:
                print ("3")
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

    print entity_names

    entCounts = nltk.FreqDist(entity_names)

    return entCounts

    # entity_count = {}
    # for entity in entity_names:
    #     if entity in entity_count:
    #         entity_count[entity] += 1
    #     else:
    #         entity_count[entity] = 1
    #
    # sorted_occurrences = sorted(entity_count.iteritems(), reverse=True, key=operator.itemgetter(1))
    # return sorted_occurrences


#get year and words for each file
docs = [(int(fileid[:4]), state_union.raw(fileid)) for fileid in state_union.fileids()[:2]]

#break text down into tokens, sentences and pos
tokens = [(year, nltk.word_tokenize(text)) for (year, text) in docs]

# sentences = nltk.sent_tokenize(sample)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)

sents = [(year, nltk.sent_tokenize(text.replace("\n", " "))) for (year, text) in docs]
senttokens = [(year, [nltk.word_tokenize(sent) for sent in entry]) for year, entry in sents]

postags = [(year, [nltk.pos_tag_sents(entry)]) for year, entry in senttokens]

ne_tags = [(year, nltk.ne_chunk_sents(pos, binary=True)) for year, pos in postags]
print (sents[0])
print (senttokens[0])
print (postags[0])
print (ne_tags[0])
entities = [(year, extract_entities(tagged)) for year, tagged in ne_tags]



print (sents[0])
print (senttokens[0])
print (postags[0])
print (ne_tags[0])
print (entities[0])

