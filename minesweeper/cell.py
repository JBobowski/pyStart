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
        else:
            if self.theMinesSurrounding == 0:
                for cellObj in self.theSurroundings:
                    cellObj.dispCell()
            self.dispCell()
    
    def cellByAxis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def theSurroundings(self):
        cells = [ 
            self.cellByAxis(self.x - 1, self.y - 1),
            self.cellByAxis(self.x - 1, self.y),
            self.cellByAxis(self.x - 1, self.y + 1),
            self.cellByAxis(self.x, self.y - 1),
            self.cellByAxis(self.x + 1, self.y - 1),
            self.cellByAxis(self.x + 1, self.y),
            self.cellByAxis(self.x + 1, self.y + 1),
            self.cellByAxis(self.x, self.y + 1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def theMinesSurrounding(self):
        counter = 0
        for cell in self.theSurroundings:
            if cell.mineVal:
                counter += 1
        return counter

    def dispCell(self):
        self.btnObj.configure(text = self.theMinesSurrounding)

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