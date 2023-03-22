#reduce
'''
reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo “reduce” a un único valor. Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.
'''
import functools

nums = [1,2,3,4,5]
def accum(counter,el):
  print('counter=> ', counter)
  print('elemento=>', el)
  return counter + el

#reduce con funcion desglosada
print('reduce con funcion desglosada')
result1 = functools.reduce(accum, nums) 
print(result1)

#reduce con funcion lambda
result = functools.reduce(lambda counter, el : counter + el, nums)
print('reduce con funcion lambda')
print(result)



