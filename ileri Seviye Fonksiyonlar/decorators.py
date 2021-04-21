# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan önceki işlemler")
#         func()
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello():
#     print("Hello")

# sayHello()


# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("Sema")




import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,**kwargs) 

        finish = time.time()
        print("Fonksiyon " + func.__name__ +" "+ str(finish-start)+ " saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

    
@calculate_time
def fonksiyon(num):
    print(math.factorial(num))


usalma(5,3)
fonksiyon(5)
    

