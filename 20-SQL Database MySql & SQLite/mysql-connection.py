from os import PathLike
import mysql.connector

# database ile bağlantı kuruyoruz.

mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "Sema_tolga85",
    # database = "mydatabase"
    database = "node-app"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE DATABASE mydatabase") # boş bir database oluşturacak


# mycursor.execute("SHOW DATABASES") # for döngüsüyle ide içindeki database klasörlerimi görüntüleyebilirim.
# for x in mycursor:
#     print(x)