import mysql.connector
from mysql.connector import connection



def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM Products1 Order By Name")
    # cursor.execute("SELECT * FROM Products1 Order By price")
    # cursor.execute("SELECT * FROM Products1 Order By id ASC") # ASC dersen değişen bişey olmaz artan biş sekilde sıralar
    # cursor.execute("SELECT * FROM Products1 Order By id DESC") # azalan bir şekilde sıralar
    # cursor.execute("SELECT * FROM Products1 Order By price DESC")
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


def updateProduct(id, name, price):

    connection = mysql.connector.connect(host="localhost", user = "root", password= "Sema_tolga85", database="node-app")
    cursor = connection.cursor()

    # sql = "Update products1 Set name = 'Samsung S10' where id=5 " #id si 5 olan kaydı güncelledik.
    # sql = "Update products1 Set name = 'Samsung S10',price = 4000 where id=1 "
    #id, name ve price vererek yapmak için:
    #name i değiştirmek istemiyorsan: if name! ="" ifadesiyle boşluk değer gönderebilirsin.


    sql= "UPDATE products1 SET name = %s, price = %s where id= %s"
    values = (name,price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

updateProduct(1, "Iphone 8", 6000)
getProducts()


