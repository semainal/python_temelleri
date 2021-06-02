import numpy as np

# 1- (10,15,30,45,60) değerine sahip numpy dizisi oluşturunuz.

result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

result = np.arange(5,16)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

result = np.arange(50,105,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

result = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

result = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

result = np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tam sayı üretin.

result = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.

result = np.random.randn(10)

# 9 - (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

result = np.random.randint(10,50,15).reshape(3,5)
# 10- Üretilen matrisin satır ve sütun sayılarının toplamlarını hesaplayınız.

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = numbers.sum(axis = 1)
# result = numbers.sum(axis = 0)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması kaçtır?

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = np.max(numbers)
# result = np.min(numbers)
# result = np.average(numbers)

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır?

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = np.argmax(numbers)


# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

# numbers = np.arange(10,20)
# result = numbers[:3]

# 14- Üretilen dizinin elemanlrını tersten yazdırın.

numbers = np.arange(10,20)
result = numbers[::-1]

# 15- Üretilen matrisin ilk satırını seçiniz.

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = numbers[0]


# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir?

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = numbers[1,2]

# 17- Üretilen matrisin tüm satırlarındaki ilk elemanı seçiniz.

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = numbers[:,0]

# 18- Üretilen matrisin her bir elemanının karesini alınız.

# numbers = np.random.randint(10,50,15).reshape(3,5)
# print(numbers)
# result = numbers **2

# 19- Üretine matrisin elemanlarının hangisi pozitif çift sayıdır?
#     Aralığı (-50,+50) arasında yapınız.

numbers = np.random.randint(-50,50,15).reshape(3,5)
print(numbers)
ciftler = numbers[numbers %2 == 0]
result = ciftler[ciftler>0]



print(result)