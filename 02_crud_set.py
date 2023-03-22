'''
Funciones de set:

*add(): Añade un elemento.

*update(): Añade cualquier tipo de objeto iterable 
 como: listas, tuplas.

*discard(): Elimina un elemento y si ya existe no 
 lanza ningún error.

*remove(): Elimina un elemento y si este no existe 
 lanza el error “keyError”.

*pop(): Nos devuelve un elemento aleatorio y lo 
 elimina y si el conjunto está vacío lanza el error 
 “key error”.

*clear(): Elimina todo el contenido del conjunto.
'''


#create
set_countries = {'col','mex','arg','bol', 'bol'}

print(set_countries)
print(type(set_countries))

size = len(set_countries) #no cuenta lo duplicado
print(size)

print('col' in set_countries)
print('nor' in set_countries)

#add
set_countries.add('nor')
print(set_countries)

set_countries.add('nor')
print(set_countries)

#update
set_countries.update({'urug', 'pe','venz', 'arg'})
print(set_countries)

#remove
set_countries.remove('pe') #si el elemento no esta en el set da error
print(set_countries)

set_countries.discard('ar') #alternativa a remove que no da error si el elemento no se encuentra
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))


