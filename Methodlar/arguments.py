# def change(n):
#  n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# change(sehirler)
# print(sehirler)


# def change(n):
#  n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# change(sehirler[:])
# print(sehirler)


def add(a,b,c = 0):
 return sum((a,b))

print(add(10,20))


def displayUser(**args):
  for key, value in args.items():
   print("{} is {}".format(key,value))

displayUser(name="Sema", age=35, city="istanbul")
displayUser(name="Melis",age=5, city="izmir", phone=123456)
displayUser(name="Tolga", age= 20, city="ankara", phone=123456, email="tolga@gmail.com")


def myFunc (a,b, *args, **kwargs):
 print(a)
 print(b)
 print(args)
 print(kwargs)

myFunc(10,20,30,40,50, key1="Value 1", key2="Value 2", )