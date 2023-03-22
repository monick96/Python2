#Higher order function: una función dentro de otra función
'''
Una función de Orden Superior o en sus siglas HOF se le lama así solo cuando contiene otras funciones como parámetro de entrada o devuelve una función como salida, es decir que en este caso las funciones que operan a otras funciones se les denomina Higher order function.

También hay que entender que a estas Funciones de Orden Superior HOF se aplican para funciones y métodos que toman como funciones a los parámetros o devuelven una función como un resultado.

Propiedades de HOF
  *Una función es una instancia de tipo objeto.
  *Puede almacenar una función en una variable.
  *Puede pasar una función como un parámetro a otra      función.
  *Puede devolver la función desde una función.
  *Se puede almacenar en una estructura de datos como 
  tablas, listas, etc.
'''

def increment(x):
  return x + 1

def hof(x, func):
  return x + func(x)
  
result = hof(2,increment)
#2 + (2 + 1)
print(result)

#HOF con lambda
increment2 = lambda x : x + 1

hof2 = lambda x,func : x + func(x)

result2 = hof2(2,increment2)
#2 + (2 + 1)
print(result2)

result2 = hof2(2,lambda x : x + 2)
#2 + (2 + 2)
print(result2)

result2 = hof2(2,lambda x : x * 3)
#2 + (2 * 3)
print(result2)

