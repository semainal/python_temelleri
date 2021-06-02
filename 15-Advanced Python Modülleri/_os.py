import os
import datetime

# result = dir(os)
# result = os.name


#dizin değğiştirme
# os.chdir("C:\\")
# os.chdir("../../../..")

#klasör oluşturma
# os.makedirs("newfile")

#etkin dizin öğrenme
# result = os.getcwd()
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory") - silmek için
# os.removedirs("yeniklasör/yeniklasör") - alt dizin silmek için

#listeleme
# result = os.listdir()
# result = os.listdir("C:\\")



# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)


# result = os.stat("_datetime.py")

# result = datetime.datetime.fromtimestamp(result.st_ctime) - oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) - son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) - değiştirilme tarihi



# os.system("notepad.exe")
# print(result)


#path

result = os.path.abspath("_datetime.py")

result = os.path.dirname("C:/Users/90544/Desktop/python_temelleri/İleri Seviye Modüller & Web Scraping/_os.py")

result = os.path.dirname(os.path.abspath("_datetime.py"))

result = os.path.exists("_datetime.py")
result = os.path.exists("C:/Users/90544/Desktop/python_temelleri")

result = os.path.isdir("C:/Users/90544/Desktop/python_temelleri")
result = os.path.isfile("C:/Users/90544/Desktop/python_temelleri/İleri Seviye Modüller & Web Scraping/_os.py")

result = os.path.join("C:\\","deneme")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
result = result[0]
print(result)

