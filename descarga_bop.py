import requests
from bs4 import BeautifulSoup
import os

def download_pdfs_from_url(url, download_folder):
    # Crear la carpeta de descarga si no existe
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Enviar una solicitud GET a la URL
    response = requests.get(url)
    
    # Analizar el contenido HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los enlaces en la página
    links = soup.find_all('a')
    
    # Iterar a través de los enlaces y descargar los PDFs
    for link in links:
        href = link.get('href')
        if href and href.endswith('.pdf'):
            pdf_url = href if href.startswith('http') else f"https://bop.dipgra.es{href}"
            pdf_response = requests.get(pdf_url)
            pdf_name = os.path.join(download_folder, os.path.basename(href))
            
            with open(pdf_name, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            
            print(f"Descargado: {pdf_name}")

# Ejemplo de uso
url = "https://bop.dipgra.es/publica/consulta-de-bops/"
download_folder = "pdfs_descargados"
download_pdfs_from_url(url, download_folder)
