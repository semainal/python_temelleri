numbers = [1, 3, 6, 10, 50, -9, 1]
letters = ["a", "s", "y", "b", "g", "a", "s"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)
val = numbers[3:6]

numbers[3] = 20

# numbers.append(49) - serinin sonuna ekler
# numbers.append(59)
# numbers.insert(3, 63) - 3.index numrasının önüne ekler.
# numbers.insert(-1,88) - son sayının önüne ekler

# numbers.pop() - son sayıyı siler
# numbers.pop(3) - 3.indexi siler

# numbers.remove(50) - silmek istediğin sayıyı veriyorsun.


# numbers.sort() 
# # letters.sort()
# numbers.reverse() 

# print(numbers.count(1)) - liste içinde kaç tane o sayıdan var.
numbers.clear()
print(numbers)
