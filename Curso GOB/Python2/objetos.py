class perro:
    ladrar="Guaaaaaaauuu!!!"
    aullar="Auuuuuuuuuuu!!!"

print(perro.ladrar)
print(perro.aullar)
english_dog=perro
english_dog.ladrar="Wouf Wouf!"
print(english_dog.ladrar)

class operaciones:
    def sumar(x,y):
        suma=x+y
        return suma
    def resta(x,y):
        resta=x-y
        return resta
    def multiplicar(x,y):
        multi=x*y
        return multi
    def dividir(x,y):
        divi=x/y
        return divi
    def potencia(x,y):
        pote=x**y
        return pote
print(operaciones.sumar(5,5))

class persona:
    saludar="Hola"
    despedida="Adios"

print(persona.saludar)

import random as rd
aleatorio=rd.random()

from datetime import date as dt
fecha=dt.today()

print(aleatorio,fecha)




