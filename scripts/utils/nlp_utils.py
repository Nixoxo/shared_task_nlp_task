import spacy
print("Loading spacy ...")
nlp_en = spacy.load('en')
nlp_de = spacy.load('de')
print("Finished")

def nlp_sentence(sentence):
    parsed = nlp_en(sentence)
    lemmas = []
    words = []
    tags = []
    poss = []
    for i, token in enumerate(parsed):
        lemma = token.lemma_
        words.append(token)
        lemmas.append(lemma)
        tag = token.tag_
        pos = token.tag_
        tags.append(tag)
        poss.append(pos)
    return words, lemmas, tags, poss

def nlp_satz(sentence):
    parsed = nlp_de(sentence)
    lemmas = []
    words = []
    tags = []
    poss = []
    for i, token in enumerate(parsed):
        lemma = token.lemma_
        words.append(token)
        lemmas.append(lemma)
        tag = token.tag_
        pos = token.tag_
        tags.append(tag)
        poss.append(pos)
    return words, lemmas, tags, poss

def spacy_words_to_string_array(words):
    arr = []
    for word in words:
        arr.append(str(word))
    return arr