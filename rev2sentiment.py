import pandas as pd
import numpy as np
import nltk
from textblob import TextBlob

def rev2sentiment(reviewlist):
    output =[]
    for i in range(len(reviewlist)):
        esp= TextBlob(reviewlist[i])
        output = output + [esp.sentiment.polarity]

    return pd.DataFrame(output)