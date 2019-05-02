from pymongo import MongoClient
import gmaps
import gmaps.datasets

client = MongoClient()
db = client["twitter_db"]
collection = db.twitter_collection

coord = []  # array to hold coordinates
count = 0
stop_count = 100

while True:
    for obj in collection.find():
        if obj['geo'] is None:
            continue

        coord.insert(0, obj['geo']['coordinates'])
        count = count + 1

        if count > stop_count:
            break
    if count > stop_count:
        break
print(coord)


def map_tweets(tweets, keyword):
coords = []
for tweet in tweets:
    if keyword is in tweet["text"]:
        coords.append(tweet["geo"])
return coords

coords = map_tweets(tweets, "weed")

gmaps.configure(api_key="AIzaSyADv13vyns8lTpdjwoxMwYL3Q0k2Eqoyno")
locations = coord
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig