# > need to create an individualized class for the cells on our minesweeper grid
from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cellCount = settings.cellCount
    cellCountLabelObj = None
    # > constructor
    def __init__(self, x, y, mineVal = False):
        self.mineVal = mineVal
        self.shown = False
        self.possMine = False
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

    @staticmethod
    def cellLabel(location):
        label = Label(
            location,
            bg = '#CDCDCD',
            fg = 'black',
            text = f"Cells Left: {Cell.cellCount}",
            font = ("",16)
        )
        Cell.cellCountLabelObj = label

    def actionLC(self, event):
        if self.mineVal:
            self.dispMine()
        else:
            if self.theMinesSurrounding == 0:
                for cellObj in self.theSurroundings:
                    cellObj.dispCell()
            self.dispCell()
            if Cell.cellCount == settings.numMines:
                ctypes.windll.user32.MessageBoxW(0, 'You Won!', 'Game Over', 0)

        self.btnObj.unbind('<Button-1>')
        self.btnObj.unbind('<Button-3>')
    
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
        if not self.shown:
            Cell.cellCount -= 1
            self.btnObj.configure(text = self.theMinesSurrounding)
            if Cell.cellCountLabelObj:
                Cell.cellCountLabelObj.configure(text = f"Cells Left: {Cell.cellCount}")
            self.btnObj.configure(bg = 'SystemButtonFace')
        self.shown = True

    def dispMine(self):
        self.btnObj.configure(bg = 'red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    def actionRC(self, event):
        if not self.possMine:
            self.btnObj.configure( bg = '#FFAA29')
            self.possMine = True
        else:
            self.btnObj.configure( bg = 'SystemButtonFace')
            self.possMine = False

    @staticmethod
    def randomMineVals():
        mineCells = random.sample(Cell.all, settings.numMines)
        for mineCell in mineCells:
            mineCell.mineVal = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"