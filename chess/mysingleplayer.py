'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with a chess engine implemented in python
For more info, read the file at chess.lib.ai

For more understanding of the variables used here, checkout multiplayer.py
'''

from chess.lib import *
from chess.lib.ai import miniMax

# A simple function to undo in singleplayer mode
def undo(moves):
    moves = moves.strip().split(" ")
    if len(moves) == 1:
        return moves[0]
    else:
        return " ".join(moves[:-2]) 

# Run main code for chess
def main(win, player, LOAD, moves=""):
    side, board, flags = convertMoves(moves)
    
    clock = pygame.time.Clock()
    sel = [0, 0]
    prevsel = [0, 0]
    
    FLIP = LOAD[1] and player

    while True:
        clock.tick(25)
        end = isEnd(side, board, flags)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if FLIP:
                        x, y = 9 - x, 9 - y
                    prevsel = sel
                    sel = [x, y]
                elif side == player or end:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        if prompt(win, saveGame(moves, "mysingle", player)):
                            return
                    elif 0 < x < 80 and 0 < y < 50 and LOAD[4]:
                        moves = undo(moves)
                        side, board, flags = convertMoves(moves)
                            
        showScreen(win, side, board, flags, sel, LOAD, player)
        if side != player:
            if not end:
                fro, to = miniMax(side, board, flags)
                animate(win, side, board, fro, to, FLIP)
                if getType(side, board, fro) == 'p' and to[1] == side*7 + 1:
                    moves += " " + encode(fro, to, 'q')
                else:
                    moves += " " + encode(fro, to)             
                board = move(side, board, fro, to)
                flags = updateFlags(side, board, fro, to, flags[0])      
                side = flip(side)
                sel = [0, 0]
        
        elif isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, side, board, prevsel, sel)
            animate(win, side, board, prevsel, sel, FLIP)
            board = move(side, board, prevsel, sel, promote)
            flags = updateFlags(side, board, prevsel, sel, flags[0])
            moves += " " + encode(prevsel, sel, promote)
            side = flip(side)      