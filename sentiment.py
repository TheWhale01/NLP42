from sqlite3 import Row
from torch import positive
import csv
import pandas as pd
from textblob import TextBlob


def ft_sentiment(corpus):    
    for key in corpus.keys():
        polarity = []
        for tweet in corpus[key]:
            polarity.append(TextBlob(tweet).sentiment[0])
        corpus[key] = polarity
    print(corpus)
    return corpus

def ft_opignion(sentiment):
    
    for key in sentiment.keys():
        neutral = 0
        negatif = 0
        positif = 0
        for i in sentiment[key]:
            if i > -0.2 and i < 0.2:
                neutral += 1
            elif i < -0.2:
                negatif += 1
            else:
                positif += 1
        sentiment[key] = [positif, neutral, negatif]
    print(sentiment)
    return sentiment
    

def ft_write_csv(opignion):
    header = ["topic", "positif", "neutral", "negatif", "total", "p/n%"]
    f = open("./blabla.csv", 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    for key in opignion.keys():
        pos, net, neg = opignion[key]
        total = pos + net + neg
        writer.writerow((key, pos, net, neg , total, (pos / (neg * (total - net))*100)))
    f.close()

corpus = {"apple": ["I love this ", "ces de la merde ce film, rembourser", "this movie is just amazing", "un pur chf-D'oeuvre", "your a fucking idiot", "USA, USA, USA"], "gateau": ["le gateau est incroyablement bon, miam miam", "nice cake", "disgusting cake"]}
sentiment = ft_sentiment(corpus)
opignion = ft_opignion(sentiment)
ft_write_csv(opignion)
fd = pd.read_csv("./blabla.csv")
print(fd)
