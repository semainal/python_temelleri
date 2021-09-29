import pymongo


#Local Host için bağlantı:

"""
myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]

print(myclient.list_database_names())
"""

#Uzaktaki database'e bağlantı için:

myclient = pymongo.MongoClient("mongodb+srv://semainal:uneG2I8BJfVJ2YXu@cluster0.qvprj.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#tek ürün ekleme
"""
product = {
    "name": "Samsung S5","price": 2000
}

result = mycollection.insert_one(product)
print(result)
print(type(result))
print(result.inserted_id)
"""

# çoklu ürün ekleme

productList = [
    {"name": "Samsung S6","price": 3000, "description": "iyi telefon"},
    {"name": "Samsung S7","price": 4000, "categories": ['telefon', 'elektronik']},
    {"name": "Samsung S8","price": 5000},
    {"name": "Samsung S9","price": 6000},
    {"name": "Samsung S10","price": 7000},
    {"name": "Samsung S11","price": 8000}
]

result =mycollection.insert_many(productList)
print(result.inserted_ids)

