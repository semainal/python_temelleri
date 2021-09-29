import pymongo
from bson.objectid import ObjectId


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://semainal:wui8SW5GZfgyLw11@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


# filter = {"name": "Samsung S5"}
# result = mycollection.find(filter)

# result = mycollection.find_one(filter)  tek kayıt dönmesi için
# result =  mycollection.find_one({"_id": ObjectId("6137cfa9b60f09716caf7757")})
# for i in result:
#     print(i)


# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })

# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
#         "$gt": 2000
#     }
# })


# result = mycollection.find({
#     "price": {
#         "$gte": 2000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq": 2000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lt": 2000
#     }
# })

result = mycollection.find({
    "name": {"$regex": "^S"}
})

for i in result:
    print(i)