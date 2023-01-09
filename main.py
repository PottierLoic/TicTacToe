# TicTacToe game
# Author : Loïc Pottier
# Creation date : 04/01/2022

# IMPORTS
import random as rd
from tkinter import *
from PIL import Image, ImageTk

# CONSTANTS
BACKGROUND_COLOR="#E0E0E0"
SIZE=100
IN_BETWEEN_SIZE=60
SIZE_DIFFERENCE=IN_BETWEEN_SIZE/2.5

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
                self.graphics()
                if self.checkWin()!=False:
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
        label.config(text="WINNN")

    def draw(self):
        label.config(text="DRAWWW")

    def reset(self):
        self.__init__()
        self.graphics()

    def graphics(self):
        canvas.delete('case')
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if x==0:
                    diffx=1
                elif x==1:
                    diffx=0
                else:
                    diffx=-1

                if y==0:
                    diffy=1
                elif y==1:
                    diffy=0
                else:
                    diffy=-1

                if self.board[y][x]=="X":
                        canvas.create_image(x*SIZE + x*IN_BETWEEN_SIZE + diffx * SIZE_DIFFERENCE, y*SIZE + y*IN_BETWEEN_SIZE + diffy * SIZE_DIFFERENCE, anchor="nw", image=crossImage, tag="case")
                elif self.board[y][x]=="O":
                    canvas.create_image(x*SIZE + x*IN_BETWEEN_SIZE + diffx * SIZE_DIFFERENCE, y*SIZE + y*IN_BETWEEN_SIZE + diffy * SIZE_DIFFERENCE, anchor="nw", image=circleImage, tag="case")
            
def click(event):
    x=event.x
    y=event.y

    if not b.checkWin() and not b.checkDraw():
        if x<=SIZE:
            posx=0
        elif SIZE+IN_BETWEEN_SIZE<=x<=SIZE*2+IN_BETWEEN_SIZE:
            posx=1
        elif (SIZE+IN_BETWEEN_SIZE)*2<=x<=SIZE*3+IN_BETWEEN_SIZE*2:
            posx=2
        else:
            posx=-1

        if y<=SIZE:
            posy=0
        elif SIZE+IN_BETWEEN_SIZE<=y<=SIZE*2+IN_BETWEEN_SIZE:
            posy=1
        elif (SIZE+IN_BETWEEN_SIZE)*2<=y<=SIZE*3+IN_BETWEEN_SIZE*2:
            posy=2
        else:
            posy=-1

        if posx!=-1 and posy!=-1:
            b.playTurn(posx, posy)
            turnText = "Actual player : "+str(b.turn)
            turnLabel.configure(text=turnText)
    else:
        b.reset()


b = Board()   

window = Tk()
window.title("TicTacToe Game")
window.resizable(False, False)

label = Label(window, text="TicTacToe", font=("consolas", 20))
label.pack()

turnText = "Actual player : "+str(b.turn)
turnLabel = Label(window, text=turnText, font=("consolas", 10))
turnLabel.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=SIZE*3 + 2*IN_BETWEEN_SIZE, width=SIZE*3 + 2*IN_BETWEEN_SIZE)
canvas.pack()

window.update()

windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
crossImage=ImageTk.PhotoImage(Image.open("img/cross.png").resize((SIZE, SIZE)))
circleImage=ImageTk.PhotoImage(Image.open("img/circle.png").resize((SIZE, SIZE)))
backgroundImage=ImageTk.PhotoImage(Image.open("img/background.png").resize((SIZE*3 + 2*IN_BETWEEN_SIZE, SIZE*3 + 2*IN_BETWEEN_SIZE)))

canvas.create_image(0, 0, anchor="nw", image=backgroundImage, tag="background")

# BINDINGS
window.bind('<Button-1>', click)


window.mainloop()


