# # global scope

# x = "global scope"

# def function():
#     # local scope
#     x = "local scope"
#     print(x)

# function()
# print(x)



# name = "Sema"

# def changeName(new_name):
#     name = new_name
#     print(name)

# changeName("Tolga")
# print(name)




# name = "global string"

# def greeting():
#     # name= "Sema"
#     print("Merhaba "+ name)

#     def hello():
#         # name = "Tolga"
#         print("Hello "+ name)

#     hello()

# greeting()
# print(name)



x = 50
def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to: {x}")

test()
print(x)