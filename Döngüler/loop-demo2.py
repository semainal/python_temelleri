import random

sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istiyorsunuz?: "))
hak = can
sayac = 0


while hak > 0:
 hak-= 1
 sayac +=1
 tahmin = int(input("Tahmin: "))

 if tahmin == sayi:
  print (f"Tebrikler, {sayac}. defada Bildiniz... Puanınız {100-(100/can)*(sayac-1)}")
  break

 elif tahmin > sayi:
  print("Aşağı")

 else: 
  print("Yukarı")

 if hak == 0:
  print(f"Hakkınız Bitti.Bilemediniz.Sayı: {sayi}") 