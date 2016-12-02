# Nicolás Machado Saenz cod 13207014 Carlos Arturo Arredondo Trullo 12107001

# Miniproyecto

### A continuación se describiran los pasos necesarios para la implementación de un servicio web que obtenga información del sistema operativo.
#### 1. Instale centos 7 en su maquina virtual. para ello se recomienda revisar el siguiente tutorial: https://www.youtube.com/watch?v=Jy6NfzlVAKg
#### La descarga de centos 7 se puede realizar en el siguiente enlace: https://www.centos.org/download/
#### Cabe recordar que la versión a instalar de centos 7 es la minimal.

#### 2. Antes de continuar con la configuración del servicio web verifique que centos 7 se encuentra instalado en virtualbox. Posterior a ello configure las interfaces de red como se muestra en la siguiente imagen:

// imagen interfaces virtualbox

#### 3. Una vez iniciada la maquina virtual el siguiente paso es ingresar a la configuración de las interfaces para lograr que estas estén activas todo el tiempo. En la línea donde dice ONBOOT=no, se cambia por ONBOOT= yes. para ingresar a la configuración de las interfaces utilice:

```sh
# vi /etc/sysconfig/network-scripts/ifcfg-eth0
```
//interfaz2

#### 4. -como usuario root ingrese al siguiente directorio y modifique el archivo iptables
```sh
# cd /etc/sysconfig
# ls
# vi iptables
```
#### - Debajo de la línea que contiene el puerto 8080 agregue una igual, pero cambie el puerto por 8088 (el puerto es de libre elección).
// iptables

#### - Una vez guardado el archivo iptables, reinicie los servicios
```sh
# service iptables restart
```
// interfaz 3

#### 5. Lo siguiente será la instalación de algunas dependencias como python y los ambientes virtuales.
//entornos 1, entornos 2.

#### 6. En el directorio flask_env cree el archivo file_manage.py con el siguiente código

```py
from flask import Flask, abort, request

import json


from file_functions import crear_archivo, dar_archivos, eliminar_archivos

from last_files import get_last_files



app = Flask(__name__)



@app.route('/archivos', methods=['POST'])

def crear():

   cont_json = request.get_json(silent=False, force=True)

   filename = cont_json['filename']

   content = cont_json['content']

   if not filename:

      return 'No ha asignado un nombre al archivo!', 400

   if crear_archivo(filename, content):

      return 'Se ha creado exitosamente el archivo', 200

   else:

      return 'No se pudo crear el archivo',400



@app.route('/archivos', methods=['GET'])

def listar():

   miLista = {}

   miLista["files"] = dar_archivos()

   return json.dumps(miLista)



@app.route('/archivos', methods=['DELETE'])
def eliminar():

   cont_json = request.get_json(silent=False, force=True)

   name_delete = cont_json['name_delete']

   if not name_delete:

      return 'No ha definido que archivo quiere eliminar!', 400
   if not eliminar_archivos(name_delete):

      return 'Imposible eliminar los archivos del directorio', 400

   else:

      return 'Archivos eliminados exitosamente', 200



@app.route('/archivos', methods=['PUT'])
def colocar():

   abort(404)



@app.route('/archivos/ultimos', methods=['GET'])

def listar_ultimos():

   recent_list = {}

   recent_list["recent"] = get_last_files()

   return json.dumps(recent_list)



@app.route('/archivos/ultimos', methods=['POST'])

def crear_ultimos():

   abort(404)



@app.route('/archivos/ultimos', methods=['DELETE'])

def eliminar_ultimos():

   abort(404)



@app.route('/archivos/ultimos', methods=['PUT'])

def colocar_ultimos():

   abort(404)



if __name__ == "__main__":

   app.run(host='0.0.0.0',port=10500,debug='True')

```

#### Luego cree file_functions.py

```py
from subprocess import Popen, PIPE


def crear_archivo(filename, content):

   proceso1 = Popen(["touch",filename])

   proceso1 = Popen(["echo",content,">>",filename], stdout=PIPE, stderr=PIPE)

   proceso1.wait()

   return True if filename in dar_archivos() else False



def dar_archivos():

   proceso2 = Popen(["ls", "-l"], stdout=PIPE)

   lista_arch = Popen(["awk",'-F',' ','{print $9}'], stdin=proceso2.stdout, stdout=PIPE).communicate()[0].split('\n')

   return filter(None, lista_arch)



def eliminar_archivos(nombre_arch):

   if nombre_arch in dar_archivos():

      proceso3 = Popen(["rm", "-r", nombre_arch], stdout=PIPE)

      return True

   else:

      return False


```

#### finalmente last_files.py

```py
from subprocess import Popen, 
PIPE

def get_last_files():
   
elProceso = Popen(["find","-type","f","-mmin","-60"], stdout=PIPE)
   
rec_list = Popen(["awk",'-F','/','{print $NF}'],stdin=elProceso.stdout, stdout=PIPE).communicate()[0].split('\n')
   
return filter(None,rec_list)
```
#### 7. Con el ambiente activado ejecute el archivo file_manage.py  y realice pruebas.

// imagenes con la muestra

