names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

#1 "Cenk" ismini listenin sonuna ekleyeniz.

names.append("Cenk")

#2 "Sena" değerini listenin başına ekleyiniz.

names.insert(0,"Sena")

#3-4 "Deniz" isminin index nosu ve listeden siliniz. index=4

# names.remove("Deniz")
# index = names.index("Deniz")
# print(index)

#5 "Ali" listenin bir elemanı mıdır?

# result = "Ali" in names
# result = names.index("Ali") - -1 den büyük bir değer getiriyorsa liste içindeki index nosunu verir.
#6 Liste elemanlarını ters çevirin.


names.reverse()


#7 Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()

#8 years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
years.reverse()



#9 str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.

# cars = "Chevrolet", "Dacia"
# cars = cars.split(",")
# print(cars)

#10 years dizisinin en büyük ve en küçük elemanı nedir?

# print(min(years))
# print(max(years))

#11 years dizisinde kaç tane 1998 değeri vardır?

# print(years.count(1998))

#12 years dizisinin tüm elemanlarını siliniz.

years.clear()

#13 Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# cars.append(["Ford","Mercedes","BMW"])
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)


# print(names)
# print(years)
# print(cars)
# print(result)