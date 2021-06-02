x, y ,z = 2, 5, 107

numbers = 1, 5, 7, 10, 6


#1Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# a = float(input("sayi1: "))
# b = float(input("sayi2: "))

# print(a*b-(x+y+z))


#2 y'nin x'e kalansız bölünü hesaplayınız.

# y//=x
# print(y)


#3 (x+y+z) toplamının mod 3ü nedir?

# print((x+y+z)%3)

#4 y'nin x. kuvvetini hesaplayınız.

# y = y**x
# print(y)

#5 x, *y,z = numbers işlemine göre z'nin küpü kaçtır?

# x, *y,z = numbers
# print(x,y,z)
# print(z**3)

#6 x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

x, *y, z= numbers
print(x,y,z)
print(y[0]+y[1]+y[2])

