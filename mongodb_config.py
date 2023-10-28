from app import app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/restaurant"
mongo = PyMongo(app)


def save_to_mongodb(positive_review, negative_review, recomendation):
    data_to_save = {
        'positive review': positive_review,
        'negative review': negative_review,
        'recomendation': recomendation
    }

    if positive_review:
        try:
            id = ObjectId("61d02c106a77339e6ecfdb6b")
            append = {"$push": {"positive_review": {
                "$each": data_to_save["positive review"]}}}
            mongo.db.positive_review.update_one(
                {"_id": id}, append, upsert=True)

            print("Data saved successfully to MongoDB.")

        except Exception as e:
            print(f"exception caught.................................{e}")
    if negative_review:
        try:
            id = ObjectId("615e2955e732d5a52d22a013")
            append = {"$push": {"negative_review": {
                "$each": data_to_save["negative review"]}}}
            mongo.db.negative_review.update_one(
                {"_id": id}, append, upsert=True)

            print("Data saved successfully to MongoDB.")

        except Exception as e:
            print(f"exception caught.................................{e}")
    if recomendation:
        try:
            id = ObjectId("615e2955e732d5a52d22a014")
            append = {"$push": {"recomendation": {
                "$each": data_to_save["recomendation"]}}}
            mongo.db.recomendation.update_one(
                {"_id": id}, append, upsert=True)

            print("Data saved successfully to MongoDB.")

        except Exception as e:
            print(f"exception caught.................................{e}")
