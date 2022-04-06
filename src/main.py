# La interfaz gráfica se crea con la ayuda de Tkinter, una librería nativa de Python
# Se puede haber realizado en Kivy por ejemplo, pero se debe haber hecho la instalación de dicho framework.
from cgitb import text
from tkinter import *
from functions import Functions
from register import Files
from interface import Interface

# Screen
window = Tk()
window.title("Pomodoro App Challenge")
window.config(padx=50, pady= 20, background= "#ffdfac")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.iconbitmap("./img/tomato_icon.ico")

# Title
title = Label(text="Timer", font=("Courier", 40, "bold"))
title.config(background="#ffdfac", foreground="white")
title.grid(row=0, column=1)

# Start Button
play_icon = PhotoImage(file="./img/play_icon.png", height=100, width=90)
start_button = Button(highlightthickness=0, image=play_icon)
start_button.grid(row=1, column=0)

# Main Loop Screen
window.mainloop()
