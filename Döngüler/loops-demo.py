"""
1-100 arasında rastgele üretilecek bir sayıyı 
aşağı yukarı ifadeleri ile bulmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen 
can sayısı üzerinden hesaplansın.
"""

import random

sayi = random.randint(1,100)
can = int(input("İstenen hak: "))
hak = can
sayac = 0

while int(hak) > 0:
 hak-=1
 sayac += 1
 tahmin = int(input("Tahmin: "))
 

 if tahmin == sayi:
  print(f"Tebrikler {sayac}.defada bildiniz. Puanınız: {100-(100/can)*(sayac-1)}, Kalan hakkınız: {hak}" )
  break

 elif tahmin > sayi:
  print(f"Aşağı.\nPuanınız {100-(100/can)*(sayac-1)}.Kalan hakkınız: {hak}")

 else:
  print(f"Yukarı.\nPuanınız {100-(100/can)*(sayac-1)}.Kalan hakkınız: {hak}")

 if hak ==0:
  print(f"Hakkınız bitti. Tahmin edilen sayı: {sayi}, puanınız: {puan}.") 
