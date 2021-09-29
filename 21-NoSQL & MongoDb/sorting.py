import pymongo
from bson.objectid import ObjectId


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://semainal:wui8SW5GZfgyLw11@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort("name") # isme göre sırlama
# result = mycollection.find().sort("name",-1) # tersten sırlama
# result = mycollection.find().sort("price")

result = mycollection.find().sort([("name",1),("price",-1)]) # önce isme göre artan, sonra fiyata göre azalan



for i in result:
    print(i)
