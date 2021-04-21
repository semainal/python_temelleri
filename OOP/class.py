#class

class Person:

    #1)class attributes
    address = "No information"

    #constructor (yapıcı metod)

    def __init__ (self,name,year):


        #2)object attributes
        self.name = name 
        self.year = year
        print("İnit metodu çalıştı.")

    #methods


#instance (object)

p1 = Person(name ="Sema",year =1985)
p2 = Person(name="Tolga",year=1985)

#updating
p1.name = "Melis"
p2.address = "İstanbul"

#accessing object attributes
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")

print(p1)
print(p2)