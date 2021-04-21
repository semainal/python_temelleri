# def sayHello(name = "user"):
#   print("Hello " + name)

# sayHello("Sema")
# sayHello("Melis")
# sayHello()

# def sayHello(name = "user"):
#   return "Hello "+ name 


# msg = sayHello("Sema")
# print(msg)

# def total(num1, num2):
#  return num1 + num2

# result = total (10,20)
# print(result)


def yasHesapla(dogumYili):
 return 2020 - dogumYili

ageSema = yasHesapla(1985)
ageMelis = yasHesapla(2015)

print(ageSema, ageMelis)


def EmekliligeKacYilKaldi (dogumYili, isim):

   '''
   DOCSTRING: Doğum yılınıza göre emekliliğe kaç yıl kaldı?
   INPUT: Doğum yılı
   OUTPUT: Hesaplanan doğum yılı
   '''

  yas = yasHesapla(dogumYili)
  emeklilik = 65-yas

 if emeklilik > 0:
  print(f"Emekliliğinize {emeklilik} yıl kaldı.")
 else:
  print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1955,"Ali")

print(help(EmekliligeKacYilKaldi))
