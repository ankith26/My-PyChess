'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for multiplayer section of this
application.
'''
import time
from chess.lib import *

# run main code for chess
def main(win, mode, timer, load, movestr=""):
    start(win, load)
    
    moves = movestr.split()

    side, board, flags = convertMoves(moves)
    clock = pygame.time.Clock()
    sel = prevsel = [0, 0]

    if timer is not None:
        timer = list(timer)
    while True:
        looptime = getTime()
        clock.tick(25)
        
        timedelta = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                starttime = getTime()
                if prompt(win):
                    return 0
                timedelta += getTime() - starttime

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    starttime = getTime()
                    if prompt(win):
                        return 1
                    timedelta += getTime() - starttime

                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if load["flip"] and side:
                        x, y = 9 - x, 9 - y

                    if isOccupied(side, board, [x, y]):
                        sound.play_click(load)

                    prevsel = sel
                    sel = [x, y]

                    if isValidMove(side, board, flags, prevsel, sel):
                        starttime = getTime()
                        promote = getPromote(win, side, board, prevsel, sel)
                        animate(win, side, board, prevsel, sel, load)
                        
                        timedelta += getTime() - starttime
                        timer = updateTimer(side, mode, timer)

                        side, board, flags = makeMove(
                            side, board, prevsel, sel, flags, promote)
                        moves.append(encode(prevsel, sel, promote))

                else:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        starttime = getTime()
                        if prompt(win, saveGame(moves, mode=mode, timer=timer)):
                            return 1
                        timedelta += getTime() - starttime
                        
                    elif 0 < x < 80 and 0 < y < 50 and load["allow_undo"]:
                        moves = undo(moves)
                        side, board, flags = convertMoves(moves)

        showScreen(win, side, board, flags, sel, load)
        timer = showClock(win, side, mode, timer, looptime, timedelta)
