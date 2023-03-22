import utils

data = [{
  'country': 'colombia',
  'population': 500
}, {
  'country': 'argentina',
  'population': 700
}]


def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  print(utils.a)
  
  country = input("type country=> ")
  
  result = utils.population_by_country(data, country)
  print(result)


#Entry point
if __name__ == '__main__':
  run()
