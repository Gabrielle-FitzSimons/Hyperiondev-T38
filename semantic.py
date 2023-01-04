import spacy 

nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

# It is interesting that cat and banana are more similar than cat and apple 
# It is also interesting that monkey and banana are more similar than apple and banana
# this could be because monkeys are commonly associated with bananas 

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

# I found it interesting that cat and apple were more similar than cat and monkey
# I also found it interesting that apple and banana weren't similar at all 
# The programme also produced a UserWarning that this model has no word vectors loaded 
# and therefore isn't the best to use. 

nlp = spacy.load('en_core_web_md')

words = nlp('computer mouse rat cheese ')
for word1 in words:
    for word2 in words: 
        print(word1.text, word2.text, word1.similarity(word2))

# Running my own words it is interesting that mouse and cheese 
# is roughly two times closer than rat and cheese even though they both eat cheese 