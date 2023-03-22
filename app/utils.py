'''
def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

  a = 'hola'
'''




def get_population(key_list, dict):
  values = [int(dict[key]) for key in key_list if key in dict]
  return values


def get_col(data, col):
  result = [el[col] for el in data]
  #result = list(result)
  return result
  
  


