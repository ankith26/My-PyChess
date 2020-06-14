'''
This file is a part of My-PyChess application.
In this file, we manage the stockfish menu.

This is called from either about menu or singleplayer menu
'''

import os

import pygame
from tools.utils import rounded_rect
from menus.stockfish.guide import main as guideMain, SF

# This shows the screen
def showScreen(win, configured):
    win.fill((0, 0, 0))
    
    rounded_rect(win, (255, 255, 255), (40, 10, 395, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)
    win.blit(SF.HEAD, (50, 12))
    for cnt, i in enumerate(SF.TEXT):
        win.blit(i, (15, 90 + cnt*18))
    
    rounded_rect(win, (255, 255, 255), (120, 320, 250, 30), 6, 3)
    win.blit(SF.CONFIG, (120, 320))
    
    if configured:
        for cnt, i in enumerate(SF.CONFIGURED):
            win.blit(i, (15, 360 + cnt*18))
    else:
        for cnt, i in enumerate(SF.NONCONFIGURED):
            win.blit(i, (15, 360 + cnt*18))

# This is the main function, called by main menu
def main(win):
    pth = os.path.join("res", "stockfish", "path.txt")
    configured = os.path.exists(pth)
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, configured)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 120 < x < 370 and 320 < y < 350:
                    if configured:
                        os.remove(pth)
                        
                    if guideMain(win):
                        return True
                    else:
                        configured = os.path.exists(pth)
                                       
        pygame.display.update()