# numbers = []

# for x in range(10):
#  numbers.append(x)
# print (numbers)

# #alttaki daha kolay, tek satır
# numbers = [x for x in range(10)]
# print(numbers)

# numbers = [x**2 for x in range(10)]
# print(numbers)

# numbers = [x*x for x in range(10) if x%3 == 0]
# print(numbers)


# myString = "Hello"
# # myList = []

# # for letter in myString:
# #  myList.append(letter)
# # print(myList)

# # myString = [myString for letter in myList ]
# # print(myList)

# myList = [letter for letter in myString]
# print(myList)

# years = [2000, 1960, 1958, 1936, 1985]
# ages = [2020-year for year in years]
# print(ages)

# results = [x if x%2 == 0 else "Tek" for x in range(1,10) ]
# print(results)

result = []

for x in range(5):
 for y in range(3):
  result.append((x,y))
print(result)