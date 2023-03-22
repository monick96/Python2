'''
¿Que es lambda?
Son conocidas como Funciones Anónimas o lambdas, en donde no tienen un identificador o no tienen un nombre, se puede definir su estructura de la siguiente manera: lambda argumentos: expresión, las funciones lambda pueden tener los argumentos que se requieran pero solo una linea de código o una expresión.

Sintaxis
lambda arguments : expression

Queremos incrementar el valor de una serie según la cantidad que le hayamos dado para ello tenemos el siguiente ejemplo:
'''


def increment(x):
  return x + 1

result = increment(10)

print(result)

#funcion lambda
increment2 = lambda x: x + 1

result2 = increment2(20)

print(result2)

#title pone la primera letra de cada palabra en mayuscula
#y capitalize solo pone la primera letra del parrafo en mayuscula

full_name = lambda name, last_name: f'Full name is: {name.title()} {last_name.title()}'

text = full_name('monica', 'melgarejo esquivel')
print(text)
