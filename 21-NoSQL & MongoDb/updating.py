import pymongo
from bson.objectid import ObjectId
from pymongo import collection


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://semainal:wui8SW5GZfgyLw11@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

#update_one

# mycollection.update_one({
#     "name": "Samsung S6"},
#     {"$set": {
#         "name": "Iphone 7",
#         "price": 5000
#     }})

# for i in mycollection.find():
#     print(i)


#update_many

# mycollection.update_many({
#     "name": "Samsung S10"},
#     {"$set": {
#         "name": "Iphone 10",
#         "price": 7500
#     }})

# for i in mycollection.find():
#     print(i)

#farklı bir kullanım şekli:

query = {"name": "Samsung S11"}
newvalues= {"$set": {
    "name": "Iphone 12", "price": 12000
}}

result =  mycollection.update_many(query,newvalues)

print(f"{result.modified_count} adet kayıt güncellendi.")

for i in result:
    print(i)
