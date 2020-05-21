'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for online section of this
application.
'''

import queue
import socket
import threading

from loader import ONLINE, putLargeNum, putNum
from chess.lib import *

q = queue.Queue()

# Define a background thread that continuously runs and gets messages from
# server, formats them and puts them into a Queue.
def bgThread(sock):
    while True:
        try:
            msg = sock.recv(8).decode("utf-8")
            if msg:
                q.put(msg.strip())
            else:
                return
        except:
            return

# A function to message the server, this is used instead of socket.send()
# beacause it buffers the message and does not raise exception if message
# could not be sent
def write(sock, msg):
    val = msg + (" " * (8 - len(msg)))
    try:
        sock.send(val.encode("utf-8"))
    except:
        pass

# A function to Query the server for number of people online, returns a list
# of players connected to server if all went well, else None.
def getPlayers(sock):
    write(sock, "pStat")
    msg = q.get()

    if msg.startswith("enum"):
        data = []
        for i in range(int(msg[-1])):
            newmsg = q.get()
            if newmsg == "close":
                return None
            else:
                data.append(newmsg)
        return tuple(data)
    else:
        return None

# Responsible for showing the online Lobby
def showMain(win, key, playerlist):
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

# It shows a popup message on the screen.
# It can show two things, 1) Waiting for players input and 2) Waiting for
# other players input
def popup(win, key, sock=None):
    if sock is None:
        pygame.draw.rect(win, (0, 0, 0), (100, 160, 300, 130))
        pygame.draw.rect(win, (255, 255, 255), (100, 160, 300, 130), 4)

        win.blit(ONLINE.MSG2[0], (110, 170))
        win.blit(ONLINE.MSG2[1], (200, 170))
        win.blit(ONLINE.MSG2[2], (105, 190))
        putNum(win, key, (160, 170))

        win.blit(ONLINE.YES, (145, 240))
        win.blit(ONLINE.NO, (305, 240))
        pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
        pygame.draw.rect(win, (255, 255, 255), (300, 240, 50, 28), 2)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 240 < event.pos[1] < 270:
                        if 140 < event.pos[0] < 200:
                            return True
                        elif 300 < event.pos[0] < 350:
                            return False
    else:
        pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
        pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)

        win.blit(ONLINE.MSG1[0], (120, 210))
        win.blit(ONLINE.MSG1[1], (110, 235))
        win.blit(ONLINE.MSG1[2], (140, 260))

        pygame.display.flip()
        while True:
            if not q.empty():
                msg = q.get()
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

# This is a null menu, it does not do anything, just waits for user to exit.
# This keeps the pygame window responsive while nothing is going on.
def nullMenu(win):
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
def oppQuit(win):
    pygame.draw.rect(win, (0, 0, 0), (70, 180, 360, 140))
    pygame.draw.rect(win, (255, 255, 255), (70, 180, 360, 140), 4)

    win.blit(ONLINE.MSG3[0], (80, 200))
    win.blit(ONLINE.MSG3[1], (100, 220))
    
    win.blit(ONLINE.OK, (230, 260))
    pygame.draw.rect(win, (255, 255, 255), (230, 260, 40, 30), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 230 < event.pos[0] < 270:
                    if 260 < event.pos[1] < 290:
                        return

# This handles the online lobby. To display the window, it calls showmain()
# and does event handling and other important stuff.
def menu(win, sock, key, LOAD):
    clock = pygame.time.Clock()

    playerList = getPlayers(sock)
    if playerList is not None:
        showMain(win, key, playerList)
    else:
        return

    while True:
        clock.tick(10)
        if not q.empty():
            msg = q.get()
            if msg == "close":
                return

            elif msg.startswith("rg"):
                if popup(win, msg[2:]):
                    write(sock, "gmOk" + msg[2:])
                    chess(win, sock, 1, LOAD)
                    return
                else:
                    write(sock, "gmNo" + msg[2:])
                    showMain(win, key, playerList)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 270 < x < 302 and 85 < y < 117:
                    playerList = getPlayers(sock)
                    if playerList is not None:
                        showMain(win, key, playerList)
                    else:
                        return
                if 300 < x < 475:
                    for i in range(len(playerList)):
                        if 122 + 30 * i < y < 148 + 30 * i:
                            write(sock, "rg" + str(playerList[i][:4]))
                            newMsg = q.get()
                            if newMsg == "msgOk":
                                stat = popup(win, None, sock)
                                if stat is None:
                                    return
                                elif stat:
                                    chess(win, sock, 0, LOAD)
                                    return
                                else:
                                    showMain(win, key, playerList)

                            elif newMsg.startswith("err"):
                                playerList = getPlayers(sock)
                                if playerList is not None:
                                    showMain(win, key, playerList)
                                else:
                                    return
                            else:
                                write(sock, "quit")
                                return

# This is called when user enters chess match, handles chess.
def chess(win, sock, player, LOAD):
    side, board, flags = convertMoves("")

    clock = pygame.time.Clock()
    sel = [0, 0]
    prevsel = [0, 0]

    FLIP = LOAD[1] and player
    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                write(sock, "quit")
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if FLIP:
                        x, y = 9 - x, 9 - y
                    prevsel = sel
                    sel = [x, y]

        showScreen(win, side, board, flags, sel, LOAD, player, True)
        if not q.empty():
            msg = q.get()
            if msg == "close":
                return

            elif msg == "quit":
                write(sock, "quit")
                oppQuit(win)
                return

            if side != player:
                fro, to, promote = decode(msg)
                if isValidMove(side, board, flags, fro, to):
                    animate(win, side, board, fro, to, FLIP)
                    board = move(side, board, fro, to, promote)
                    flags = updateFlags(side, board, fro, to, flags[0])
                    sel = [0, 0]
                    side = flip(side)
                else:
                    write(sock, "quit")
                    return

        if side == player and isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, player, board, prevsel, sel)
            write(sock, encode(prevsel, sel, promote))
            animate(win, player, board, prevsel, sel, FLIP)
            board = move(player, board, prevsel, sel, promote)
            flags = updateFlags(player, board, prevsel, sel, flags[0])
            side = flip(side)

# This is a main function that controls all other functions, socket initialisation
# and the screen that appears just after online menu but just before online lobby.
def main(win, addr, LOAD):
    if addr is None:
        return

    win.fill((0, 0, 0))
    win.blit(ONLINE.TRYCONN, (0, 0))
    pygame.display.update()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((addr, 26104))
    except:
        win.blit(ONLINE.ERRCONN, (0, 40))
        nullMenu(win)
        return

    threading.Thread(target=bgThread, args=(sock,)).start()
    write(sock, "v3.0.0")
    msg = q.get()

    if msg == "errVer":
        win.blit(ONLINE.ERRVER, (0, 40))
        nullMenu(win)
    elif msg == "errBusy":
        win.blit(ONLINE.ERRBUSY, (0, 40))
        nullMenu(win)
    elif msg.startswith("GTag"):
        key = int(msg[4:])
        menu(win, sock, key, LOAD)
        
        while not q.empty():
            q.get()
    sock.close()
