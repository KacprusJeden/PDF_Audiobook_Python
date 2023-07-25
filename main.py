from GetTextFromPDF import choosePath, extractTextFromPdf
import VoiceReadModule
from tkinter import *

root = Tk()
root.title('Audiobook')
root.geometry('1200x700')
root.configure(bg='#dc143c')


text = extractTextFromPdf(choosePath())

playButton = Button(text='Play', command=lambda: VoiceReadModule.readText(text),
                    borderwidth=0,
                    cursor="hand2", background='#f05c79', padx=5, pady=5, fg='#460713')
playButton.place(x=15, y=50)


bookText = Text(root, width=55, height=75, bg='#ffffff')
bookText.pack(pady=40)
bookText.insert("end", text)


root.mainloop()
