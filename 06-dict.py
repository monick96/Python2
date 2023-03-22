#dict a partir de una lista comprehencions
import random

countries = ['arg', 'mex', 'bol', 'ven']
population_v2 = {country: random.randint(200, 500) for country in countries}
print(population_v2)
print(population_v2.items())

result = {
  country: population
  for (country, population) in population_v2.items() if population > 250
}
print(result)

text = 'Hi! i am Moni'
#diccionario con las vocales
unique = {v: v.upper() for v in text if v in "aeiou"}
print(unique)

many = {v: text.count(v) for v in text if v in "aeiouAEIOU" }
print(many)
