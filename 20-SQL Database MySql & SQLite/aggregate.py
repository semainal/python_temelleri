import mysql.connector
from mysql.connector import connection

#insert.py da daha önce hazırladığımız fonksiyonlar
# insertProduct & insertProducts

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products1(name,price,imageURL,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products1(name,price,imageURL,description) VALUES (%s,%s,%s,%s) " 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products1 Order By name, price") # önce name e göre sıralar sonra, kendi içinde fiyat sıralaması yapar. 
    
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(f" id= {product[0]} name: {product[1]} price {product[2]}")

    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


    

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    sql = "SELECT * FROM products1 WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")


def getProductInfo():
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) FROM Products1" #(*) Kaç kayıt var.
    # sql = "SELECT COUNT(*) FROM Products1 WHERE  price > 2000" #2000 den büyük kaç kayıt var
    # sql = "SELECT COUNT(name) FROM Products1" # (*) demeyip name parametresini de versem aynı sonucu alırım.
    # sql = "SELECT AVG(price) FROM Products1" # ortalama
    # sql = "SELECT AVG(price) FROM Products1 WHERE name LIKE '%Samsung%'"
    # sql = "SELECT SUM(Price) FROM Products1" # toplam değer
    # sql = "SELECT MAX(price) FROM Products1"
    # sql = "SELECT MIN(price) FROM Products1"
    # sql = "SELECT name FROM Products1 WHERE price = (SELECT MAX(price) FROM Products1)" # en yüksek fiyatlı telefonun adı gelir.
    sql = "SELECT name,price FROM Products1 WHERE price = (SELECT MAX(price) FROM Products1)"

    
    cursor.execute(sql)

    result = cursor.fetchone()

    # print(f"result: {result[0]}")
    print(f"result: {result[0]} {result[1]}")

getProductInfo()