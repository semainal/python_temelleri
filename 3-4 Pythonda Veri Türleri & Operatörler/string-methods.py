message = "Hello there. My name is Sema İnal"

# message = message.upper() - hepsini büyütür
# message = message.lower() - hepsini küçültür
# message = message.capitalize() - sadece ilk harfi büyütür
# message = message.title() - ilk harflerin hepsini büyütür.

# message = message.strip() - Özellikle parolalar için kullanılıyor. Baştaki boşluğu yok ediyor.
# message = message.split() - Cümleyi, boşluklarından tek tek bölüyor. print(message[]) index numarasıyla arayabilirsin.
# message = message.split(".") - Noktalardan itibaren böler.

# message = message.split() -cümleyi ayırdım, joinle her kelime arasına yıldız koydum.
# message = "*".join(message)

# index = message.find("Sema") - ilk başladığı index numarasını verir.

# isFound = message.startswith("H") - başlayan harfi
# isFound = message.endswith("o") - biten harf

# message = message.replace("Sema","Melis") - değiştirme
# message = message.replace("ç","c").replace("ö","o")

# message = message.center(100,"*") -mesajı ortalayıp, 100 karakterlik bir container oluşturuyor.*ların ortasına ortalıyor.

print(message)