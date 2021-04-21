# def square(num): return num ** 2

# numbers = [1,3,5,7,9]

# result = list(map(square, numbers))

# print(result)


# numbers = [1,3,5,7,9]

# result = list(map(lambda num: num ** 3, numbers))

# print(result)




# square = lambda num: num ** 2

# numbers = [1,3,5,7,9]

# result = list(map(square,numbers))
# print(result)


numbers = [1,2,3,4,5,6,7,8,9,10]

def check_even(num): return num %2 == 0

# result = list(filter(check_even, numbers))

result = list(filter(lambda num: num %2 == 0, numbers))
print(result)