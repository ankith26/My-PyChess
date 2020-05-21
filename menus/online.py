'''
This file is a part of My-PyChess application.
In this file, we manage the online menu which is called when user clicks
online button on main menu.
'''

import os
import pygame
from loader import ONLINEMENU as ONLINE
from tools.utils import rounded_rect
from tools.pyBox import TextBox

def showScreen(win, pg):
    win.fill((0, 0, 0))
    
    rounded_rect(win, (255, 255, 255), (120, 10, 260, 70), 20, 4)
    rounded_rect(win, (255, 255, 255), (20, 90, 460, 400), 14, 4)
    win.blit(ONLINE.HEAD, (175, 15))
    
    if pg:
        for cnt, i in enumerate(ONLINE.TEXT):
            win.blit(i, (40, 100 + cnt*17))
            
        rounded_rect(win, (255, 255, 255), (150, 235, 80, 20), 3, 2)
        win.blit(ONLINE.CLICK, (150, 235))
        
        rounded_rect(win, (255, 255, 255), (300, 150, 110, 30), 10, 3)
        win.blit(ONLINE.CONNECT, (300, 150))
            
    else:
        for cnt, i in enumerate(ONLINE.TEXT2):
            win.blit(i, (40, 100 + cnt*17))
        rounded_rect(win, (255, 255, 255), (130, 455, 70, 23), 4, 2)
        win.blit(ONLINE.BACK, (130, 457))

def main(win):
    clock = pygame.time.Clock()
    pg = True
    box = TextBox(os.path.join("res", "Asimov.ttf"), (0, 0, 0), (65, 150, 200, 35))
    while True:
        clock.tick(24)
        showScreen(win, pg)
        for event in pygame.event.get():
            if pg:
                box.push(event)
                
            if event.type == pygame.QUIT:
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pg:
                    if 150 < x < 230 and 235 < y < 255:
                        pg = False
                        
                    if 300 < x < 410 and 150 < y < 180:
                        return box.text
                else:
                    if 130 < x < 200 and 455 < y < 478:
                        pg = True
                    pass
        if pg:
            pygame.draw.rect(win, (255, 255, 255), (63, 148, 204, 39))
            box.draw(win)            
        pygame.display.update()