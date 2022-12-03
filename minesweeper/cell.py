# > need to create an individualized class for the cells on our minesweeper grid
from tkinter import Button
import random
import settings

class Cell:
    all = []
    # > constructor
    def __init__(self, x, y, mineVal = False):
        self.mineVal = mineVal
        self.btnObj = None
        self.x = x
        self.y = y

        # > append object to list
        Cell.all.append(self)
    
    def createBtnObj(self, location):
        btn = Button(location, height = 3, width = 6)
        # > need to create actions for our buttons
        # > <Button-1> is conventional for left click
        btn.bind('<Button-1>', self.actionLC)
        btn.bind('<Button-3>', self.actionRC)
        self.btnObj = btn
    
    def actionLC(self, event):
        if self.mineVal:
            self.dispMine()
    
    def dispMine(self):
        # > this will stop the game and tell the user they have lost
        self.btnObj.configure(bg = 'red')

    def actionRC(self, event):
        print("here on the right")

    @staticmethod
    def randomMineVals():
        mineCells = random.sample(Cell.all, settings.numMines)
        for mineCell in mineCells:
            mineCell.mineVal = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"