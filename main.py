from app import app
from mongodb_config import mongo
from flask import Flask, request, jsonify
from pymongo import MongoClient
from mongodb_config import save_to_mongodb
from textBlob import textBlob
from review import review

# MongoDB configuration
# client = MongoClient('localhost', 27017)
# db = client['movies_sentiment']
# collection = db['comment_sentiment']


@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():

    data = request.json
    print("data........................................")
    print(data)
    print("data........................................")

    if 'comment' in data:
        comment = data['comment']
        # Use the textBlob function for sentiment analysis
        # sentiment = textBlob(comment)
        positive_review, negative_review, recomendation = review(comment)
        save_to_mongodb(positive_review, negative_review, recomendation)
        return jsonify({"message": "Sentiment analysis completed and data saved successfully."}), 200
    else:
        return jsonify({"message": "Invalid data format. Please provide a 'comment' in the JSON payload."}), 400


if __name__ == '__main__':
    app.run(debug=True)
