def sum_range(min,max):
  print(f"El rango ingresado es {min} y {max}")
  sum = 0
  for x in range(min,max):
    sum += x
  return sum

result1 = sum_range(1,12)
result2= sum_range(5,12)
result3 = sum_range(result2,12+50)

print(result1, result2, result3)
