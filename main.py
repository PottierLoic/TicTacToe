# TicTacToe game
# Author : Loïc Pottier
# Creation date : 04/01/2022

# IMPORTS
import random as rd
from tkinter import *

# CONSTANTS
BACKGROUND_COLOR="#E0E0E0"
HEIGHT=400
WIDTH=400

window = Tk()
window.title("TicTacToe Game")
window.resizable(False, False)

label = Label(window, text="TicTacToe", font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

# BINDINGS



window.mainloop()

