# Fichero dedicado a crear los elementos gráficos necesarios
from tkinter import *
import tkinter

class Interface:
    
    def __init__(self):

        window = tkinter.Tk()
        window.title("Pomodoro App Challenge")
        window.config(padx=50, pady= 20, background= "#000000")
        window.minsize()
        window.iconwindow()

        window.mainloop()
        