# > this is a widely accepted and useful library used for creating 2D games with python
from tkinter import *
# > imports our class from our file
from cell import Cell
import settings # > need to import our other py file
import utils


# > create a window
win = Tk()

# > .geometry is used to set the dimensions of our frame [Width by Height]
# > EDIT: f'{}x{} is called a formatted string and allows us to put values in our string
win.geometry(f'{settings.mainW}x{settings.mainH}')
# > the window will not be resizable
win.resizable(False, False)
# > styling
win.config(bg = '#CDCDCD')

# > sets the title in the top banner of the frame
win.title("Minesweeper_v1.0")



# > this creates a new frame on our window
frameTop = Frame(
    win, 
    bg = '#CDCDCD', 
    width = settings.mainW, 
    height = utils.calcHeight(15)
)
frameTop.place(
    x = 0, 
    y = 0
)

win.update()

gameTitle = Label(
    frameTop,
    bg = '#CDCDCD',
    fg = 'black',
    text = 'MINESWEEPER',
    font = ('Verdana 10 bold', 32)
)
gameTitle.place(
    x = utils.calcWidth(25), 
    y = ((frameTop.winfo_height()) // 2) - 21
)

frameLS = Frame(
    win, 
    bg = '#CDCDCD', 
    width = utils.calcWidth(25), 
    height = utils.calcHeight(80)
)
frameLS.place(
    x = 0, 
    y = utils.calcHeight(15)
)

frameCent = Frame(
    win, 
    bg = '#CDCDCD', 
    width = utils.calcWidth(70), 
    height = utils.calcHeight(80)
)
frameCent.place(
    x = utils.calcWidth(25), 
    y = utils.calcHeight(15)
)

frameRS = Frame(
    win, 
    bg = '#CDCDCD', 
    width = utils.calcWidth(5), 
    height = utils.calcHeight(80)
)
frameRS.place(
    x = utils.calcWidth(95), 
    y = utils.calcHeight(15)
)

frameBot = Frame(
    win, 
    bg = '#CDCDCD', 
    width = settings.mainW, 
    height = utils.calcHeight(5)
)
frameBot.place(
    x = 0, 
    y = utils.calcHeight(95)
) 

win.update()


for i in range(settings.gridLen):
    for j in range(settings.gridLen):
        newCell = Cell(i, j)
        newCell.createBtnObj(frameCent)
        newCell.btnObj.grid(column = i, row = j)

Cell.cellLabel(frameLS)
Cell.cellCountLabelObj.place(x = 0, y = 0)

Cell.randomMineVals()

# > this main loop is actually what allow us to have the window
# > without this, there would be no minimize or close buttons in the top of our frame
win.mainloop()