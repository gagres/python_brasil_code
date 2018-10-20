# -*- coding: utf-8 -*-
import spacy

# Setup nlpnet data_dir
nlp = spacy.load('pt')

word = nlp(u'Essa é uma frase bem longa, vamos ver como o spacy trata')

phrase_lemma = []
for token in word:
  phrase_lemma.append(token.lemma_)

print(' '.join(phrase_lemma))
