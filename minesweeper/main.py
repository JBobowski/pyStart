# > this is a widely accepted and useful library used for creating 2D games with python
from tkinter import *

# > create a window
win = Tk()

# > .geometry is used to set the dimensions of our frame [Width by Height]
win.geometry('640x480')
# > the window will not be resizable
win.resizable(False, False)
# > styling
win.config(bg = '#CDCDCD')

# > sets the title in the top banner of the frame
win.title("Minesweeper_v1.0")

# > this main loop is actually what allow us to have the window
# > without this, there would be no minimize or close buttons in the top of our frame
win.mainloop()