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

#agregaremos el atributo impuesto a products con una funcion y map

def add_tax(el):
  el['taxes'] = el['price'] * .19
  return el


new_products = map(add_tax,products)
#new_products = map (add_tax, products)

new_products = list(new_products)

print(new_products)
print(' ')
print(products)

  