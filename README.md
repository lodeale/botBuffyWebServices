# botBuffyWebServices
Con este script podemos disponibilizar servicios sencillos para que el botBuffy pueda enviarles información del usuario, y los servicios devuelvan información mediante botBuffy para entregarle al usuario.

# Instalación
* pip install -r requirements.txt

# uso
* python server.py

# Disponibilizar nuevo servicio
* Creamos un nuevo servicio en la carpeta lib/classes/helloWorld.py con el siguiente contenido:

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.src.servicesInterface import ServicesInterface

class HelloWorld(ServicesInterface):
	_args=[]
	
	def execute(self):
            pass

	def getResult(self):
            return 'Hola Mundo!!!' 
```
 
* Luego modificamos el archivo lib/core/core.py. El siguiente diff muestra los cambios necesario para agregar un servicio:

``` diff
diff --git a/lib/core/core.py b/lib/core/core.py
index a3e9666..562f571 100755
--- a/lib/core/core.py
+++ b/lib/core/core.py
@@ -2,12 +2,14 @@
 # -*- coding: utf-8 -*-
 
 from lib.classes.weatherYahoo import WeatherYahoo
+from lib.classes.helloWorld import HelloWorld
 
 class Core(object):
        _answer = []
        _sqlo = None
        _services = {
                'tiempo': WeatherYahoo,
+                'hola' : HelloWorld,
                }
 
        def __init__(self):
@@ -28,6 +30,8 @@ class Core(object):
                array_response = response.split('+')
                if 'tiempo' in array_response:
                        indexCommand,wordCommand=array_response.index('tiempo'),'tiempo'
+                elif 'hola' in array_response:
+                        indexCommand,wordCommand=0,'hola'
 
                objServices = self.instanceServices(wordCommand,array_response[indexCommand+1:])
                objServices.execute()
 ``` 
 
 Estos cambios disponibilizan un servicio nuevo. Ahora es cuestión de imaginacion.
