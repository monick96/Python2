'''
r -> abre un archivo solo para lectura. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
rb -> abre un archivo solo para lectura en formato binario. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
r+ -> abre un archivo para escritura y lectura. El puntero del archivo está localizado al comienzo del archivo.
w -> abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
wb -> abre un archivo solo para escritura en formato binario. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
w+ -> abre un archivo para escritura y lectura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
a -> abre un archivo para anexo. El puntero del archivo esta al final del archivo si este existe. Es decir, el archivo está en modo anexo. Si el archivo no existe, crea un nuevo archivo para escritura

'''


#por defecto viene con permiso de read para mod agregar 'r+' o 'w+'este ultimo reescribe todo el archivo
with open('./text.txt','r+') as file:
  #usar un for no ocpa tanta memoria, sirve cuando no sabemos cuantas lineas tine
  for line in file:
    print(line)
  file.write('En vano he luchado. No quiero hacerlo más. Mis sentimientos no pueden contenerse. Permítame usted que le manifieste cuan ardientemente la admiro y la amo.\n')
