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

# Ejemplo de uso
# pdf_path = "ilovepdf_merged.pdf"  # Reemplaza con la ruta a tu archivo PDF
# pdf_path = "ilovepdf_merged_compressed.pdf"  # Reemplaza con la ruta a tu archivo PDF
# pdf_path = "bop-26_12_2024.pdf"  # Reemplaza con la ruta a tu archivo PDF
# pdf_path = "bop-27_12_2024.pdf"  # Reemplaza con la ruta a tu archivo PDF
pdf_path = "bop-30_12_2024.pdf"  # Reemplaza con la ruta a tu archivo PDF
word_count = count_words_in_pdf(pdf_path)
print(f"El archivo PDF contiene {word_count} palabras.")
