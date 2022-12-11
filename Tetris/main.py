# > keep in mind: seven shapes in tetris. Need to define a center point for each of these shapes, will be used as the center of rotation
import pygame
from copy import deepcopy
from random import choice, randrange

# > need to create tile dimensions and size
tileW, tileH = 10, 20
tileDim = 45

GAME_RES = tileW * tileDim, tileH * tileDim
newRes = 750, 940
gameFrames = 60

pygame.init()
#sc = pygame.display.set_mode(newRes)
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

# > need to create a grid for the game. Can do this with two dimensional array
# > each element is a rect
grid = [pygame.Rect(x * tileDim, y * tileDim, tileDim, tileDim) for x in range(tileW) for y in range(tileH)]

# > as stated above, seven figures in tetris. We can hold those figures in a list within a list
# > tripled checked these coordinates in windows paint, everything looks correct initially
shapesCords = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

# > using the positions above we need to do two things: 
# > 1. create rectangles out of the coordinates
shapesRect = [[pygame.Rect(x + tileW // 2, y + 1, 1, 1) for x, y in theCords] for theCords in shapesCords]
shapesDraw = pygame.Rect(0, 0, tileDim - 2, tileDim - 2)
playMap = [[0 for i in range(tileW)] for j in range(tileH)]

# > 2. draw those rectangles that we create
# > this is going to be in our while loop, look below under the grid outline

# > falling animation variables
counter, speed, limit = 0, 5, 2000
shape = deepcopy(choice(shapesRect))

# > time to color the shapes
randColors = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
color = randColors()

def borders():
    if shape[i].x < 0 or shape[i].x > tileW - 1:
        return False
    elif shape[i].y > tileH - 1 or playMap[shape[i].y][shape[i].x]:
        return False
    return True

while True:
    leftRightMove, shapeRotate = 0, False
    game_sc.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                leftRightMove = -1
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                leftRightMove = 1
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                limit = 100
            elif event.key == pygame.K_UP or event.key == ord('w'):
                shapeRotate = True

    # > horizontal movement
    copyShape = deepcopy(shape)
    for i in range(4):
        shape[i].x += leftRightMove
        if not borders():
            shape = deepcopy(copyShape)
            break

    # > vertical movement
    counter += speed
    if counter > limit:
        counter = 0
        copyShape = deepcopy(shape)
        for i in range(4):
            shape[i].y += 1
            if not borders():
                for i in range(4):
                    playMap[copyShape[i].y][copyShape[i].x] = color
                color = randColors()
                shape = deepcopy(choice(shapesRect))
                limit = 2000
                break

    # > rotate the shapes
    center = shape[0]
    copyShape = deepcopy(shape)
    if shapeRotate:
        for i in range(4):
            x = shape[i].y - center.y
            y = shape[i].x - center.x
            shape[i].x = center.x - x
            shape[i].y = center.y + y
            if not borders():
                shape = deepcopy(copyShape)
                break

    # > find full lines
    line = tileH - 1
    for row in range(tileH - 1, -1, -1):
        count = 0
        for i in range(tileW):
            if playMap[row][i]:
                count += 1
            playMap[line][i] = playMap[row][i]
        if count < tileW:
            line -= 1

    # > outline the rects in grid
    [pygame.draw.rect(game_sc, (40, 40, 40), ele, 1) for ele in grid]
    
    # > draw our shapes from our coordinates
    for i in range(4):
        shapesDraw.x = shape[i].x * tileDim
        shapesDraw.y = shape[i].y * tileDim
        pygame.draw.rect(game_sc, color, shapesDraw)

    # > draw playMap with other shapes
    for y, raw in enumerate(playMap):
        for x, col in enumerate(raw):
            if col:
                shapesDraw.x, shapesDraw.y = x * tileDim, y * tileDim
                pygame.draw.rect(game_sc, col, shapesDraw)

    pygame.display.flip()
    clock.tick()