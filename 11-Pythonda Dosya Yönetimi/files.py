# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi, dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"w": (write) yazma modu. => dosyayı konumda oluşturur.
# ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Sema İnal")
# # print(file)
# # file.close()
# file.close()
# #"a": (append) ekleme modu. => dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nTolga İnal")
# file.close()
#"x": (create) oluşturma modu. => dosya zaten varsa hata verir.

file = open("newfile2.txt","x",encoding="utf-8")

#"r": (read) okuma modu. => varsayılan. dosya konumda yoksa hata verir.

