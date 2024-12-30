import requests
from bs4 import BeautifulSoup
import os

# Lista de URLs
urls = [
"https://www.boe.es/borme/dias/2024/12/02/",
"https://www.boe.es/borme/dias/2024/12/03/",
"https://www.boe.es/borme/dias/2024/12/04/",
"https://www.boe.es/borme/dias/2024/12/05/",
"https://www.boe.es/borme/dias/2024/12/09/",
"https://www.boe.es/borme/dias/2024/12/10/",
"https://www.boe.es/borme/dias/2024/12/11/",
"https://www.boe.es/borme/dias/2024/12/12/",
"https://www.boe.es/borme/dias/2024/12/13/",
"https://www.boe.es/borme/dias/2024/12/16/",
"https://www.boe.es/borme/dias/2024/12/17/",
"https://www.boe.es/borme/dias/2024/12/18/",
"https://www.boe.es/borme/dias/2024/12/19/",
"https://www.boe.es/borme/dias/2024/12/20/",
"https://www.boe.es/borme/dias/2024/12/23/",
"https://www.boe.es/borme/dias/2024/12/24/",
"https://www.boe.es/borme/dias/2024/12/26/",
"https://www.boe.es/borme/dias/2024/12/27/",
"https://www.boe.es/borme/dias/2024/12/30/"
    # Añade más URLs aquí
]

# Crear un directorio para guardar los PDFs descargados
os.makedirs('downloaded_pdfs_anual', exist_ok=True)

for url in urls:
    # Enviar una solicitud GET a la página web
    response = requests.get(url)

    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los enlaces a archivos PDF
    pdf_links = soup.find_all('a', href=True)
    pdf_urls = ["https://www.boe.es" + link['href'] for link in pdf_links if link['href'].endswith('.pdf')]

    # Obtener la parte final de la URL para usarla como prefijo
    # url_suffix = url.split('/')[-2].replace('/', '') + "_"

    # Obtener la parte final de la URL para usarla como prefijo
    url_suffix = url.split('/')[-4] + url.split('/')[-3] + url.split('/')[-2] + "_"    

    # Descargar cada archivo PDF y guardarlo en el directorio con el prefijo adecuado
    for pdf_url in pdf_urls:
        pdf_response = requests.get(pdf_url)
        pdf_name = os.path.join('downloaded_pdfs', url_suffix + pdf_url.split('/')[-1])
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

print("Descargados todos los archivos PDF de las URLs proporcionadas con el prefijo adecuado.")
