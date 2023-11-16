import pandas as pd
grupoA=[50,40]
grupoB=[60,70]
datos={"Grupo A": grupoA,
       "Grupo B": grupoB}
#definimos las filas con los nombres de las filas
#que queremos
nombre_filas = ["Sin recompensa","Con recompensa"]
#Luego usamos el parametro index de la funcion
#DataFrame() de la libreria pandas
tabla = pd.DataFrame(datos,
                     index=nombre_filas)
print(tabla)

#Agregamos el .sum() al print para que nos muestre la
#suma de las columnas por grupo
print(tabla.sum())

#Luego sumamos el total de cada columna y obtenemos el
#total de personas
total_personas= sum(tabla.sum())
print(total_personas)

#Para obtener el total de personas sin recompensa, indicamos
#por medio del comando .loc[] el nombre o numero de fila
#que queremos recuperar
print(tabla.loc["Sin recompensa"])

#Luego sumamos esta cantidad para obtener el total de
#personas sin recompensa
total_sin_recompensa= sum(tabla.loc["Sin recompensa"])
print(total_sin_recompensa)

#Finalmente con estos dos valores , calculamos el porcentaje
porcentaje=((total_sin_recompensa/total_personas)*100)
print(porcentaje)

#Esto nos imprime una tabla ordenada de nuestros datos 
#se crea un objeto dataframe con puntajes de 3 personas
objeto = pd.DataFrame({"Pepe": [30,10,80],
                       "Juanita": [100,90,95],
                       "Deniss": [10,10,100]},
                       index = ["Pueba 1","Prueba 2","Prueba 3"])
print(objeto)
print(objeto.sum())

#Porcentajes de personas con recompensa segun su grupo
recompensa_grupo_b = ((tabla.loc["Con recompensa","Grupo B"]/total_personas)*100)
recompensa_grupo_a = ((tabla.loc["Con recompensa","Grupo A"]/total_personas)*100)
print(recompensa_grupo_a,recompensa_grupo_b)

#Esto se hace para calcular la frecuencia de estas personas 
#por grupo y dividiendo el total de personas del grupo respectivamente
sin_recompensa = ((tabla.loc["Sin recompensa"]/tabla.sum())*100)
print(sin_recompensa)

#Ley de numeros pequeños !
""" investigar!
"""