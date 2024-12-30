import requests
from bs4 import BeautifulSoup
import os

# Lista de URLs
urls = [
    "https://www.boe.es/borme/dias/2024/01/02/",
    "https://www.boe.es/borme/dias/2024/01/03/",

    # Añade más URLs aquí
]

# Crear un directorio para guardar los PDFs descargados
os.makedirs('downloaded_pdfs', exist_ok=True)

for url in urls:
    # Enviar una solicitud GET a la página web
    response = requests.get(url)

    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los enlaces a archivos PDF
    pdf_links = soup.find_all('a', href=True)
    pdf_urls = ["https://www.boe.es" + link['href'] for link in pdf_links if link['href'].endswith('.pdf')]

    # Descargar cada archivo PDF y guardarlo en el directorio
    for pdf_url in pdf_urls:
        pdf_response = requests.get(pdf_url)
        pdf_name = os.path.join('downloaded_pdfs', pdf_url.split('/')[-1])
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

print("Descargados todos los archivos PDF de las URLs proporcionadas.")
