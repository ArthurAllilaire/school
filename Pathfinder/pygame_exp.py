import pygame
import math

from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from pathfinder import grid


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


def drawGrid(size):
    """
    Size: (num cols, num rows) that need to be drawn
    Start at 20 go to 20 from the window width. divide that 
    """
    global WINDOW_HEIGHT, WINDOW_WIDTH
    space = [WINDOW_WIDTH-40, WINDOW_HEIGHT - 40]
    blockSize = math.floor(space[0] / size[0])
    for x in range(20, WINDOW_WIDTH-20, blockSize):
        for y in range(20, WINDOW_HEIGHT-20, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

            # Initialise pygame


def drawBlocked():
    """
    Based on what people highlight on the grid it will then be drawn as white and given to the back end as blocked
    """


pygame.init()

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.fill(BLACK)


while True:
    # Set up the screen
    drawGrid(grid.shape)

    drawBlocked()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN:
            print(event)

    pygame.display.update()
