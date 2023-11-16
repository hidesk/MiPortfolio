#Usamos pandas y lo definimos como pd
import pandas as pd
#Se importa el archivo desde la ubicaion o carpeta en donde
#esta se encuentra
casen = pd.read_csv("C:\Workspace\Curso GOB\Python2\importar\casen_2017.csv", sep=";", encoding="unicode_escape")

#Imprimira toda la tabla de excel en la terminal
#print(casen)

#La funcion head() imprimira las primeras filas segun el numero
#print(casen.head(3))

#Podemos explorar la tabla y ver una columna especifica
#de estas dos maneras
#print(casen.sexo)
#print(casen["sexo"])

#Podemos recuperar una posicion o fila especifica dentro de
#cada columna
#La propiedad .iloc[] permite ubicar coordenadas especificas
#de un dataframe, en funcion de los valores indicados 
#print(casen.sexo[10])
#print(casen["sexo"].iloc[10])

#Si quisieramos filtrar solo a las mujeres del dataframe
#podriamos hacerlo de la siguiente manera:
#print(casen.loc[casen["sexo"]=="Mujer"])

#Podriamos hacer mas compleja la situacion filtrando a todas
#las mujeres con mas de 12 años de escolaridad
#Usaremos operadores logicos
#print(casen.loc[(casen["sexo"]=="Mujer")&(casen["esc"]>12)])

#Tambien podriamos buscar datos en las tablas por coordenadas
#numero de fila y columna, por ejemplo, si queremos recuperar
#la fila 10 de la columna 3
#print(casen.iloc[10,3])

#O podemos recuperar ciertas columnas o filas especificas
#en este caso, recuperamos la columna 2,5 y 6
#el simbolo de dos puntos ":" en la posicion de las filas
#de la propiedad .iloc[], indica "Todos", esto es que
#trae todas las filas de las columnas 2,5 y 6
#print(casen.iloc[:,[2,5,6]])

#El metodo .describe los datos del archivo importado
#print(casen.describe())

#Tambien podemos describir columnas especificas, indicandole
#entre corchetes, y llamando la funcion .describe()
#print(casen["edad"].describe())

#Este ejemplo es para hacer el codigo de mas arriba
#pero de una manera mas legible
pd.set_option("display.float_format", lambda x: "%.5f"% x)
casen=pd.read_csv("C:\Workspace\Curso GOB\Python2\importar\casen_2017.csv",
                  sep=";", encoding= "unicode_escape")
casen["edad"].describe

#Lo que nos permite .nunique() es ver la cantidad de diferentes
#edades entre si
#print(casen["edad"].nunique())

#Con .max podemos ver el valor maximo de los datos de la tabla
#en este caso la edad maxima
#print(casen["edad"].max())

#Otra forma de tener una mirada general de los datos es agregando
#o agrupando los datos
#Para ello usamos el metodo .groupby() quien agrupara por alguna
#de las variables o columnas,y calcula los estadisticos
#en este caso el promedio para cada grupo
#.groupby() agrupacion 
#("sexo")["edad"] columna a agrupar
# .mean estadistico
#print(casen.groupby("sexo")["edad"].mean())

#Si quisieramos asignar esto a un objeto en formato dataframe
#para analizarlo aparte, incluimos el parametro"as_index=False
#de esta forma:
#edad_por_sexo=casen.groupby("sexo",as_index=False)["edad"].mean()
#print(edad_por_sexo)

#Tambien podemos agregar una nueva categoria
casen["contador"]=1
#la funcion .agg es otra funcion de agregacion
#print(casen.groupby(["sexo","es_indigena"]).agg({"contador":"sum"}))

#Si quisieramos sacar el promedio de ingreso, lo podemos 
#hacer de la siguiente manera (recuerda que mean=promedio)
#Tenemos todos los valores por sexo y etnia
etnicidad_y_sexo=casen.groupby(["sexo","es_indigena"]).agg({"contador":"sum"})
print(etnicidad_y_sexo)

#Ahora obtenemos el agregado por cada sexo, lo cual se 
# obtiene asi, obteniendo finalmente la cantidad de personas
#por sexo
por_sexo=etnicidad_y_sexo.groupby("sexo").sum()
print(por_sexo)

#Ya con esto podemos obtener el resultado que esperamos
#divideindo nuestra tabla original por la agregacion a nivel
#de sexo, de la siguiente forma:
final=etnicidad_y_sexo/etnicidad_y_sexo.groupby("sexo").sum()
print(final)

