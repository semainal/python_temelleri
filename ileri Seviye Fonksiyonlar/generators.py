# def cube():
#     for i in range(10):
#         yield i **3

# iterator = cube()

# for i in iterator:
#     print(i)


generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)