'''
This file is a part of My-PyChess application.

In this file, we give platform specific installation guide for installing
stockfish.
'''

import os
import platform
import pygame
from loader import INSTALL as INST, putLargeNum
from tools.pyFish import teststockfish

def popup(win, pth):
    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)
    win.blit(INST.LOADING, (100, 200))
    pygame.display.update()
    
    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)
    
    pygame.draw.rect(win, (255, 255, 255), (220, 270, 65, 20), 2)
    win.blit(INST.BACK, (220, 270))
    
    active = teststockfish(pth)
    if active:
        with open(os.path.join("res", "stockfish", "path.txt"), "w") as f:
            f.write(pth)
        for cnt, i in enumerate(INST.SUCCESS):
            win.blit(i, (120, 206 + cnt*17))
    else:
        for cnt, i in enumerate(INST.NOSUCCESS):
            win.blit(i, (130, 206 + cnt*17))
            
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 < event.pos[0] < 285 and 270 < event.pos[1] < 290:
                    return active

def showScreen(win, OS, pg):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (10, 10, 480, 480), 4)
    
    win.blit(INST.TEST, (20, 425))
    pygame.draw.rect(win, (255, 255, 255), (160, 450, 140, 30), 2)
    win.blit(INST.INSTALL, (160, 450))       
    
    if OS == "Linux":
        win.blit(INST.LIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)
        
        if pg:
            putLargeNum(win, 1, (380, 15))
            for cnt, i in enumerate(INST.LIN_TEXT):
                win.blit(i, (20, 50 + cnt*18))
                
            pygame.draw.rect(win, (255, 255, 255), (235, 300, 80, 20), 2)
            win.blit(INST.CLICK, (235, 300))
               
        else:
            putLargeNum(win, 2, (380, 15))
            for cnt, i in enumerate(INST.LIN_TEXT2):
                win.blit(i, (20, 50 + cnt*18))
                
            pygame.draw.rect(win, (255, 255, 255), (420, 20, 65, 20), 2)
            win.blit(INST.BACK, (420, 20))
            
    elif OS == "Windows":
        win.blit(INST.WIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (400, 48), 3)
        
        for cnt, i in enumerate(INST.WIN_TEXT):
            win.blit(i, (20, 60 + cnt*18))
            
    elif OS == "Darwin":
        win.blit(INST.MAC_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (340, 48), 3)
        
        for cnt, i in enumerate(INST.MAC_TEXT):
            win.blit(i, (20, 60 + cnt*18))
    
    else:
        win.blit(INST.OTH_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)
        
        for cnt, i in enumerate(INST.OTH_TEXT):
            win.blit(i, (20, 50 + cnt*18))

def main(win):
    OS = platform.system()
    pg = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, OS, pg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if OS == "Linux":
                    if 235 < x < 315 and 300 < y < 320 and pg:
                        pg = False
                    if 420 < x < 485 and 20 < y < 40 and not pg:
                        pg = True
                
                if 160 < x < 300 and 450 < y < 480:
                    if (OS == "Linux" and pg) or OS == "Darwin":
                        path = "stockfish"
                    else:
                        path = "res/stockfish/build/stockfish"
                    return popup(win, path)             
        pygame.display.update()