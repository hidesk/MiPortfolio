"""
La moda mide cual es el numero mas repetido
dentro de un conjunto de datos
"""
#El programa decia que se importaba de esta ,manera
# from statistics as st
#pero generaba error asi que se cambio al siguiente:

import statistics as st

edades=[10,10,2,5,7]
estadistica=st.mode(edades)
print(estadistica)

"""La mediana es una media que señala cual valor corta el 50%
de los datos
 """
 #Quantile vera la mediana de los datos y es 0.5
 #lo podemos modificar para obtener cualquier 
 #quantil de corte
from numpy import quantile

numeros = list(range(1,8))
print(numeros)

media=quantile(numeros,0.5)
print(media)

numeros= [2,4,6,8,10,1,3,5,7,9]
media=quantile(numeros,0.5)
print(media)

#Ejemplo de quantil de corte diferente
numeros=[11,2,4,6,8,10,1,3,7,9,11,12]
media=quantile(numeros,0.25,interpolation="midpoint")
print(media)
#Especificamos el parametro interpolation y lo fijamos al
#midpoint para usar el punto medio
#se puede cambiar por lower,higher,nearest o linear

"""El promedio es uno de los estadisticos mas comunes
e intenta capturar el centro de los datos pero distinto
de la mediana y la moda, considera el total de los datos
disponiles, sumandolos, y dividiendolos por la cantidad
de datos disponibles"""
#mean significa promedi en ingles
from numpy import mean
numeros =[15,16,16,17,17,18,19,19,20,21]
promedio=mean(numeros)
print(promedio)

computador_por_persona =[2,0]
cant=mean(computador_por_persona)
print(cant)

"""Desviacion estandar es la medida adicional que considera
la concentracion o dispersion,"""
#std es un acronimo de standard deviation
from numpy import std
desviacion =std(computador_por_persona)
print(desviacion)