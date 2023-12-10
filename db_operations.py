#db_operations.py

import pymongo

mongo_url = "mongodb+srv://admin:admin@cluster0.uksugso.mongodb.net/dictation"

try:
    client = pymongo.MongoClient(mongo_url)
    if client.server_info():
        print("Connected to MongoDB successfully!")
    db = client.dictation
    Collection = db.user_google
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")

userName = "tuan.nguyen19051996@hcmut.edu.vn"
    
def get_user_full_name():
    try:
        user_full_name = Collection.find_one({"userName": userName})["fullName"]
        return user_full_name
    except Exception as e:
        print(f"Error retrieving user name: {str(e)}")
        return "Not Found"
    
def get_score():
    try:
        user_scores = db.score.find({"userName": userName}).sort("time", -1).limit(1)
        scores_list = [score["score"] for score in user_scores]
        return scores_list
        # user_scores = db.score.find({"userName": userName}).sort("time", -1).limit(3)
        # # scores_list = [(score["time"], score["score"]) for score in user_scores]
        # scores_list = [score["score"] for score in user_scores]
        # return f"3 latest scores: {scores_list}"
    except Exception as e:
        return "Not Found"