import os
import fitz  # PyMuPDF

def count_words_in_pdf(pdf_path):
    # Abre el archivo PDF
    pdf_document = fitz.open(pdf_path)
    word_count = 0
    
    # Itera a través de cada página
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        words = text.split()
        word_count += len(words)
    
    return word_count

def count_words_in_folder(folder_path):
    word_counts = {}
    
    # Itera a través de cada archivo en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            word_counts[filename] = count_words_in_pdf(file_path)
    
    return word_counts

# Ejemplo de uso
folder_path = "./"  # Reemplaza con la ruta a tu carpeta
word_counts = count_words_in_folder(folder_path)

for filename, count in word_counts.items():
    print(f"El archivo {filename} contiene {count} palabras.")
