import pygame
from myutils import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((460, 460))
pygame.display.set_caption('Chess')
running = True

wmove = True
x = y = -100
sel = [0, 0]
prevsel = [0, 0]

while running:
    clock.tick(24)
    drawboard(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 30<x<430 and 30<y<430:
                x = ((x - 30) // 50) + 1
                y = ((y - 30) // 50) + 1
                prevsel = sel
                sel = [x, y]
            else: sel = [0, 0]
            
    if wmove and sel != [0, 0]:
        for i in range(len(wBoard)):          
            if wBoard[i] != None and prevsel == wBoard[i][:2]:
                if isoccupied(sel[0], sel[1]) != "white":
                    ptype = getpiece("w", prevsel)
                    if sel in [i for i in availableMoves(ptype, prevsel)]:
                        if move("w", prevsel, sel): wmove = False
                        else: wmove = True
                        doroutine()
    elif sel != [0, 0]:
        for i in range(len(bBoard)):
            if bBoard[i] != None and prevsel == bBoard[i][:2]:
                if isoccupied(sel[0], sel[1]) != "black":
                    ptype = getpiece("b", prevsel)
                    if sel in [i for i in availableMoves(ptype, prevsel)]:
                        if move("b", prevsel, sel): wmove = True
                        else: wmove = False
                        doroutine()
    pygame.draw.rect(win, (255,255,0), ((x-1)*50+30, (y-1)*50+30, 50, 50))
    drawpieces(win)
    pygame.display.update()
pygame.quit()
