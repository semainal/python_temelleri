# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.write("Deneme\n")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read(27))
#     # print(file.tell())
#     file.seek(0)
#     content = "İyi Geceler"
#     print(content)
#     content2= file.read()
#     print(content2)


# ****** sayfa sonunda güncelleme

# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nSizi Seviyorum")

# with open("newfile.txt","r", encoding="utf-8") as file:
#     print(file.read())

# ***** sayfa başında güncelleme

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Merhaba\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


#******* sayfa ortasına güncelleme




with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Seni Seviyorum\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())