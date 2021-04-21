from os import read


# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)

# file.close()


with open("newfile.txt", "r", encoding="utf-8") as file :
    content= file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)