from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Reloj - Tarea 8 - 1989934')

def hora(): 
    datos = strftime('%I:%M:%S %p')
    label.config(text = datos)
    label.after(1000, hora)

label = Label(root,
    font = (
        'Comic Sans MS', 60
    ),
    padding= '50',
    background= 'BLUE',
    foreground= 'GRAY'
)

label.pack(expand= True)
hora()
mainloop()