def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'


result = find_volume(width=10)  #tupla

result1, width, text = find_volume(width=10)

print(result)
print(result1)
print(width)
print(text)
