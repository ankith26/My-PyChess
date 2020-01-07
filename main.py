import pygame

import multiplayer, singleplayer

import loadGame
import os
from fontloader import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PyChess')

BACKGROUND = pygame.image.load(os.path.join("images",
                                            "background.jpg")).convert()

single = (250, 140, 230, 40)
multi = (270, 200, 210, 40)
online = (355, 260, 115, 40)
load = (280, 320, 200, 40)
about = (390, 450, 110, 40)
docs = (0, 450, 90, 40)


def pieceGen(isWhite):
    if isWhite:
        Board = []
        for i in range(8):
            Board.append([i+1, 7, "pawn"])
        Board.append([1, 8, "rook"])
        Board.append([8, 8, "rook"])
        Board.append([2, 8, "knight"])
        Board.append([7, 8, "knight"])
        Board.append([3, 8, "bishop"])
        Board.append([6, 8, "bishop"])
        Board.append([4, 8, "queen"])
        Board.append([5, 8, "king"])
        return Board
    else:
        Board = []
        for i in range(8):
            Board.append([i+1, 2, "pawn"])
        Board.append([1, 1, "rook"])
        Board.append([8, 1, "rook"])
        Board.append([2, 1, "knight"])
        Board.append([7, 1, "knight"])
        Board.append([3, 1, "bishop"])
        Board.append([6, 1, "bishop"])
        Board.append([4, 1, "queen"])
        Board.append([5, 1, "king"])
        return Board
    
def showMain():
    WHITE = (255,255,255)

    win.blit(BACKGROUND, (0, 0))
    win.blit(HEADING,(85,20))
    win.blit(VERSION,(340,100))
    
    win.blit(DOCS,(docs[0], docs[1]))
    win.blit(ABOUT, (about[0], about[1]))   
    win.blit(SINGLE, (single[0], single[1]))
    win.blit(MULTI, (multi[0], multi[1]))
    win.blit(ONLINE, (online[0], online[1]))
    win.blit(LOAD, (load[0], load[1]))
    
running = True
while running:
    pygame.display.flip()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            #singleplayer
            if single[0] < x < (single[0]+single[2]) and \
               single[1] < y < (single[1]+single[3]):
                running = singleplayer.main(win, True,
                                           pieceGen(True),
                                           pieceGen(False),
                                           [False for _ in range(6)])
            #multiplayer
            elif multi[0] < x < (multi[0]+multi[2]) and \
               multi[1] < y < (multi[1]+multi[3]):
                running = multiplayer.main(win, True,
                                           pieceGen(True),
                                           pieceGen(False),
                                           [False for _ in range(6)])
            #online
            elif online[0] < x < (online[0]+online[2]) and \
               online[1] < y < (online[1]+online[3]):
                print("Coming soon")
            #Load Game
            elif load[0] < x < (load[0]+load[2]) and \
               load[1] < y < (load[1]+load[3]): 
                var = loadGame.showMain(win)
                if var != None:
                    if var[0] == "multi":
                        running = multiplayer.main(win, var[1], var[2],
                                                   var[3], var[4])
                    if var[0] == "single":
                        running = singleplayer.main(win, var[1], var[2],
                                                   var[3], var[4])
            #docs
            elif docs[0] < x < (docs[0]+docs[2]) and \
               docs[1] < y < (docs[1]+docs[3]):
                print("Coming soon")
            #about
            elif about[0] < x < (about[0]+about[2]) and \
               about[1] < y < (about[1]+about[3]):
                print("Coming soon")
        showMain()
        x,y = pygame.mouse.get_pos() 
        #singleplayer
        if single[0] < x < (single[0]+single[2]) and \
           single[1] < y < (single[1]+single[3]):
            win.blit(SINGLE_H, (single[0], single[1]))
        #multiplayer
        elif multi[0] < x < (multi[0]+multi[2]) and \
           multi[1] < y < (multi[1]+multi[3]):
            win.blit(MULTI_H, (multi[0], multi[1]))
        #online
        elif online[0] < x < (online[0]+online[2]) and \
           online[1] < y < (online[1]+online[3]):
            win.blit(ONLINE_H, (online[0], online[1]))
        #Load Game
        elif load[0] < x < (load[0]+load[2]) and \
           load[1] < y < (load[1]+load[3]):
            win.blit(LOAD_H, (load[0], load[1]))
        #docs
        elif docs[0] < x < (docs[0]+docs[2]) and \
           docs[1] < y < (docs[1]+docs[3]):
            win.blit(DOCS_H, (docs[0], docs[1]))
        #about
        elif about[0] < x < (about[0]+about[2]) and \
           about[1] < y < (about[1]+about[3]):
            win.blit(ABOUT_H, (about[0], about[1]))
pygame.quit()
