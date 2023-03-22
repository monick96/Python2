'''
PRUEBA & ERROR
Cuando se nos presenta un error o una excepción como se le llama en python, el programa se detiene y presenta el error que se presento, pero si utilizamos la excepción try() podemos omitir ese error y continuar con el programa. Esto es de uso fundamental para que el programa no continue con su ejecución por el error y así evitar retrasos en la producción, también de su uso para determinar en los bloques de código si se nos presenta un error poder ser identificado de manera mas facil.

Para qué try sea efectivo podemos utilizar estas declaraciones:

Exception	          Description
try	                Permite probar un bloque de código en búsqueda 
                    de un error.
except	            Permite manejar el tipo de error en el bloque.
else	              Permite ejecutar el código cuando no hay 
                    ningún tipo de error en el bloque.
finally	            Permite ejecutar el código en el bloque, 
                    independiente en el resultado de los bloques 
                    de prueba y excepción

'''

try:
 print(0/0 )
 assert 1 !=1, 'Uno no es igual a uno'
 age = 15
 if age < 18:
  raise Exception('No se perminten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)  
except Exception as error:
  print(error)
print('hola')