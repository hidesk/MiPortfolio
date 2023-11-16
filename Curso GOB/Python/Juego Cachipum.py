"""
Se crea una funcion para que la maquina devuelva
un valor aleatorio y asignamos una palabra al 
return, asi tenemos definida la funcion
"""
#Se importa la funcion random para generar una 
#respuesta aleatoria

import random as rd

def maquina():
    jugada=rd.randrange(0,3)
    if jugada ==0:
        return "Piedra"
    if jugada ==1:
        return "Papel"
    if jugada ==2:
        return "Tijera"
    
python=maquina()

def persona():
    jugada2=int(input("Que elegiras? :\nPiedra  -1\nPapel   -2\nTijera  -3\nElige tu arma   : "))
    if jugada2 ==1:
        return "Piedra"
    if jugada2 ==2:
        return "Papel"
    if jugada2 ==3:
        return "Tijera"

def match(persona):
    jugada=persona
    python=maquina()
    print("Python jugo: "+python)
    print("Usuario jugo: "+jugada)
    if jugada == python:
        return 0
    if jugada == "Piedra" and python == "Papel":
        return -1
    if jugada == "Piedra" and python == "Tijera":
        return 1
    if jugada == "Papel" and python == "Piedra":
        return 1
    if jugada == "Papel" and python == "Tijera":
        return -1
    if jugada == "Tijera" and python == "Piedra":
        return -1
    if jugada == "Tijera" and python == "Papel":
        return 1

def listaResultados(resultado):
    for i in range (0,3):
        lista=[]
        lista.append(resultado)
    return lista


persona=persona()

resultado=match(persona)
resultados=listaResultados(resultado)
print(resultados)
