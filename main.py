import pygame
import os

import multiplayer, singleplayer
import loadGame, pref
from fontloader import HEADING, VERSION, SINGLE, SINGLE_H, MULTI, MULTI_H, \
     ONLINE, ONLINE_H, LOAD, LOAD_H, ABOUT, ABOUT_H, DOCS, DOCS_H, PREF, PREF_H

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PyChess')

LOGO = pygame.image.load(os.path.join("images",
                                            "logo.png"))

pygame.display.set_icon(LOGO)

BACKGROUND = pygame.image.load(os.path.join("images",
                                            "background.jpg")).convert()
BACKGROUND2 = pygame.image.load(os.path.join("images",
                                            "background2.jpg")).convert()
BACKGROUND3 = pygame.image.load(os.path.join("images",
                                            "background3.jpg")).convert()
BACKGROUND4 = pygame.image.load(os.path.join("images",
                                            "background4.jpg")).convert()

single = (250, 140, 230, 40)
multi = (270, 200, 210, 40)
online = (355, 260, 115, 40)
load = (280, 320, 200, 40)
docs = (400, 450, 100, 40)
prefer = (0, 450, 215, 40)
about = (0, 400, 110, 40)

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
    
def showMain(cnt = 0, img = 0):
    if img == 0:
        win.blit(BACKGROUND, (0, 0))
    elif img == 1:
        win.blit(BACKGROUND2, (0, 0))
    elif img == 2:
        win.blit(BACKGROUND3, (0, 0))
    elif img == 3:
        win.blit(BACKGROUND4, (0, 0))
        
    if cnt > -1:
        s = pygame.Surface((500,500))
        s.set_alpha(cnt*5)
        s.fill((0,0,0))
        win.blit(s, (0,0))
        
    win.blit(HEADING, (85, 20))
    pygame.draw.line(win, (255, 255, 255), (90, 95), (130, 95), 5)
    pygame.draw.line(win, (255, 255, 255), (170, 95), (400, 95), 5)
    win.blit(VERSION, (340, 100))
      
    win.blit(SINGLE, (single[0], single[1]))
    win.blit(MULTI, (multi[0], multi[1]))
    win.blit(ONLINE, (online[0], online[1]))
    win.blit(LOAD, (load[0], load[1]))
    win.blit(PREF, (prefer[0], prefer[1]))
    win.blit(ABOUT, (about[0], about[1]))
    win.blit(DOCS, (docs[0], docs[1]))
    
running = True
cnt = -80
img = 0
showMain()
while running:
    clock.tick(20)
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
            #prefer
            elif prefer[0] < x < (prefer[0]+prefer[2]) and \
               prefer[1] < y < (prefer[1]+prefer[3]):
                pref.main(win)
            #about
            elif about[0] < x < (about[0]+about[2]) and \
               about[1] < y < (about[1]+about[3]):
                print("Coming soon")
            #docs
            elif docs[0] < x < (docs[0]+docs[2]) and \
               docs[1] < y < (docs[1]+docs[3]):
                print("Coming soon")
    if pref.LOAD[2]:
        cnt += 1
        if cnt < 54:
            showMain(cnt, img)
        else:
            if img < 3:
                img += 1
            else:
                img = 0
            showMain(0, img)
            cnt = -80
    else:
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
    # Pref
    elif prefer[0] < x < (prefer[0]+prefer[2]) and \
       prefer[1] < y < (prefer[1]+prefer[3]):
        win.blit(PREF_H, (prefer[0], prefer[1]))
    #about
    elif about[0] < x < (about[0]+about[2]) and \
       about[1] < y < (about[1]+about[3]):
        win.blit(ABOUT_H, (about[0], about[1]))
    #docs
    elif docs[0] < x < (docs[0]+docs[2]) and \
       docs[1] < y < (docs[1]+docs[3]):
        win.blit(DOCS_H, (docs[0], docs[1]))
    pygame.display.flip()
pygame.quit()
