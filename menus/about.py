'''
This file is a part of My-PyChess application.
In this file, we manage the about menu which is called when user clicks
about button on main menu.
'''

import pygame
from loader import ABOUT
from menus import stockfish

def showScreen(win):
    win.fill((0, 0, 0))
    
    win.blit(ABOUT.HEAD, (30, 12))
    pygame.draw.rect(win, (255, 255, 255), (20, 10, 460, 60), 4)
    
    win.blit(ABOUT.SOON, (25, 90))
    pygame.draw.rect(win, (255, 255, 255), (10, 80, 480, 410), 4)
    
    win.blit(ABOUT.STOCKFIG, (15, 160))
    win.blit(ABOUT.CLICK, (160, 190))
    pygame.draw.rect(win, (255, 255, 255), (160, 190, 140, 30), 3)

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