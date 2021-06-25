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

    # sql = "SELECT * FROM products1 "
    # sql = "SELECT * FROM categories "
    # sql = "select * from products1 inner join categories on categories.id= products1.categoryid"
    # sql = "select products1.name, products1.price, categories.name from products1 inner join categories on categories.id = products1.categoryid"
    # sql = "select products1.name, products1.price, categories.name from products1 inner join categories on categories.id = products1.categoryid where categories.name = 'Telefon'"
    # sql = "select products1.name, products1.price, categories.name from products1 inner join categories on categories.id = products1.categoryid where products1.name = 'Samsung S6'"
    sql = "select p.name, p.price, c.name from products1 as p inner join categories as c on c.id = p.categoryid where p.name = 'Samsung S6'"


    cursor.execute(sql)
    
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(product)

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

getProducts()