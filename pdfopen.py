import PyPDF2
from tkinter import filedialog

def choosePath():
    try:
        x = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        return x
    except FileNotFoundError:
        print('Nie wybrano ścieżki pliku')

choosenPath = choosePath()

# Otwórz plik PDF
with open(choosenPath, 'rb') as pdf_file:
    # Utwórz obiekt PdfFileReader
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Wyświetl ilość stron w pliku PDF
    print('Liczba stron w pliku PDF:', pdf_reader.getNumPages())

    # Wyświetl całą zawartość pliku PDF
    for page in range(pdf_reader.getNumPages()):
        print('Strona', page + 1)
        print(pdf_reader.getPage(page).extractText())
