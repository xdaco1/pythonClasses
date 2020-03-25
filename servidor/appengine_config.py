#archivo necesario para despliegue en GCloud

#Google no usa pip para instalar las librerías necesarias por lo que
#también es necesario suministrárselas
from google.appengine.ext import vendor

vendor.add('lib') #Las librerías (requirements) van a estar disponibles en esta carpeta