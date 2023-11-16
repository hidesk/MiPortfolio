"""
-Se instalan NumPy, que es una biblioteca utilizada
para realizar calculos numericos y manipulacion
de matrices en Python
-En especial "numpy.random" nos proporciona funciones
para generar numeros aleatorios y muestras aleatorias
-Para instalarlo , desde la terminal y en la carpeta de trabajo
ponemos: "pip install numpy"
"""
from numpy.random import seed
from numpy.random import randint

#La semilla la definimos nosotros y nos dara valores aleatorios
#dentro de lo esperado en la semilla

semillas =1234
seed(semillas)
valor = randint(0, 11, 5)
print(valor)
  
edades = randint(5,61,10)
print(edades)

dinosaurios = randint(0,11,10)
print(dinosaurios)


