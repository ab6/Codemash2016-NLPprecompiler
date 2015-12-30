import operator

def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]), )
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names


def extract_entities(taggedText):
    entity_names = []
    for tree in taggedText:
        entity_names.extend(extract_entity_names(tree))

    #create a map with entity,count count representing
    # the number of occurrences of an entity
    entity_count = {}
    for entity in entity_names:
        if entity in entity_count:
            entity_count[entity] += 1
        else:
            entity_count[entity] = 1

    sorted_occurrences = sorted(entity_count.iteritems(), reverse=True, key=operator.itemgetter(1))
    return sorted_occurrences