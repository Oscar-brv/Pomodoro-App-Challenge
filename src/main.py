# La interfaz gráfica se crea con la ayuda de Tkinter, una librería nativa de Python
# Se puede haber realizado en Kivy por ejemplo, pero se debe haber hecho la instalación de dicho framework.
from cgitb import text
from tkinter import *
from functions import Functions
from register import Files
from interface import Interface

# Constants
background_color = "#FFFFFF"
text_color = "#000000"
no_borders = 0
window_width = 500
window_height = 500
button_row = 2

# Screen
window = Tk()
window.title("Pomodoro App Challenge")
window.config(padx=50, pady=20, background= background_color)
window.minsize(width=window_width, height=window_height)
window.maxsize(width=window_width, height=window_height)
window.iconbitmap("./img/tomato_icon.ico")

# Title
title = Label(text="Timer", font=("Courier", 40, "bold"))
title.config(background=background_color, foreground=text_color)
title.grid(row=0, column=0, columnspan=4)

# Timer
timer = Label(text="00:00", font=("Courier", 40, "bold"))
timer.config(background=background_color, foreground=text_color)
timer.grid(row=1, column=0, columnspan=4)

# Start Button
play_icon = PhotoImage(file="./img/play_icon.png", height=99, width=88)
start_button = Button(
        highlightthickness=no_borders, 
        image=play_icon, 
        foreground=background_color, 
        background=background_color, 
        borderwidth=no_borders)
start_button.grid(row=button_row, column=0)

# Pause Button
pause_icon = PhotoImage(file="./img/pause_icon.png", height=100, width=100)
pause_button = Button(
        highlightthickness=no_borders, 
        image=pause_icon, 
        foreground=background_color, 
        background=background_color, 
        borderwidth=no_borders)
pause_button.grid(row=button_row, column=1)

# Stop Button
stop_icon = PhotoImage(file="./img/stop_icon.png", height=100, width=100)
stop_button = Button(
        highlightthickness=no_borders, 
        image=stop_icon, 
        foreground=background_color, 
        background=background_color, 
        borderwidth=no_borders)
stop_button.grid(row=button_row, column=2)

# Next Button
next_icon = PhotoImage(file="./img/next_icon.png", height=100, width=100)
next_button = Button(
        highlightthickness=no_borders, 
        image=next_icon, 
        foreground=background_color, 
        background=background_color, 
        borderwidth=no_borders)
next_button.grid(row=button_row, column=3)

# Main Loop Screen
window.mainloop()
