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
