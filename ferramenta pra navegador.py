import webbrowser
from tkinter import *
root = Tk( )
root.title("Abrir navegador")
root.geometry("260x130")

def google():
    webbrowser.open("www.google.com")
mygoogle = Button(root, text="Abrir site.", command=google).pack(pady=20)
root.mainloop()
