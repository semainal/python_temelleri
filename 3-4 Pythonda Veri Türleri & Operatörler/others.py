# Identity Operator - is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y)
print(x==z)

print( x is y)
print(x is z)
print(x is not z)

#Membership Operator - in

x = ["apple", "banana"]
print("apple" in x)

name = "Sema"
print("a" in name)
print("a" not in name)