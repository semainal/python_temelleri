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

    # cursor.execute("SELECT * FROM products1 WHERE id=1") # sadece id 1 gelir.
    # cursor.execute("SELECT * FROM products1 WHERE name= 'Samsung S6'") # samsung s6 lar gelir.
    # cursor.execute("SELECT * FROM products1 WHERE name= 'Samsung S6' and Price=2500") # samsung s6 ve fiyatı 2500 olan gelir.
    # cursor.execute("SELECT * FROM products1 WHERE name= 'Samsung S6' and Price >=2500") # 2500 ve üzeri gelir.
    # cursor.execute("SELECT * FROM products1 WHERE name= 'Samsung S6' or Price =3000")
    # cursor.execute("SELECT * FROM products1 WHERE name LIKE '%Samsung%'") # içinde samsung geçen tüm ürünler
    # cursor.execute("SELECT * FROM products1 WHERE name LIKE '%Samsung%' and price >= 3000") # tüm samsungların içinden fiyatı 3000den büyük olanlar
    cursor.execute("SELECT * FROM Products1")
    
    result = cursor.fetchall()
    # print(result)

    for product in result:
        print(f" id= {product[0]} name: {product[1]} price {product[2]}")

# getProducts()

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    sql = "SELECT * FROM products1 WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

getProductById(2)
