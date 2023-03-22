'''
Sets
*Se pueden modificar
*No tienen un orden
*No pueden tener elementos duplicados
*no es diccionario, no tiene par clave valor
'''
set_countries = {'col','mex','arg','bol'}
print(set_countries)
print(type(set_countries))

set_nums = {2, 5, 6, 9, 11, 15, 2}
print(set_nums)

set_types = {True, 'focus', 4, 5.25}
print(set_types)

set_from_string = set('Python')
print(set_from_string)

set_from_tuple = set (('abc','cde','fgg','fg'))
print(set_from_tuple)

list_num = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8]
set_num1 = set(list_num)
print(set_num1)
#convierte el set en lista
unique_nums = list(set_num1)
print(unique_nums)

