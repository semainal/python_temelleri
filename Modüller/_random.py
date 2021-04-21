import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100
result = random.randint(1,100)
result = random.uniform(1,10)

greeting = "Hello World"
names = ["Sema","Tolga","Melis","Venüs"]

# result = names[random.randint(0,len(names)-1)]

result = random.choice(names) #yukardakinin aynısı
result = random.choice(greeting)


liste = list(range(10))

random.shuffle(liste)
result = liste



liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names,2)
print(result)