import pymongo
from bson.objectid import ObjectId
from pymongo import collection


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://semainal:wui8SW5GZfgyLw11@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#delete_one()
#delete_many()

for i in mycollection.find():
    print(i)

print("*"*50)

# mycollection.delete_one({"name":"Iphone 12"})
# mycollection.delete_many({"name":
# {"$regex": "^S"}})

result = mycollection.delete_many({}) # bütün kayıtları siler.

print(f"{result.deleted_count} adet kayıt silindi.")
for i in mycollection.find():
    print(i)

print("*"*50)