# -*- coding: utf-8 -*-
import spacy

# Setup nlpnet data_dir
nlp = spacy.load('pt')

phrase = input('Qual a sua frase? ')

word = nlp(phrase)

phrase_lemma = []
for token in word:
  phrase_lemma.append(token.lemma_)

print(' '.join(phrase_lemma))
