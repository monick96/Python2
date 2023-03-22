price= 100 #global

def increment():
  price= 100 #local
  result = price + 10
  return result

print(increment())

print(price)

#print(result) #solo vive en la funcion increment()


