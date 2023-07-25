from io import StringIO
from pdfminer.high_level import extract_text
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
            with open(choosenPath, "rb") as file:
                text = extract_text(file)
                text = text.encode("utf-8")
                text = text.decode("utf-8")
                text = StringIO(text)
            return text.read()
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        return 'Nie wybrano ścieżki pliku'