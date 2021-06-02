# def usalma(number):

#     def inner(power):
#         return number ** power

#     return inner

# two = usalma(2)
# three = usalma(3)

# print(two(5))
# print(three(4))


# def yetki_sorgulama(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)

#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)

#     return inner

# user1 = yetki_sorgulama("Product Page")
# print(user1("user"))



def islem(islem_adi):
    def toplam(*args):
        toplam =0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print (toplama(1,3,5,7,9))

carpim = islem("carpma")
print(carpim(3,5))