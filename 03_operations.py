'''
Operaciones set

*union(set): Realiza la operacion “union” entre dos conjuntos. 
 La unión entre dos conjuntos es sumar los elementos de estos 
 sin repetir elementos. Esta operación tambien se puede 
 realizar con el signo “|”: set_a | set_b.
*intersection(set): Realiza la operacion “intersection” entre 
 dos conjuntos. La intersección entre dos conjuntos es tomar 
 unicamente los elementos en común de los conjutnos. Esta 
 operación tambien se puede realizar con el signo “&”: set_a & 
 set_b.
 
*difference(set): Realiza la operacion “difference” entre dos 
 conjuntos. La diferencia entre dos conjuntos es restar los 
 elementos del segundo conjunto al primero. Esta operación 
 tambien se puede realizar con el signo “-”: set_a - set_b.
 
*symmetric_difference(set): Realiza la operacion 
 “symmetric_difference” entre dos conjuntos. La diferencia 
 simetrica entre dos conjutnos consta de restar todos los 
 elementos de ambos exceptuando el elemento en común. Esta 
 operación tambien se puede realizar con el signo “^”: set_a ^ 
 set_b.
 
NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede únicamente entre conjuntos.
'''


set_countries_a = {'col', 'mex','bol'}
set_countries_b = {'bol', 'pe'}

print(set_countries_a)
print(set_countries_b)

#join
set_countries_c = set_countries_a.union(set_countries_b)
print(set_countries_c)
#otra forma de join
set_countries_c1 = set_countries_a | set_countries_b
print(set_countries_c1)

#intersection entre un set y otro /elementos en comun
set_c = set_countries_a.intersection(set_countries_b)
print(set_c)
#otra forma de intersection
set_c1 = set_countries_a & set_countries_b
print(set_c1)

#difference/ saca los elementos del 1er conjunto (los que comparten con el 2do)restandole los elementos del 2do/resta de A-B/
set_d = set_countries_a.difference(set_countries_b)
print(set_d)
#otra forma de difference
set_d1 = set_countries_a - set_countries_b
print(set_d1)

#symmetric difference/union sin los elemento que comparten(sin intersection)
set_e = set_countries_a.symmetric_difference(set_countries_b)
print(set_e)
#otra forma de symmetric difference
set_e1 = set_countries_a ^ set_countries_b
print(set_e1)











