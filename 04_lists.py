'''

numbers = []
#forma clasica
for el in range(1,11):
  numbers.append(el*2)
print(numbers)

#List Comprehension
numbers_v2 = [el for el in range(1,11)]
print(numbers_v2)

'''

numbers = []
#forma clasica con if
for el in range(1,11):
  if el % 2 == 0:
    numbers.append(el*2)
print(numbers)

#List Comprehension con if
numbers_v2 = [el * 2 for el in range(1,11) if el % 2 == 0]
print(numbers_v2)