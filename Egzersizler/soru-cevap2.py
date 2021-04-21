# import math

# result = pow(5,3)
# print(result)


# def ayni_mi(yazi):
#     if yazi == "selam":
#         return True
#     elif yazi == "SELAM":
#         return True
#     else:
#         return False

# print(ayni_mi("Selam"))


# sayi = int(input("sayı: "))

# def tamBolen(sayi):
#     bolenler = []
#     for i in range(1, sayi+1):
#         if sayi %i == 0:
#             bolenler.append(i)
#     return bolenler

# print(tamBolen(sayi))

    # tavuk = int(input("tavuk: "))
    # inek = int(input("inek: "))
    # koyun = int(input("koyun: "))


    # def ayak(tavuk,inek,koyun):
    #     tavukayak = tavuk *2
    #     inekayak = inek *4
    #     koyunayak = koyun *4

    #     toplam = tavukayak + inekayak + koyunayak
    #     return toplam

    # print(ayak(tavuk, inek, koyun))


# arkadas = ["ahmet","ali","vural","fatih","emre"]
# arkadas2= ["fatih","vural","ali","emre","ahmet"]
# arkadas3 = ["ali","vural","emre","fatih","ahmet"]


# def yanYana(arkadas):
#     if arkadas.index("fatih")-1 == arkadas.index("vural"):
#         return True
#     elif arkadas.index("vural")-1 == arkadas.index("fatih"):
#         return True
#     else:
#         return False

# print(yanYana(arkadas3))
            

# cumle = input("cümle girin: ")

# def sesli_kaldir(cumle):
#     sesliharfler = ("aeıioöuüAEIİOÖUÜ")
#     yeni = ""

#     for i in cumle:
#         if i not in sesliharfler:
#             yeni += i
#     return yeni

# print(sesli_kaldir(cumle))
            

# tarih = int(input("tarih: "))

# def yuzyil(yil):
    
#     n = yil //100

#     if tarih %100 > 0:
#         n += 1
#         return f"{n}. yüzyıl"
#     elif tarih %100 == 0:
#         return f"{n}. yüzyıl"

# print(yuzyil(tarih))


# liste = [6,7,8,9,10]

# def index_carpma(liste):
#     toplam = 0
#     for i in range(len(liste)):
#         toplam += liste[i] * i
#     return toplam

# print(index_carpma(liste))


# yazi = input("yazi: ")
# harfler = "abcçdefgğhıijklmnoöprsştuüvyzqwx"
# rakamlar = "0123456789"

# def karakter(yazi):
#     sayilanHarf = 0
#     sayilanRakam =0
    
#     for i in yazi:
#         if i in harfler:
#             sayilanHarf += 1

#         elif i in rakamlar:
#             sayilanRakam += 1 

#     return {"Harf ": sayilanHarf, "Rakam ":sayilanRakam }

    

# print(karakter(yazi))






# def gunBulma(ay, yil):
#     gunler = {1: 31,
#         2: 28,
#         3:31,
#         4:30,
#         5:31,
#         6:30,
#         7:31,
#         8:31,
#         9:30,
#         10:31,
#         11:30,
#         12:31}

#     if ay == 2:
#         if yil %4 == 0:
#             if yil %100 == 0:
#                 if yil %400 ==0:
#                     return 29
#                 return 28
#             return 29
#         return 28
#     return gunler[ay]

# print(gunBulma(2,2015))
        



