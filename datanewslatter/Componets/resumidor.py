import nltk
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

def resumidor(texto):
    parepalavras = nltk.corpus.stopwords.words('portuguese')+ list(punctuation)
    sentencas = nltk.sent_tokenize(texto)
    palavras = nltk.word_tokenize(texto.lower())
    nopareplavra = [palavra for palavra in palavras if palavra not in parepalavras]

    frequencia = FreqDist(nopareplavra)
    sqimportant = defaultdict(int)

    for i, sentenca in enumerate(sentencas):
        for palavra in nltk.word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sqimportant[i] += frequencia[palavra]

    idx_sqimportant = nlargest(2, sqimportant, sqimportant.get)
    for i in sorted(idx_sqimportant):
        return sentencas[i]

