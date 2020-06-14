'''
This file is a part of My-PyChess application.
In this file, we manage the online menu which is called when user clicks
online button on main menu.

Level of development = STABLE
'''

import pygame
from loader import ONLINEMENU as ONLINE, FONT
from tools.utils import rounded_rect
from tools.pyBox import TextBox

# This shows the screen
def showScreen(win, pg):
    win.fill((0, 0, 0))
    
    rounded_rect(win, (255, 255, 255), (120, 10, 260, 70), 20, 4)
    rounded_rect(win, (255, 255, 255), (20, 90, 460, 400), 14, 4)
    win.blit(ONLINE.HEAD, (175, 15))
    
    if pg:
        for cnt, i in enumerate(ONLINE.TEXT):
            win.blit(i, (40, 100 + cnt*18))
            
        rounded_rect(win, (255, 255, 255), (150, 245, 80, 20), 3, 2)
        win.blit(ONLINE.CLICK, (150, 245))
        
        rounded_rect(win, (255, 255, 255), (300, 150, 110, 30), 10, 3)
        win.blit(ONLINE.CONNECT, (300, 150))
            
    else:
        for cnt, i in enumerate(ONLINE.TEXT2):
            win.blit(i, (40, 100 + cnt*17))
        rounded_rect(win, (255, 255, 255), (130, 455, 70, 23), 4, 2)
        win.blit(ONLINE.BACK, (130, 457))

# This is the main function, called from main menu
def main(win):
    clock = pygame.time.Clock()
    pg = True
    
    box = TextBox(FONT, (0, 0, 0), (65, 150, 200, 35))
    while True:
        clock.tick(24)
        showScreen(win, pg)
        if pg:
            pygame.draw.rect(win, (255, 255, 255), (63, 148, 204, 39))
            box.draw(win)
            
        for event in pygame.event.get():
            if pg:
                box.push(event)
                
            if event.type == pygame.QUIT:
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pg:
                    if 150 < x < 230 and 245 < y < 265:
                        pg = False
                        
                    if 300 < x < 410 and 150 < y < 180:
                        return box.text
                else:
                    if 130 < x < 200 and 455 < y < 478:
                        pg = True           
        pygame.display.update()