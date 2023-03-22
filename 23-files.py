file = open('./text.txt')
 
#lee todas las lineas de una vez
print(file.read())
 


#lee de auna linea en caso de que el archivo sea muy grande y no lo necesitamos todo
'''
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''


#debemos cerrar el archivo de texto cuando ya no necesitemos leerlo debido a que ocupa mucha memoria en python
file.close()


#instruccion para abrir el file y una vez se terminan las instrucciones del programa se cierra automaticamente
with open('./text.txt') as file:
  
  for line in file: #usar un for no ocpa tanta memoria, sirve                          cuando no sabemos cuantas lineas tine
    print(line)
