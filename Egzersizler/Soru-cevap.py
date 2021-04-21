# 1.	Taban sayısını ve üstel sayıyı alan sonrasında hesaplamayı döndüren bir fonksiyon yazın. usHesapla(5, 5) ➞ 3125

# import math

# result = pow(5,3)
# print (result)


# 2.	Girdi dizisi sadece büyük harf veya sadece küçük harf içeriyorsa True döndüren bir fonksiyon yazın. ayni_mi("SELAM") ➞ True  ayni_mi("Selam") ➞ False

# def ayni_mi(yazi):
#     if yazi == "selam":
#         return True
#     elif yazi == "SELAM":
#         return True
#     else:
#         return False


# print(ayni_mi("Selam"))

# 3.	Bir sayıyı alan ve tüm çarpanlarını listeleyen bir fonksiyon yazın. carpanlar(12) ➞ [1, 2, 3, 4, 6, 12]

# def tamBolen(sayi):
#     liste = []
#     for i in range(1, sayi+1):
#         if sayi % i ==0:
#             liste.append(i)

#     return liste

# print(tamBolen(105))

# 4.Bir çiftçi sizden tüm hayvanlarının bacak sayısını söylemeniz konusunda yardım istiyor. Çiftçide üç tür hayvan var: tavuk, inek, koyun *Sırasıyla Çiftçi hayvanlarını saydı ve size tüm türlerin alt toplamını verdi. Tüm hayvanların toplam bacak sayısını döndüren bir fonksiyonu uygulamanız gerekiyor. hayvanlar(2, 3, 5) ➞ 36
        
# def ayakSayisi(tavuk, inek, koyun):
#     tavukayak = tavuk*2
#     inekayak = inek*4
#     koyunayak = koyun*4
#     toplam = tavukayak + inekayak + koyunayak
#     return toplam

# print(ayakSayisi(3,4,5))

# 5.	Vural ve Fatih yakın arkadaşlar. Listede yan yana duruyorlarsa fonksiyon True döndürmeli. Aralarında isim varsa False döndürmeli. arkadas(["Fatih", "Vural", "Emre"]) ➞ True  arkadas(["Fatih", "Furkan", "Vural"]) ➞ False
# arkadas = ["ahmet","ali", "vural", "fatih","emre"]
# arkadas = ["vural", "emre", "ali", "fatih"]
# arkadas= ["fatih", "vural", "emre", "ali"]

# def yanYana(arkadas):
#     if arkadas.index("vural")-1 == arkadas.index("fatih"):
#         return True

#     elif arkadas.index("fatih")-1 == arkadas.index("vural"):
#         return True

#     else:
#         return False

# print(yanYana(arkadas))
        

# 6.Bir string alan ve tüm sesli harflerin çıkarıldığı yeni bir string döndüren bir fonksiyon oluşturun. sesli_kaldir("Hayatımda hiç Diyet Kola içen ince bir insan görmedim.") ➞ " Hytmd hç Dyt Kl çn nc br nsn grmdm.”

# cumle = "Hayatımda hiç Diyet Kola içen ince bir insan görmedim."

# def sesli_kaldir(cumle):
#     sesliharf = "aeıioöuüAEIİOÖUÜ"
#     yeni = ""
#     for i in cumle:
#         if i not in sesliharf:
#             yeni += i
#     return yeni

# print(sesli_kaldir(cumle))
            

# 7.Tarihi alan ve doğru yüzyıla döndüren bir fonksiyon oluşturun. yuzyil(1756) ➞ "18. yüzyıl"

# tarih = int(input("tarih: "))

# def yuzyil(yil):
#     n = yil // 100
#     if yil%100 >0:
#         n +=1
#         return f"{n}. yüzyıl"

# print(yuzyil(tarih))

#8.Her elemanın kendi indeksi ile çarpıldığı listede tüm elemanların toplamını döndürün. Boş listeler için 0 döndürün. index_carpici([1, 2, 3, 4, 5]) ➞ 40  # (1*0 + 2*1 + 3*2 + 4*3 + 5*4)
    
# sayi = [1, 2, 3, 4, 5]  

# def index(sayi):
#     toplam = 0
#     for i in range(len(sayi)):
#         toplam += sayi[i]*i
#     return toplam

# print(index(sayi))

#9.Bir stringi alan ve içindeki harf ve sayıların sayısını hesaplayan bir fonksiyon yazın. Sonuçları sözlüğe döndürün.  say("H3ll0 Wor1d") ➞ { "Harfler":  7, "Sayılar": 3 }

# cumle = input("cümle: ")
# harf = "abcçdefgğhıijklmnoöprsştuüvyzxwq"
# rakam = "0123456789"

# def harfRakam(cumle):
#     sayilanHarf = 0
#     sayilanRakam = 0

#     for karakter in cumle:
#         if karakter in harf:
#             sayilanHarf += 1
#         elif karakter in rakam:
#             sayilanRakam += 1
#     return {"Harfler": sayilanHarf, "Rakamlar": sayilanRakam}

# print(harfRakam(cumle))

#10.Ay ve günleri (tam sayı) olarak alan ve aydaki gün sayısını döndüren bir fonksiyon oluşturun. gun(2, 2018) ➞ 28

# def gun(ay, yil):
#     gunler = {1:31,
#               2:28,
#               3:31,
#               4:30,
#               5:31,
#               6:30,
#               7:31,
#               8:31,
#               9:30,
#               10:31,
#               11:30,
#               12:31}


#     if ay ==2:
#         if yil %4 ==0:
#             if yil %100==0:
#                 if yil%400==0:
#                     return 29
#                 return 28
#             return 29
#         return 28


#     return gunler[ay]

# print(gun(2,2020))
    

#11.Boşluklara göre tam sayıları ayıran ve en büyük ve en küçük tam sayıları (string olarak) döndüren bir fonksiyon yazın.  buyuk_kucuk("1 2 3 4 5") ➞ "5 1"

#BEN YAPTIM BEN YAPTIM : )))
# liste = 15,20,25,5,45

# def buyukKucuk(liste):
#     buyuk = max(liste)
#     kucuk = min(liste)
#     yeni = {"küçük": kucuk, "büyük": buyuk}
#     for i in liste:
#         if i == min(liste):
#             i+= kucuk
          
#         elif i == max(liste):
#             i += buyuk
        
#     return yeni
# print(buyukKucuk(liste))

# 12.Parametre olarak bir veya daha fazla kelimeyi alan ve beş veya daha fazla harfe sahip kelimeleri ters döndürecek şekilde döndüren bir fonksiyon yazın. String sadece harfler ve boşluklardan oluşacak. Boşluk sadece birden fazla kelime olduğunda dahil edilecek.  ters("Ters") ➞ "Ters" ters("Bu normal bir cümle.") ➞ "Bu lamron bir .elmüc" ters("Köpek büyük.") ➞ "kepöK .küyüb"


# cumle = input("cümle giriniz: ")

# def ters(cumle):
    
#     kelimeler = cumle.split()
#     yeni = ""

#     for kelime in kelimeler:
#         if len(kelime) <5:
#             yeni += kelime + " "

#         else:
#             yeni += kelime[::-1] + " "

#     return yeni.split()

# print(ters(cumle))


# 13.Stringi alan ve orta karakteri döndüren bir fonksiyon oluşturun. Eğer kelimenin uzunluğu tek ise orta karakteri dönün. Eğer kelimenin uzunluğu çift ise orta iki karaktere dönün. ortanca("test") ➞ "es" ortanca("testing") ➞ "t"

# kelime = input("kelime: ")

# def orta(kelime):
    
#     if len(kelime) % 2== 1:
#         return kelime[len(kelime)//2]

#     elif len(kelime) %2 == 0:
#         return kelime[len(kelime)//2 -1 : len(kelime)//2 +1]
    
# print(orta(kelime))
       


# 15.Oy sayısı stringini sayılar listesine dönüştüren bir fonksiyon yazın. k bini temsil eder. gercek_deger("6.8k 13.5k") ➞ [6800, 13500] Oyları liste olarak döndürün
        




    













