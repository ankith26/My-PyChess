'''
This file is a part of My-PyChess application.
In this file, we define the general utility functions for online chess.
These are mostly gui related.

Level of development = STABLE
'''

import pygame

from chess.onlinelib.sockutils import *
from loader import ONLINE, putLargeNum, putNum

def showLoading(win, errcode=-1):
    pygame.draw.rect(win, (255, 255, 255), (100, 220, 300, 60))
    pygame.draw.rect(win, (0, 0, 0), (103, 223, 294, 54))
    
    if errcode == -1:
        win.blit(ONLINE.TRYCONN, (135, 240))
        pygame.display.update()
        return
    
    win.blit(ONLINE.ERR[errcode], (110, 240))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

# Show a popup message when user left, resigned or draw accepted.
def popup(win, typ):
    pygame.draw.rect(win, (0, 0, 0), (75, 190, 350, 120))
    pygame.draw.rect(win, (255, 255, 255), (75, 190, 350, 120), 4)
    
    if typ == "quit":
        win.blit(ONLINE.OPPQUIT, (100, 210))
    elif typ == "resign":
        win.blit(ONLINE.RESIGN, (77, 210))
    elif typ == "draw":
        win.blit(ONLINE.DRAWAGREED, (114, 210))
    
    win.blit(ONLINE.OK, (230, 260))
    pygame.draw.rect(win, (255, 255, 255), (230, 260, 40, 30), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 230 < event.pos[0] < 270:
                    if 260 < event.pos[1] < 290:
                        return

# It shows a popup message on the screen for draw. It can show two things,
# 1) Waiting for players input for game request
# 2) Waiting for other players input for game request
def request(win, key, sock=None):
    if sock is None:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.MSG2[0], (110, 175))
        win.blit(ONLINE.MSG2[1], (200, 175))
        win.blit(ONLINE.MSG2[2], (105, 200))
        putNum(win, key, (160, 175))

        win.blit(ONLINE.OK, (145, 240))
        win.blit(ONLINE.NO, (305, 240))
        pygame.draw.rect(win, (255, 255, 255), (140, 240, 50, 28), 2)
        pygame.draw.rect(win, (255, 255, 255), (300, 240, 50, 28), 2)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 240 < event.pos[1] < 270:
                        if 140 < event.pos[0] < 190:
                            return True
                        elif 300 < event.pos[0] < 350:
                            return False
    else:
        pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
        pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)

        win.blit(ONLINE.MSG1[0], (120, 210))
        win.blit(ONLINE.MSG1[1], (105, 235))
        win.blit(ONLINE.MSG1[2], (135, 260))

        pygame.display.flip()
        while True:
            if readable():
                msg = read()
                if msg == "close":
                    return None

                elif msg == "start":
                    write(sock, "ready")
                    return True

                elif msg == "nostart":
                    write(sock, "pass")
                    return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return None
                
# It shows a popup message on the screen for draw. It can show two things,
# 1) Waiting for players input for draw game
# 2) Waiting for other players input for draw game
def draw(win, sock=None):
    if sock is None:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.DRAW2[0], (120, 170))
        win.blit(ONLINE.DRAW2[1], (170, 195))

        win.blit(ONLINE.OK, (145, 240))
        win.blit(ONLINE.NO, (305, 240))
        pygame.draw.rect(win, (255, 255, 255), (140, 240, 50, 28), 2)
        pygame.draw.rect(win, (255, 255, 255), (300, 240, 50, 28), 2)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 240 < event.pos[1] < 270:
                        if 140 < event.pos[0] < 190:
                            return True
                        elif 300 < event.pos[0] < 350:
                            return False
    else:
        pygame.draw.rect(win, (0, 0, 0), (100, 220, 300, 60))
        pygame.draw.rect(win, (255, 255, 255), (100, 220, 300, 60), 4)

        win.blit(ONLINE.DRAW[0], (110, 225))
        win.blit(ONLINE.DRAW[1], (180, 250))

        pygame.display.flip()
        while True:
            if readable():
                msg = read()
                if msg == "close":
                    return True

                elif msg == "draw":
                    popup(win, msg)
                    write(sock, "end")
                    return True

                elif msg == "nodraw":
                    return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return True
                    
# Responsible for showing the online Lobby
def showLobby(win, key, playerlist):
    win.fill((0, 0, 0))
    
    win.blit(ONLINE.LOBBY, (100, 14))
    pygame.draw.rect(win, (255, 255, 255), (65, 10, 355, 68), 4)
    win.blit(ONLINE.LIST, (20, 75))
    win.blit(ONLINE.REFRESH, (270, 85))
    pygame.draw.line(win, (255, 255, 255), (20, 114), (190, 114), 3)
    pygame.draw.line(win, (255, 255, 255), (210, 114), (265, 114), 3)
    
    if not playerlist:
        win.blit(ONLINE.EMPTY, (25, 130))
    
    for cnt, player in enumerate(playerlist):
        pkey, stat = int(player[:4]), player[4]
        yCord = 120 + cnt * 30
        
        putLargeNum(win, cnt + 1, (20, yCord))
        win.blit(ONLINE.DOT, (36, yCord))
        win.blit(ONLINE.PLAYER, (52, yCord))
        putLargeNum(win, pkey, (132, yCord))
        if stat == "a":
            win.blit(ONLINE.ACTIVE, (200, yCord))
        elif stat == "b":
            win.blit(ONLINE.BUSY, (200, yCord))
        pygame.draw.rect(win, (255, 255, 255), (300, yCord + 2, 175, 26), 2)
        win.blit(ONLINE.REQ, (300, yCord))

    win.blit(ONLINE.YOUARE, (100, 430))
    pygame.draw.rect(win, (255, 255, 255), (250, 435, 158, 40), 3)
    win.blit(ONLINE.PLAYER, (260, 440))
    putLargeNum(win, key, (340, 440))

    pygame.display.update()