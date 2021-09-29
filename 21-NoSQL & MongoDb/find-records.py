import pymongo
from bson.objectid import ObjectId


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://semainal:wui8SW5GZfgyLw11@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# tek kayıt için:

# result = mycollection.find_one()

# print(result)

#çoklu kayıt için:

# for i in mycollection.find({},{"_id":0, "name":1, "price": 1}):
# for i in mycollection.find({},{"_id":0}):
for i in mycollection.find({},{"name":1}):
    print(i)

