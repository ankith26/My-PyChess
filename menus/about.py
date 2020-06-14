'''
This file is a part of My-PyChess application.
In this file, we manage the about menu which is called when user clicks
about button on main menu.

Level of development = STABLE
'''

import pygame
from loader import ABOUT
from tools.utils import rounded_rect

# This shows the screen
def showScreen(win):
    win.fill((0, 0, 0))
    rounded_rect(win, (255, 255, 255), (20, 10, 460, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)
    
    win.blit(ABOUT.HEAD, (30, 12))
    for cnt, i in enumerate(ABOUT.TEXT):
        win.blit(i, (20, 90 + cnt*18))
        
    pygame.display.update()

# This is the main function, called from main menu
def main(win):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 160 < x < 300 and 190 < y < 210:
                    stockfish.main(win)
                    return
        pygame.display.update()