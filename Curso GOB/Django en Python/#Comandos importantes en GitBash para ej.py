#Comandos importantes en GitBash para ejecutar Django

"""Para el manejo del entorno virtual de Python
haremos uso del mismo programa GitBash, ya que dicho
virtualenv se instala,crea y ejecuta mediante un 
comando en Python"""
#Crear entorno virtual en la carpeta de nuestro proyecto
"""Para instalar nuestro virtualenv utilizamos el 
siguiente comando:
python -m pip install virtualenv

para comprobar la version utilizamos el comando:
python -m virtualenv --version
"""
#Para crear nuestro propio virtualenv, y despues
#nuestro proyecto en Django
"""Para esto vamos a la carpeta en donde queramos trabajar
Dentro de esta hacemos clic dereco y seleccionamos la opcion:
GitBash Here
Se abrira GitBash posicionado en esa carpeta
"""
"""Luego de eso escribimos el siguiente comando:
python -m virtualenv PruebaDjango(Nombre de tu proyecto)

Este comando nos crea un virtualenv llamado "PruebaDjango"
el cual estara ubicado en la carpeta en donde esta 
posicionado el GitBash
"""
#Para acceder a la carpeta creada
"""Para esto hacemos uso del siguiente comando:
cd PruebaDjango
"""
#Para iniciar nuestro virtualenv
"""Para iniciar nuestro virtualenv, escribimos
el siguiente comando:
source Scripts/activate

Ahora se mostrara el nombre de nuestro virtualenv entre
parentesis(), esto indica que se ha iniciado correctamente
 """
 #IMPORTANTE! SI SE CIERRA NUESTRO GITBASH Y SE ABRE OTRA, SE
 #TENDRA QUE VOLVER A INICIAR EL VIRTUALENV, ENTRANDO A SU
 #CARPETA Y USANDO EL CODIGO:
 #source Scripts/activate

"""Para instalar Django en nuestro entorno virtual
debemos ejecutar el siguiente comando:
python -m pip install Django
"""

"""Para comprobar que version tenemos instalada
utilizamos el siguiente comando:
python -m django --version
"""
"""Para empezar con nuestro proyecto necesitamos 
estar en nuestro entorno virtual iniciado previamente
y que el GitBash este iniciado en la carpeta
Luego utilizamos en comando:
django-admin startproject PruebaProjecto(nombre del proyecto)
"""

"""Ahora procedemos a ejecutar el "Hola Mundo" que crea Django
por defecto, para ello ingresamos a la carpeta del proyecto
haciendo uso del comando:
cd PruebaProyecto
"""
"""Finalmente ejecutamos el siguiente comando:
python manage.py runserver
"""
