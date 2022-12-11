import pygame

# > need to create tile dimensions and size
tileW, tileH = 10, 20
tileDim = 45

GAME_RES = tileW * tileDim, tileH * tileDim
gameFrames = 60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

# > need to create a grid for the game. Can do this with two dimensional array
# > each element is a rect
grid = [pygame.Rect(x * tileDim, y * tileDim, tileDim, tileDim) for x in range(tileW) for y in range(tileH)]

while True:
    game_sc.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # > outline the rects in grid
    [pygame.draw.rect(game_sc, (40, 40, 40), ele, 1) for ele in grid]

    pygame.display.flip()
    clock.tick()