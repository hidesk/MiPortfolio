"""Ley de los Grandes Numeros
    Es el razonamiento suyaciente detras de todo buen dato
    Probabilidad teorica
    Probabilidad Empirica
"""
from numpy.random import seed
from numpy.random import randint

seed(1234)

lanzamientos=randint(0,2,1000000)
suma=(sum(lanzamientos)/1000000)
print(suma)

valor=sum(randint(1,7,100)==6)/100
print(valor)

eventos=[]
for i in range(1,1000000):
    eventos.append(sum(randint(0,2,10))/10)
print(eventos)
eventos[1:10]
mean(eventos)
print(eventos)