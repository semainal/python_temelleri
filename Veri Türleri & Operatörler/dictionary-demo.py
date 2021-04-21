"""ogrenciler = {
        "120": {
             "ad": "Ali",
             "soyad": "Yılmaz",
             "telefon": "532 000 00 01"},
        "125": {
        "ad": "Can",
        "soyad": "Korkmaz",
        "telefon": "532 000 00 02"},

        "128": {
        "ad": "Volkan",
        "soyad": "Yükselen",
        "telefon": "0532 000 00 03"}     
         }
"""

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")



# ogrenciler[number] = {
#      "ad": name,
#      "soyad": surname,
#      "telefon": phone
# }


ogrenciler.update({
number: {
"ad": name,
"soyad": surname,
"telefon": phone}})


print("*"*50)

ogrNo = input("Öğrenci no: ")
ogrenci = ogrenciler[number]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {name} soyadı: {surname} ve telefon numarası: {phone}" ) 



