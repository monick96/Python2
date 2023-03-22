#map()
'''
La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.

Sintaxis.
map(function, iterables)

'''
numbers = [1, 2, 3, 4, 5]
numbers2 = []
for i in numbers:
  numbers2.append(i * 2)

#map() + lambda
#map(function, iterables)
numbers3 = map(lambda i: i * 2, numbers)
numbers3 = list(numbers3)
  
print(numbers)
print(numbers2)
print(numbers3)

numbers1 = [1, 2, 3, 4, 5]
numbers5 = [6, 7, 8, 9]

print(numbers1)
print(numbers5)

result = list(map(lambda x,y: x + y, numbers1, numbers5))

print(result)


