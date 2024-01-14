'''
This file is a part of My-PyChess application.
In this file, we define the gui functions for online chess.
'''

import datetime
import pygame

from chess.onlinelib.sockutils import *
from tools.loader import ONLINE, BACK, putLargeNum, putNum

# Shows a small popup when user requests game with wrong player.
def showUpdateList(win):
    pygame.draw.rect(win, (0, 0, 0), (110, 220, 280, 60))
    pygame.draw.rect(win, (255, 255, 255), (110, 220, 280, 60), 4)
    
    win.blit(ONLINE.ERRCONN, (120, 240))
    
    pygame.display.update()
    for _ in range(50):
        pygame.time.delay(50)
        for _ in pygame.event.get():
            pass

# This shows screen just before the lobby, displays error messages too.
def showLoading(win, errcode=0):
    pygame.draw.rect(win, (0, 0, 0), (100, 220, 300, 80))
    pygame.draw.rect(win, (255, 255, 255), (100, 220, 300, 80), 4)
    
    win.blit(ONLINE.ERR[errcode], (115, 240))
    if errcode == 0:
        pygame.display.update()
        return
    
    pygame.draw.rect(win, (255, 255, 255), (220, 270, 65, 20), 2)
    win.blit(ONLINE.GOBACK, (220, 270))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 < event.pos[0] < 285 and 270 < event.pos[1] < 290:
                    return

# Show a popup message when user left, resigned or draw accepted.
def popup(win, sock, typ):
    pygame.draw.rect(win, (0, 0, 0), (130, 220, 240, 80))
    pygame.draw.rect(win, (255, 255, 255), (130, 220, 240, 80), 4)

    win.blit(ONLINE.POPUP[typ], (145, 240))
    
    pygame.draw.rect(win, (255, 255, 255), (220, 270, 65, 20), 2)
    win.blit(ONLINE.GOBACK, (220, 270))
    pygame.display.update()
    
    ret = 3
    while True:
        if readable() and read() == "close":
            write(sock, "quit")
            ret = 2
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 < event.pos[0] < 285 and 270 < event.pos[1] < 290:
                    write(sock, "end")
                    return ret

# It shows a popup message on the screen. It can show two things,
# 1) Waiting for opponent input for game request (when key is None)
# 2) Waiting for player input for game request (when key is not None)
def request(win, sock, key=None):
    if key is None:
        pygame.draw.rect(win, (0, 0, 0), (100, 210, 300, 100))
        pygame.draw.rect(win, (255, 255, 255), (100, 210, 300, 100), 4)

        win.blit(ONLINE.WAITING1[0], (120, 220))
        win.blit(ONLINE.REQUEST1[1], (105, 245))
        win.blit(ONLINE.REQUEST1[2], (135, 270))
                    
    else:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.REQUEST2[0], (110, 175))
        win.blit(ONLINE.REQUEST2[1], (200, 175))
        win.blit(ONLINE.REQUEST2[2], (105, 200))
        putNum(win, key, (160, 175))

        win.blit(ONLINE.OK, (145, 240))
        win.blit(ONLINE.NO, (305, 240))
        pygame.draw.rect(win, (255, 255, 255), (140, 240, 50, 28), 2)
        pygame.draw.rect(win, (255, 255, 255), (300, 240, 50, 28), 2)
        
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if key is None and event.type == pygame.QUIT:
                write(sock, "quit")
                return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if key is None:
                    if 460 < event.pos[0] < 500 and 0 < event.pos[1] < 50:
                        write(sock, "quit")
                        return 1
                    
                elif 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 190:
                        return 4
                    elif 300 < event.pos[0] < 350:
                        return 3
                
        if readable():
            msg = read()
            if msg == "close":
                return 2
            
            if msg == "quit":
                return 3
            
            if key is None:
                if msg == "nostart":
                    write(sock, "pass")
                    return 3

                if msg == "start":
                    write(sock, "ready")
                    return 4
                
# It shows a popup message on the screen. It can show two things,
# 1) Waiting for other players input for draw game (when requester is True)
# 2) Waiting for players input for draw game (when requester is False)
def waiting(win, sock):
    pygame.draw.rect(win, (0, 0, 0), (100, 210, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 210, 300, 100), 4)

    win.blit(ONLINE.WAITING1[0], (120, 220))
    while True:
        if readable():
            msg = read()
            if msg == "nostart":
                write(sock, "pass")
                return 3

            if msg == "start":
                write(sock, "ready")
                return 4
            if msg.startswith("xr"):
                write(sock, "ready")
                return 4
    
    
def draw(win, sock, requester=True):
    if not requester:
        pygame.draw.rect(win, (0, 0, 0), (100, 220, 300, 60))
        pygame.draw.rect(win, (255, 255, 255), (100, 220, 300, 60), 4)

        win.blit(ONLINE.DRAW1[0], (110, 225))
        win.blit(ONLINE.DRAW1[1], (180, 250))
        
    else:
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
            if requester:
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 190:
                        write(sock, "draw")
                        return 3
                    
                    elif 300 < event.pos[0] < 350:
                        write(sock, "nodraw")
                        return 4
                
        if readable():
            msg = read()
            if msg == "close":
                return 2
            if msg == "win":
                return popup(win, sock, msg)
            if msg == "quit":
                return popup(win, sock, msg)
            
            if requester:
                if msg == "draw":
                    return popup(win, sock, msg)
                if msg == "nodraw":
                    return 4
                
def rematch(win, sock, requester=True):
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
                        write(sock, "acc")
                        return 3  
                    elif 300 < event.pos[0] < 350:
                        write(sock, "dec")
                        return 4    
            if readable():
                msg = read()
                print(f'{msg}__')
def draw_win(win, sock, requester=True):
    if requester:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.WIN2[0], (225, 195))

        win.blit(ONLINE.OK, (240, 240))
        pygame.draw.rect(win, (255, 255, 255), (235, 240, 50, 28), 2)
        
    else:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.WIN1[0], (225, 195))

        win.blit(ONLINE.OK, (240, 240))
        pygame.draw.rect(win, (255, 255, 255), (235, 240, 50, 28), 2)
        
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if requester:
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 240 < event.pos[1] < 270:
                        if 240 < event.pos[0] < 290:
                            write(sock, "win")
                            return 3 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 240 < event.pos[0] < 290:
                        write(sock, "lose")
                        return 3  
                    elif 300 < event.pos[0] < 350:
                        write(sock, "nodraw")
                        return 4              
        if readable():
            msg = read()
            if msg == "close":
                return 2
            if msg == "win":
                return popup(win, sock, msg)
            if msg == "quit":
                return popup(win, sock, msg)
            
            if requester:
                if msg == "draw":
                    return popup(win, sock, msg)
                if msg == "nodraw":
                    return 4                    
# Responsible for showing the online Lobby
def showLobby(win, key, playerlist):
    win.fill((0, 0, 0))
    
    win.blit(ONLINE.LOBBY, (100, 14))
    pygame.draw.rect(win, (255, 255, 255), (65, 10, 355, 68), 4)
    win.blit(BACK, (460, 0))
    win.blit(ONLINE.LIST, (20, 75))
    win.blit(ONLINE.REFRESH, (270, 85))
    win.blit(ONLINE.HISTORY, (330, 85))
    pygame.draw.line(win, (255, 255, 255), (20, 114), (190, 114), 3)
    pygame.draw.line(win, (255, 255, 255), (210, 114), (265, 114), 3)
    
    if not playerlist:
        win.blit(ONLINE.EMPTY, (25, 130))
    
    # TODO: Hien thi so diem
    for cnt, player in enumerate(playerlist):
        pkey, stat, elo = int(player[:4]), player[4], player[5:]
        yCord = 120 + cnt * 30
        
        putLargeNum(win, cnt + 1, (20, yCord))
        win.blit(ONLINE.DOT, (36, yCord))
        win.blit(ONLINE.PLAYER, (52, yCord))
        putLargeNum(win, pkey, (132, yCord))
        if stat == "a":
            win.blit(ONLINE.ACTIVE, (200, yCord))
        elif stat == "b":
            win.blit(ONLINE.BUSY, (200, yCord))
        pygame.draw.rect(win, (255, 255, 255), (350, yCord + 2, 120, 26), 2)
        putLargeNum(win, elo, (300, yCord))
        win.blit(ONLINE.REQ, (360, yCord))

    win.blit(ONLINE.FIND_MATCH, (200, 450))
    # win.blit(ONLINE.YOUARE, (100, 430))
    # pygame.draw.rect(win, (255, 255, 255), (250, 435, 158, 40), 3)
    # win.blit(ONLINE.PLAYER, (260, 440))
    # putLargeNum(win, key, (340, 440))
    pygame.display.update()
    
def showHistory(win, key, history):
    win.fill((0, 0, 0))
    
    win.blit(ONLINE.HISTORY_TITLED, (140, 14))
    pygame.draw.rect(win, (255, 255, 255), (65, 10, 355, 68), 4)
    win.blit(BACK, (460, 0))
    if not history:
        win.blit(ONLINE.EMPTY_HISTORY, (25, 130))
    for cnt, his in enumerate(history):
        parts = his.split()
        username = parts[0]
        time = parts[1]
        status = parts[2]
        yCord = 120 + cnt * 30
        
        # win.blit(ONLINE.DOT, (20, yCord))
        # win.blit(ONLINE.PLAYER, (52, yCord))
        putLargeNum(win, username, (20, yCord))
        if status == '1':
            win.blit(ONLINE.WIN_STATUS, (110, yCord))
        elif status == "0":
            win.blit(ONLINE.LOSE_STATUS, (110, yCord))
        year, month, day, hour, minute = map(int, time.split('-'))
        output_str = '{:02d}-{:02d}-{} {:02d}:{:02d}'.format(day, month, year, hour, minute)
        putLargeNum(win, output_str, (230, yCord))
    pygame.display.update()
    