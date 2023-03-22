#Reto: map con inmutabilidad
products = [
  {
    'product' : 'camisa',
    'price': 100
  },
  {
    'product' : 'pantalones',
    'price': 300
  },
  {
    'product' : 'shorts',
    'price': 180
  }
]

prices = list(map(lambda item: item['price'], products))

print(prices)
print(products)

#agregaremos el atributo impuesto a products con una funcion y map
#como evitar que se modifique nuestro dic original
def add_tax(el):
  new_el = el.copy()
  new_el['taxes'] = new_el['price'] * .19
  return new_el


new_products = map(add_tax,products)
#new_products = map (add_tax, products)

new_products = list(new_products)

print('New list ')
print(new_products)
print(' ')
print('Old list ')
print(products)