# website = "http://www.sadikturan.com"
# course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# # result = len(course)
# # result = website[7:10]
# # result = website[22:25]
# # result = course[:15]
# # result = course[-15:]
# # result = course[::-1]

# # name = "Bora"
# # surname = "Yılmaz"
# # age = 32
# # job = "mühendis"

# # print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

# # message = "Hello world"
# # result = message.replace("w","W")

# # alphabet = "abc"
# # result = alphabet*3

# # message = " Hello World "

# # print(message.strip())
# # print(message)

# # result = "www.sadikturan.com".strip("w.com")

# # result = course.lower()
# result = website.startswith("www")
# result = website.endswith("com")
# result = website.find("com")

# result = course.isalpha()
# result = course.isdigit()
# message = "Contents"
# # print(message.center(50,"*"))
# # result = website.count("a")


# # result = course.split()
# # result = course.replace(" ","-")

# message = "Hello World"
# result = message.replace("World","There")

# result = course.split()

# cars = ["BMW", "Mercedes", "Opel", "Mazda"]

# cars[3] = "Toyota"

# # result = "Mercedes" in cars

# cars[2] = "Toyota"
# cars[3] = "Renault"

# newcars = ["Audi", "Nissan"]
# result = cars + newcars

# result.pop()



# print(result[::-1])


# studentA = ["Yiğit", "Bilgi", "2010", ["70", "60", "70"]]
# studentB = ["Sena", "Turan", "1999", ["80", "80", "70"]]
# studentC = ["Ahmet", "Turan", "1998", ["80","70","90"]]

# result = studentA + studentB + studentC
# print(result)

# names = ["Ali", "Yağmur", "Hakan", "Deniz"]
# years = [1998, 2000, 1998, 1987]

# # names.append("Cenk")
# # names.insert(0,"Sena")
# # # names.remove("Deniz")
# # names.sort()
# # years.sort()
# # print(names)
# # print(years)


# print(min(years))
# print(max(years))
# print(years.count(1998))
# print(years.clear())

# markalar = []

# marka = input("marka1: ")
# markalar.append(marka)

# marka = input("marka2: ")
# markalar.append(marka)

# marka = input("marka3: ")
# markalar.append(marka)



# print(markalar)


ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }


# ogrenciler = {}

# number = input("Öğrenci no: ")
# name = input("Öğrenci adı: ")
# surname = input("Öğrenci Soyadı: ")
# phone = input("Telefon: ")

# ogrenciler.update(
# {number: {
# "ad" : name,
# "soyad" : surname,
# "telefon " : phone} 
# })


# ogrNo = input("Öğrenci No: ")
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)

# print(f"Aradığınız {ogrNo} numaralı öğrenci {ogrenci["ad"]} {ogrenci["soyad"]}, telefon numarası: {ogrenci["telefon"]}.")

# x, y, z = 2, 5, 10

# a = int(input("sayı1: "))
# b = int(input("sayı2: "))

# result = ((a*b)-(x+y+z))


# numbers = 1, 5, 7, 10, 6
# x, *y, z = numbers
# result = y[0]+y[1]+y[2]
# print(result)


# a = input("sayı1: ")
# b = input("sayı2: ")

# result = a > b

# print(f"Girdiğiniz iki sayıdan {a} ve {b}, büyük olan {b} mıdır? {result}")


vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))

ortalama = ((vize1 + vize2) / 2) * 0.60 + (final * 0.40)

print(f"Ortalamanız: {ortalama}. Dersten geçme durumunuz: {ortalama >= 50}")