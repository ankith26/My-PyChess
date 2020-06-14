'''
This file is a part of My-PyChess application.

In this file, we give platform specific installation guide for installing
stockfish.
'''

import os.path
import platform

import pygame
from loader import STOCKFISH as SF, putLargeNum
from tools.pyFish import teststockfish

# This shows a popup on screen wether stockfish is configured or not.
def install(win, pth):
    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)
    win.blit(SF.LOADING, (100, 200))
    pygame.display.update()
    
    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)
    
    pygame.draw.rect(win, (255, 255, 255), (220, 270, 65, 20), 2)
    win.blit(SF.BACK, (220, 270))
    
    active = teststockfish(pth)
    if active:
        with open(os.path.join("res", "stockfish", "path.txt"), "w") as f:
            f.write(pth)
        for cnt, i in enumerate(SF.SUCCESS):
            win.blit(i, (120, 206 + cnt*17))
    else:
        for cnt, i in enumerate(SF.NOSUCCESS):
            win.blit(i, (130, 206 + cnt*17))
            
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 < event.pos[0] < 285 and 270 < event.pos[1] < 290:
                    return active
                
def prompt(win):
    pygame.draw.rect(win, (0, 0, 0), (110, 160, 280, 130))
    pygame.draw.rect(win, (255, 255, 255), (110, 160, 280, 130), 4)

    win.blit(SF.PROMPT[0], (130, 170))
    win.blit(SF.PROMPT[1], (130, 205))

    win.blit(SF.YES, (145, 240))
    win.blit(SF.NO, (305, 240))
    pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
    pygame.draw.rect(win, (255, 255, 255), (300, 240, 45, 28), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 200:
                        return True
                    elif 300 < event.pos[0] < 345:
                        return False

# This shows the installation guide screen
def showScreen(win, OS, pg):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (10, 10, 480, 480), 4)
    
    win.blit(SF.TEST, (50, 425))
    
    pygame.draw.rect(win, (255, 255, 255), (180, 450, 90, 30), 2)
    win.blit(SF.INSTALL, (187, 450))
    
    if OS == "Linux":
        win.blit(SF.LIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)
        
        if pg:
            putLargeNum(win, 1, (380, 15))
            for cnt, i in enumerate(SF.LIN_TEXT):
                win.blit(i, (20, 50 + cnt*18))
                
            pygame.draw.rect(win, (255, 255, 255), (210, 380, 80, 20), 2)
            win.blit(SF.CLICK, (210, 380))
               
        else:
            putLargeNum(win, 2, (380, 15))
            for cnt, i in enumerate(SF.LIN_TEXT2):
                win.blit(i, (20, 50 + cnt*18))
                
            pygame.draw.rect(win, (255, 255, 255), (420, 20, 65, 20), 2)
            win.blit(SF.BACK, (420, 20))
            
    elif OS == "Windows":
        win.blit(SF.WIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (400, 48), 3)
        
        for cnt, i in enumerate(SF.WIN_TEXT):
            win.blit(i, (20, 60 + cnt*18))
            
    elif OS == "Darwin":
        win.blit(SF.MAC_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (340, 48), 3)
        
        for cnt, i in enumerate(SF.MAC_TEXT):
            win.blit(i, (20, 60 + cnt*18))
    
    else:
        win.blit(SF.OTH_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)
        
        for cnt, i in enumerate(SF.OTH_TEXT):
            win.blit(i, (20, 50 + cnt*18))

# This is the main function, called by stockfish main-menu.
def main(win):
    OS = platform.system()
    pg = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, OS, pg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if OS == "Linux":
                    if 210 < x < 290 and 380 < y < 400 and pg:
                        pg = False
                    if 420 < x < 485 and 20 < y < 40 and not pg:
                        pg = True
                
                if 180 < x < 270 and 450 < y < 480:
                    if (OS == "Linux" and pg) or OS == "Darwin":
                        path = "stockfish"
                    else:
                        path = "res/stockfish/build/stockfish"
                    return install(win, path)             
        pygame.display.update()