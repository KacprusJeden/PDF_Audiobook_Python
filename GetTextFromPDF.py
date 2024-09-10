from PyPDF2 import PdfReader
from tkinter import filedialog

class ExtendFileExcpetion(Exception):
    pass

def choosePath():
    try:
        x = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        return x
    except FileNotFoundError:
        print('Nie wybrano ścieżki pliku')

def extractTextFromPdf(choosenPath):
    try:
        if choosenPath is not None:
            text = ''
            reader = PdfReader(choosenPath)

            for num in range(len(reader.pages)):
                text += f'strona {num + 1} \n\n'
                page = reader.pages[num]
                text += f'{page.extract_text()} \n\n'

            return text

        else:
            raise FileNotFoundError
    except FileNotFoundError:
        return 'Nie wybrano ścieżki pliku'