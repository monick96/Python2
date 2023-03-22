#dictionary comprehensions
'''
#clasic form
dict ={}
for el in range(1,6):
  dict[el] =el * 2

print(dict)

#comprehensions form
dict_v2 = {el: el * 2 for el in range(1,6)}
print(dict_v2)

'''
'''
#dict a partir de una lista
import random
countries = ['arg','mex','bol','ven']
population = {}
for country in countries:
  population[country] = random.randint(200,500)
print(population)

#dict a partir de una lista comprehencions
population_v2 = {country: random.randint(200,500) for country in countries}

print(population_v2)
'''

#dict a partir de dos lista
names = ['juani','rose','daian','brian']
ages = [22,25,26,21]

datos = list(zip(names,ages))#zip une dos listas, list convierte en lista
print(datos)#lista de tuplas

new_dict = {name: age for (name,age) in datos}
print(new_dict)

#other way
new_dict2 = {names[i]:ages[i] for i in range(len(ages))}
print(new_dict2) 
#other way
new_dict3=dict(zip(names,ages))
print(new_dict3)