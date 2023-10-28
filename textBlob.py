import nltk
import pandas as pd
import numpy as np
import textblob


def textBlob(comment):

    sentiment_polarity = textblob.TextBlob(comment).sentiment.polarity
    print("sentiment polarity---", sentiment_polarity)

    predicted_sentiments = "Positive" if sentiment_polarity >= 0.1 else 'Negative'

    return predicted_sentiments
