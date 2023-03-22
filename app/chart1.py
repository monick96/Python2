import rcsv
import utils
import matplotlib.pyplot as plt
import charts


keys = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']

header = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
#header = int(header)
header = header[::-1]

def run():
  data = rcsv.read_csv('./app/data.csv')
  #obtengo la lista con el diccionario
  country = input('Type Country =>')
  country = country.capitalize()
  country_list = utils.population_by_country(data,country)
  #obtengo el diccionario
  country_dict = country_list[0]
  
  #obtengo la poblacion
  values = utils.get_population(keys, country_dict)
  values = values[::-1]

  

  #uno los años con los valores 
  datos = list(zip(header,values))

  #convierto en dict
  population_by_year = {year:hab for (year,hab) in datos}
  print(country_list)
  print(country_dict)
  print('*' * 20)
  print(values)
  print('*' * 20)
  print(datos)
  print('*' * 20)
  print(population_by_year)

  charts.generate_bar_chart(header,values)
  

if __name__ == '__main__':
  run()
  
  
 
  

  
