from screeninfo import get_monitors

for m in get_monitors():
    if m.is_primary:
        # > print(f"Width: {m.width} Height: {m.height}")
        mainW = m.width // 2
        mainH = m.height // 2

# > this file is mainly used to house variables that way I don't hardcode them in the main file
# > mainW = monitorWidth
# > mainH = monitorHeight

gridLen = 6
cellCount = gridLen ** 2
numMines = cellCount // 4