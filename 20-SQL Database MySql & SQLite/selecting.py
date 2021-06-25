import mysql.connector

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

    # cursor.execute("SELECT * FROM products1") # * la hepsini seçiyorum tüm kolonlar
    cursor.execute("SELECT name,price FROM products1") # kullanmayacağım kolonlar gelmiyor, sadece name ve price geliyor.
    
    # result = cursor.fetchall() #1den fazla kayıt seçmek için
    result = cursor.fetchone() # bulduğu ilk kaydı bana getirecek, bütün liste gelmeyecek.
    # print(result)
    
    print(f"name: {result[0]}, price {result[1]}")
    
    # for product in result:
    #     # print(f"name: {product[1]} price: {product[2]}")
    #     print(f"name: {product[0]} price: {product[1]}")
getProducts()

