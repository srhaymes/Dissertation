import tweepy
import json
import pymongo
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from pymongo import MongoClient

# Twitter API credentials
consumer_key = "Aydwt7ZY9hEEsJKyN4LOz5fTI"
consumer_secret = "dKAXuqCkaFrp0B6ZI8twwiYmb6xEPN848vkh3Z74XFBhXNegi7"
access_key = "477823860-imARokjepWo4MgCm6t7Im2VeKqquiY10gL3v4YbZ"
access_secret = "a0wuEMNfpaFXobwc9FYBOlSo0xbPTtRTV0vtMREpmB1FR"

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# override tweepy.StreamListener to add logic to on_status, on_error & on_data
class MyStreamListener(tweepy.StreamListener):
        # currently does nothing
    def on_status(self, status):
        print(status.text)
        try:  # insert tweets to mongodb
            collection.insert(status._json)

        # Error handling
        except BaseException as e:
            print("Error on_status: %s" % str(e))

        return True

    # use on_error to catch 420 errors and disconnect stream.
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_data(self, data):
        try:
            # try block takes json data and inserts into mongoDB
            client = MongoClient()
            db = client["twitter_db"]
            # decode json from twitter
            datajson = json.loads(data)
            # get created at for print statement
            created_at = datajson["created_at"]
            # print every time tweet is collected
            print("Tweet collected at " + str(created_at))
            # insert data into twitter_collection collection
            db.twitter_collection.insert(datajson)
        except Exception as e:
            print(e)


# Tweets stream at a faster rate than I can accept them which causes an IncompleteRead error,
#  this function restarts the stream when it errors
def start_stream():
    while True:
        try:
            # Create a stream object
            twitter_stream = tweepy.Stream(auth, MyStreamListener())
            # uk location
            twitter_stream.filter(locations=[-6.38, 49.87, 1.77, 55.81])
        except:
            continue


start_stream()
