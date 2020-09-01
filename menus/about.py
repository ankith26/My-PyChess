'''
This file is a part of My-PyChess application.
In this file, we manage the about menu which is called when user clicks
about button on main menu.
'''

import pygame
from tools.loader import ABOUT, BACK
from tools.utils import rounded_rect

# This shows the screen
def showScreen(win):
    win.fill((0, 0, 0))
    rounded_rect(win, (255, 255, 255), (70, 10, 360, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)

    win.blit(ABOUT.HEAD, (74, 12))
    for cnt, i in enumerate(ABOUT.TEXT):
        win.blit(i, (20, 90 + cnt*18))

    win.blit(BACK, (460, 0))
    pygame.display.update()

# This is the main function, called from main menu
def main(win):
    showScreen(win)
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    return 1
