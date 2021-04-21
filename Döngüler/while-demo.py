# sayilar = [1,3,5,7,9,12,19,21]

#1saylar listesini while ile yazdırın.

# i = 0
# while (i < len(sayilar)):
#  print(sayilar[i])
#  i += 1

#2 Başlangıç ve bitiş değerlerini kullanıcıdan alıp, aradaki tüm tek sayıları yazdırın.

# baslangic = int(input("Başlangıç: "))
# bitis = int(input("Bitiş: "))


# i = baslangic

# while i < bitis:
#  i+=1
#  if i%2 == 1:
 
#   print(i)





#3 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100

# while i>=1:
#  print(i)
#  i -= 1
# print("Bitti..")

#4 Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# Benim yaptğım for döngüsüyle
# list = [int(input("Sayı1: ")),int(input("sayı2: ")),int(input("sayı3: ")),int(input("sayı4: ")),int(input("sayı5: "))]


# for x in list:
#  list.sort()
# print(list)

#while döngüsüyle

# numbers = []
# i = 0

# while i<5:
#  sayi = int(input("Sayı: "))
#  numbers.append(sayi)
#  i+=1
# numbers.sort() 
# print(numbers)


#5 
urunler = []

adet = int(input("Kaç ürün listelensin? :"))
i = 0

while i < adet:
 name = input("Ürün ismi: ")
 price = input("Ürün fiyatı: ")
 urunler.append ({
        "name": name,
        "price": price})
 i+= 1

for urun in urunler:
 print(urun)










