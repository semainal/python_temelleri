# try:
#     file = open("newfile.txt","r")
#     print(file)

# except FileNotFoundError:
#     print("dosya okuma hatası")

# finally:
#     print("dosya kapandı.")
#     file.close()


from typing import ContextManager


file = open("newfile.txt", "r", encoding="utf-8")

# for i in file:
#     print(i, end="")


# content = file.read()
# print(content)


# content1 = file.read()
# print("içerik 1")
# print(content1)

# content2 = file.read()
# print("içerik 2")
# print(content2)


# readline fonksiyonu


# print(file.readline(),end=(""))
# print(file.readline(),end=(""))
# print(file.readline())
# print(file.readline())


#readlines() fonksiyonu

liste = file.readlines()
print(liste)
file.close()