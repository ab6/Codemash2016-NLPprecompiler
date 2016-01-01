import nltk
from nltk.corpus import gutenberg

ids = gutenberg.fileids()

'''['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt',
'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt',
'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt',
'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']'''

blakeWords = gutenberg.words("blake-poems.txt")

fdist = nltk.FreqDist([w.lower() for w in blakeWords])

print (blakeWords[:20])