'''
This file is a part of My-PyChess application.
In this file, we define the main functions for online chess, and aggregate
other functions for importing from online.py
'''
from chess.lib import *
from chess.onlinelib.sockutils import getHistory
from chess.onlinelib.utils import (
    bgThread,
    read,
    readable,
    flush,
    showHistory,
    waiting,
    write,
    getPlayers,
    showUpdateList,
    showLoading,
    popup,
    request,
    draw,
    draw_win,
    rematch,
    showLobby,
)

# This handles the online lobby. To display the window, it calls showLobby()
# and does event handling, socket handling and other important stuff.
def lobby(win, sock, key, load):
    clock = pygame.time.Clock()
    playerList = getPlayers(sock)
    while True:
        clock.tick(10)
        if playerList is None:
            return 2        
        showLobby(win, key, playerList)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    write(sock, "quit")
                    return 1

                if 270 < x < 300 and 85 < y < 115:
                    playerList = getPlayers(sock)
                    
                if 330 < x < 400 and 85 < y < 115:
                    history = getHistory(sock)
                    break_while = False

                    while True:
                        showHistory(win, key, history)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                write(sock, "quit")
                                return 0
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if 460 < x < 500 and 0 < y < 50:
                                    break_while = True
                                    break  # This breaks out of the for loop

                        if break_while:
                            break  # This breaks out of the while loop
                            
                        
                if 300 < x < 475:
                    for i in range(len(playerList)):
                        if 122 + 30 * i < y < 148 + 30 * i:
                            write(sock, "rg" + playerList[i][:4])
                            
                            msg = read()
                            if msg == "close":
                                return 2
                            
                            elif msg == "msgOk":
                                ret = request(win, sock)
                                if ret in [0, 1, 2]:
                                    return ret
                                elif ret == 4:
                                    newret = chess(win, sock, 0, load)
                                    if newret in [0, 1, 2]:
                                        return newret
                            
                            elif msg.startswith("err"):
                                showUpdateList(win)

                            playerList = getPlayers(sock)
                            break
                if 200 < x < 300 and 450 < y < 480:
                    write(sock,"find")
                    msg = read()
                    print(msg)
                    if msg == "msgOk":
                        ret = waiting(win, sock)
                        newret = chess(win, sock, 0, load)
                        if newret in [0, 1, 2]:
                            return newret

        if readable():
            msg = read()
            # print(f"{msg}") # Tai sao lai chay toi day
            if msg == "close":
                return 2
            elif msg.startswith("gr"):
                ret = request(win, sock, msg[2:])
                # write(sock, "ready")        
                ret = 4
                if ret == 4:
                    write(sock, "gmOk" + msg[2:])
                    newret = chess(win, sock, 1, load)
                    if newret in [0, 1, 2]:
                        return newret
                    
                else:
                    write(sock, "gmNo" + msg[2:])
                    if ret == 2:
                        return ret
                playerList = getPlayers(sock)
            elif msg.startswith("xr"):
                write(sock, "ready")
                write(sock, "gmOk" + msg[2:])
                newret = chess(win, sock, 1, load)
                if newret in [0, 1, 2]:
                    return newret
                playerList = getPlayers(sock)


def save_game_to_pgn(moves, filename="game.pgn"):
    with open(filename, "w") as pgn_file:
        pgn_file.write("[Event \"My Chess Game\"]\n")
        pgn_file.write("[Site \"Chess Board\"]\n")
        pgn_file.write("[Date \"2023.12.21\"]\n")
        pgn_file.write("[Round \"-\"]\n")
        pgn_file.write("[White \"Player 1\"]\n")
        pgn_file.write("[Black \"Player 2\"]\n")
        pgn_file.write("[Result \"*\"]\n\n")

        for i, move in enumerate(moves, start=1):
            if i % 2 == 1:
                pgn_file.write(f"{i // 2 + 1}. {move} ")
            else:
                pgn_file.write(move + " ")

        if len(moves) % 2 == 1:
            pgn_file.write("*")
        else:
            pgn_file.write("\n*\n")
# This is called when user enters chess match, handles online chess.
def chess(win, sock, player, load, pgn_filename="game.pgn"):
    start(win, load)

    side, board, flags = initBoardVars()
    moves = []  # List to store moves for PGN

    clock = pygame.time.Clock()
    sel = prevsel = [0, 0]
    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    write(sock, "end")
                    return 3

                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if load["flip"] and player:
                        x, y = 9 - x, 9 - y

                    if isOccupied(side, board, [x, y]) and side == player:
                        sound.play_click(load)

                    prevsel = sel
                    sel = [x, y]

                    if (side == player
                            and isValidMove(side, board, flags, prevsel, sel)):
                        promote = getPromote(win, player, board, prevsel, sel)
                        write(sock, "mov" + encode(prevsel, sel, promote))

                        animate(win, player, board, prevsel, sel, load, player)
                        side, board, flags = makeMove(
                            side, board, prevsel, sel, flags, promote)

                        # Save move to PGN
                        pgn_move = encode(prevsel, sel, promote)
                        moves.append(pgn_move)

                        # Save PGN after each move
                        save_game_to_pgn(moves, pgn_filename)

                    if isEnd(side, board, flags):
                        write(sock, "win")
                        # ret = rematch(win, sock)
                        ret = draw_win(win, sock)
                        return ret
                elif not isEnd(side, board, flags):
                    if 0 < x < 70 and 0 < y < 50:
                        write(sock, "draw?")
                        ret = draw(win, sock)
                        if ret in [0, 2, 3]:
                            return ret

                    if 400 < x < 500 and 450 < y < 500:
                        write(sock, "resign")
                        return 3

        showScreen(win, side, board, flags, sel, load, player, True)
        if readable():
            msg = read()
            if msg == "close":
                return 2
            elif msg == "quit" or msg == "resign":
                return popup(win, sock, msg)

            elif msg == "end":
                msg = "end" if isEnd(side, board, flags) else "abandon"
                return popup(win, sock, msg)

            elif msg == "draw?":
                ret = draw(win, sock, False)
                if ret in [2, 3]:
                    return
            elif msg == "win":
                ret = draw_win(win, sock, False)
                # ret = rematch(win, sock)
                return ret
            elif msg.startswith("mov") and side != player:
                fro, to, promote = decode(msg[3:])
                if isValidMove(side, board, flags, fro, to):
                    animate(win, side, board, fro, to, load, player)

                    side, board, flags = makeMove(
                        side, board, fro, to, flags, promote)
                    sel = [0, 0]
                else:
                    return 2
