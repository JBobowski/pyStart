# > this is a widely accepted and useful library used for creating 2D games with python
from tkinter import *
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
frameTop = Frame(win, bg = '#CDCDCD', width = settings.mainW, height = utils.calcHeight(25))
frameTop.place(x = 0, y = 0)

frameLS = Frame(win, bg = '#CDCDCD', width = utils.calcWidth(25), height = utils.calcHeight(75))
frameLS.place(x = 0, y = utils.calcHeight(25))

frameCent = Frame(win, bg = '#CDCDCD', width = utils.calcWidth(75), height = utils.calcHeight(75))
frameCent.place(x = utils.calcWidth(25), y = utils.calcHeight(25))

# > this main loop is actually what allow us to have the window
# > without this, there would be no minimize or close buttons in the top of our frame
win.mainloop()