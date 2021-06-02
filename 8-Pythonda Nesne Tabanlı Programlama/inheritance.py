# Inheritance (Kalıtım): Miras alma

#Person => name, lastname, age, eat(), run(), drink()

#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I'm a person")

    def eat(self):
        print("I'm eating")

class Student(Person):
    def __init__(self,fname,lname, number):
        Person.__init__(self,fname, lname)
        self.studentNumber = number
        print("Student Created")

    def who_am_i(self):
        print("I'm a Student") # init metodunu kullanmadığım için Person classını ezdi!! (override) deniyor.

    def sayHello(self):
        print("Hello, I'm a student.")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        Person.__init__(self,fname,lname)
        # super().__init__(fname,lname) - alternatif yazılışı
        self.teacherBranch = branch
        print("Teacher created")

    def who_am_i(self):
        print(f"I'm a {self.teacherBranch} teacher")

p1 = Person("Sema", "İnal")
s1 = Student("Melis","İnal", "523")
t1 = Teacher("Tolga", "İnal", "Math")

print(p1.firstName + " " +p1.lastName)
print(s1.firstName + " " +s1.lastName + " "+ s1.studentNumber)
print(t1.firstName+" "+t1.lastName+" "+ t1.teacherBranch)

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()