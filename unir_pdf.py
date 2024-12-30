import PyPDF2

def unir_pdfs(lista_pdfs, salida):
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf in lista_pdfs:
        with open(pdf, 'rb') as archivo:
            pdf_merger.append(archivo)
    
    with open(salida, 'wb') as archivo_salida:
        pdf_merger.write(archivo_salida)

lista_pdfs = [

"downloaded_pdfs_anual/20241230_BORME-A-2024-250-01.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-02.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-04.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-06.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-07.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-08.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-11.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-15.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-17.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-18.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-22.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-24.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-26.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-28.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-30.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-35.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-36.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-38.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-39.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-42.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-46.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-47.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-49.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-50.pdf",
 "downloaded_pdfs_anual/20241230_BORME-A-2024-250-99.pdf",
 "downloaded_pdfs_anual/20241230_BORME-C-2024-7145.pdf",
 "downloaded_pdfs_anual/20241230_BORME-C-2024-7146.pdf",
 "downloaded_pdfs_anual/20241230_BORME-C-2024-7147.pdf",
 "downloaded_pdfs_anual/20241230_BORME-C-2024-7148.pdf",
 "downloaded_pdfs_anual/20241230_BORME-C-2024-7149.pdf",
 "downloaded_pdfs_anual/20241230_BORME-S-2024-250.pdf"


    ]  # Añade tus archivos PDF aquí
salida = 'archivo_unido.pdf'

unir_pdfs(lista_pdfs, salida)
print("¡Archivos PDF combinados exitosamente!")
