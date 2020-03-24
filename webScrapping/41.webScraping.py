
#Hay info disponible en la web pero disponible
#sólo a través de un navegador (precios de casas,
# monitorear precios, o descargar mucha información)

#Los scrapers permiten automatizar el proceso obteniendo
#los datos de los sitios web y almacenarlos.

#Ej
#Indexar la web
#Reputación web
#Obtener precios

#Se imlementará un scraper para obtener imágenes de xkcd.com

#beautifulsoup4 permite interpretar interpretar el html, modificarlo y 
#accederlo como si fuera un árbol

#Identificar la estructura del sitio web (inspect)
#Se identifica la imagen a "scrapear" https://imgs.xkcd.com/comics/exa_exabyte.png
#También se identifica un patrón xkcd/#imagen/

import requests
from bs4 import BeautifulSoup
import urllib.request

def run():
    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i)) #Obtiene html
        soup = BeautifulSoup(response.content,'html.parser') #Parsing del html
        image_container = soup.find(id='comic') #id del <div> que contiene la <img>
        image_url = image_container.find('img')['src'] #obtiene el atributo src de la etiqueta img
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url),image_name)        

if __name__ == "__main__":
    run()
