# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from nltk.tokenize import sent_tokenize, word_tokenize


def end_punctuation_space(comment): return re.sub(
    r'(?<!\s)([.!?…]+)(?!\s)', r'\1 ', comment)


def end_punctuation_split(sentences):
    comments = []
    for sentence in sentences:
        split = re.split(
            r'[.!?]+', sentence)
        for comment in split:
            if comment:
                comments.append(comment)
    return comments


def split_by_but(comments):
    temp = []
    for comment in comments:
        split = comment.split("but")
        for s in split:
            if s and s != "but":
                temp.append(s)
    return temp


def review(comment):
    # comment preprocess SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    # comment = input("write your comment:")
    comment = comment.casefold()
    comment = end_punctuation_space(comment)
    print(f"fullstop----- {comment}")
    sentences = sent_tokenize(comment)
    print(f"sent_tokenizer----- {sentences}")
    comments = end_punctuation_split(sentences)
    print(f"punctuation split-----{comments}")
    comments = split_by_but(comments)
    print(f"split but-----{comments}")
    # comment preprocess EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

    # sentiment analysis SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    sentiment = SentimentIntensityAnalyzer()
    vaderScores = [sentiment.polarity_scores(
        single_comment) for single_comment in comments]

    print(f"sentiment-----{vaderScores}")

    positive_review = []
    negative_review = []
    recomendations = []

    for i, vaderScore in enumerate(vaderScores):
        comment = comments[i]
        if vaderScore["compound"] >= 0.2:
            positive_review.append([comment, vaderScore])

        elif vaderScore["compound"] <= -0.2:
            negative_review.append([comment, vaderScore])

        else:
            if vaderScore["pos"] > vaderScore["neg"]:
                positive_review.append([comment, vaderScore])

            if vaderScore["pos"] < vaderScore["neg"]:
                negative_review.append([comment, vaderScore])

            else:
                recomendations.append([comment, vaderScore])
    # sentiment analysis EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

    return positive_review, negative_review, recomendations


# while True:
#     review("")
