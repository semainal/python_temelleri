x = 6
hak = 5
devam = "e"

#and 

# True, True => True
# True, False => False

# result = (x >5) and (x < 10 )
# result = (hak > 0) and (devam == "e")
# print(result)

#or
#True, False => True

# result =(x > 0) or (x % 2 == 0)
# print(result)

#not
#değeri tam tersine çeviriyor.

# result = not(x > 0)
# print(result)

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x > 5) and (x < 10) and (x %2 == 0))
print(result)