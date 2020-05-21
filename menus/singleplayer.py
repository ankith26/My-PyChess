'''
This file is a part of My-PyChess application.
In this file, we manage the single player menu which is called when user clicks
singleplayer button on main menu.
'''

import os
import random
import pygame
from loader import SINGLE, putLargeNum
from tools.utils import rounded_rect
from menus import stockfish

def showScreen(win, sel, sel2, lvl):
    win.fill((0, 0, 0))
    
    rounded_rect(win, (255, 255, 255), (70, 5, 340, 60), 15, 4)
    win.blit(SINGLE.HEAD, (100, 7))
        
    rounded_rect(win, (255, 255, 255), (10, 70, 480, 180), 12, 4)
    for cnt, i in enumerate(SINGLE.PARA1):
        y = 75 + cnt * 17
        win.blit(i, (20, y))
    win.blit(SINGLE.CHOOSE, (90, 160))
    win.blit(SINGLE.SELECT, (200, 150))
    pygame.draw.rect(win, (50, 100, 150), (200 + sel*50, 150, 50, 50), 3)
    
    rounded_rect(win, (255, 255, 255), (170, 210, 140, 30), 7, 3)
    win.blit(SINGLE.START, (170, 210))
    
    win.blit(SINGLE.OR, (220, 250))
    
    rounded_rect(win, (255, 255, 255), (10, 295, 480, 200), 12, 4)
    for cnt, i in enumerate(SINGLE.PARA2):
        y = 300 + cnt * 17
        win.blit(i, (20, y))
    win.blit(SINGLE.LEVEL, (30, 380))
    for i in range(9):
        pygame.draw.rect(win, (255, 255, 255), (110 + i*35, 380, 25, 30), 3)
        putLargeNum(win, i+1, (113 + i*35, 380))
    pygame.draw.rect(win, (50, 100, 150), (75 + lvl*35, 380, 25, 30), 3)
    
    win.blit(SINGLE.CHOOSE, (40, 440))
    win.blit(SINGLE.SELECT, (150, 430))
    pygame.draw.rect(win, (50, 100, 150), (150 + sel2*50, 430, 50, 50), 3)
    
    rounded_rect(win, (255, 255, 255), (320, 440, 140, 30), 7, 3)
    win.blit(SINGLE.START, (320, 440))

def main(win):
    sel = sel2 = 0
    lvl = 1
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, sel, sel2, lvl)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 160 < y < 210 and 200 < x < 350:
                    sel = (x // 50) - 4
                    
                if 430 < y < 480 and 150 < x < 300:
                    sel2 = (x // 50) - 3
                        
                if 380 < y < 410:
                    for i in range(9):
                        if 110 + i*35 < x < 135 + i*35:
                            lvl = i + 1
                        
                if 170 < x < 310 and 220 < y < 250:
                    if sel == 2:
                        return True, random.randint(0, 1)
                    else:
                        return True, sel
                    
                if 320 < x < 460 and 440 < y < 470:
                    pth = os.path.join("res", "stockfish", "path.txt")
                    if os.path.exists(pth):
                        if sel2 == 2:
                            return False, random.randint(0, 1), lvl
                        else:
                            return False, sel2, lvl
                    else:
                        if prompt(win):
                            stockfish.main(win)
                        return None
            pygame.display.update()

def prompt(win):
    rounded_rect(win, (255, 255, 255), (100, 200, 300, 100), 20, 4)
    
    for cnt, i in enumerate(SINGLE.CONFIG):
        win.blit(i, (110, 206 + cnt*18))
    
    win.blit(SINGLE.OK, (160, 270))
    pygame.draw.rect(win, (255, 255, 255), (160, 270, 25, 20), 3)
    win.blit(SINGLE.NOTNOW, (250, 270))
    pygame.draw.rect(win, (255, 255, 255), (250, 270, 70, 20), 3)
    
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 270 < event.pos[1] < 290:
                    if 160 < event.pos[0] < 185:
                        return True
                    if 250 < event.pos[0] < 320:
                        return False
