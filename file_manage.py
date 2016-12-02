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