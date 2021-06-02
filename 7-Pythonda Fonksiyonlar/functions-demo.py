#1 Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def sayHello(name , adet):
#  print(name * adet)

# sayHello("Sema\n", 10)

#2 Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

# def listeyeCevir(*params):
#     liste = []
    
#     for param in params:
#         liste.append(param)
    
#     return liste 

# result = listeyeCevir(10,20,30,40,"a","b","c")
# print(result)


#3 Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#                 else:
#                     print(sayi)

# sayi1 = int(input("sayi1:"))
# sayi2 = int(input("sayi2:"))

# asalSayılariBul(sayi1,sayi2)

#4 Kendisine gönderilen bir sayının tam bölenlerini bir liste şekline döndürün.

#BEN YAPTIM :)))
# def tamBolen(sayi):
#     for i in range(1, sayi+1):
#         if  sayi % i == 0:
#             print(i)

# sayi = int(input("Sayı: "))

# tamBolen(sayi)
