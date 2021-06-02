website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40saat)"

# 1 -"course" karakter dizisinde kaç karakter bulunmaktadır. (cevap:64)

# print(len(course))

# 2 -"website" içinden www karakterini alın. (alındı)

# print(website[7:10])

# 3 - "website içinden com karakterlerini alın." (alındı)

# length = len(website)
# print(website[length-3:length])

#4 "couse" içinden ilk 15 ve son 15 karakterleri alın. (alındı)

# result = course[0:15]
# print(result)
# result = course[-15:]
# print(result)

# 5- "course" ifadesindeki karakterleri tersten yazdırın.

# print(course[::-1])

#name, surname , age , job = "Bora, Yılmaz, 32, mühanedis"

#6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırınız.(yazıldı)
#'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis'

# name = "Bora"
# surname = "Yılmaz"
# age = 32
# job = "mühendis"

# print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

# 7 -"Hello world" ifadesindeki w harfini "W" ile değiştirin. (değiştirildi)

# s = "Hello world"
# s = s[0:6] + "W"+s[-4:]
# s.replace("w","W")
# print(s)


# 8 -"abc" ifadesini yan yana 3 defa yazdırın. (yazıldı)

result = "abc" * 3
print(result)

result = "abc " * 3
print(result)



