# TicTacToe game
# Author : Loïc Pottier
# Creation date : 04/01/2022

# IMPORTS
import random as rd
from PIL import Image, ImageTk
from tkinter import *

# CONSTANTS
BACKGROUND_COLOR="#E0E0E0"
HEIGHT=400
WIDTH=400
BORDER_SIZE=10

class Board:
    def __init__(self) -> None:
        self.board=[[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        self.turn="X"

    # place a symbol on the board
    # and change self.turn to the other player
    def playTurn(self, x, y):
        if 0<=x<3 and 0<=y<3:
            if self.board[y][x]==0:
                self.board[y][x]=self.turn
                self.changeTurn()
                if not self.checkWin():
                    self.win(self.checkWin())
                elif self.checkDraw():
                    self.draw()
            else:
                return "invalid choice"
        else:
            return "invalid choice"

    # change self.turn attribute to the other player char 
    def changeTurn(self):
        if self.turn=="X":
            self.turn="O"
        else:
            self.turn="X"

    # return a printable version of self.board
    def __str__(self) -> str:
        returnStr="\n"
        for y in range (len(self.board)):
            for x in range (len(self.board[0])):
                returnStr+=" "+str(self.board[y][x])
            returnStr+="\n"
        return returnStr

    # check if a player has won
    def checkWin(self):
        for symbols in ["X", "O"]:
            for i in range(len(self.board)):
                # check on horizontal lines
                if self.board[i].count(symbols)==len(self.board[i]):
                    return symbols
                # check on vertical lines
                if self.board[0][i]==self.board[1][i]==self.board[2][i]==symbols:
                    return symbols
            # check on diagonal lines
            if self.board[0][0]==self.board[1][1]==self.board[2][2]==symbols:
                return symbols
            elif self.board[0][2]==self.board[1][1]==self.board[2][0]==symbols:
                return symbols
        return False

    # check is the party is a draw
    def checkDraw(self):
        if not self.checkWin():
            for row in self.board:
                for value in row:
                    if value==0:
                        return False
        return True
    
    def win(self, winner):
        print(winner+" a gagné !")
        self.reset()

    def draw(self):
        print("draw")
        self.reset()

    def reset(self):
        self.__init__()

    def graphics(self):
        for row in self.board:
            for value in row:
                if value=="X":
                    canvas.create_image(x*WIDTH/3 + BORDER_SIZE, y*HEIGHT/3+BORDER_SIZE, anchor="nw", image=xImage, tag="case")
            
                

window = Tk()
window.title("TicTacToe Game")
window.resizable(False, False)

label = Label(window, text="TicTacToe", font=("consolas", 20))
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
xImage=ImageTk.PhotoImage(Image.open("img/1.png").resize((int(WIDTH/3), int(HEIGHT/3))))

# BINDINGS


b = Board()

window.mainloop()


