'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with the popular stockfish engine with the
help of pyFish module.
For more info, read docs in pyFish module.

For more understanding of the variables used here, checkout multiplayer.py
'''

import os
from chess.lib import *
from tools.pyFish import StockFish      

# Get path to stockfish executable from path.txt
def getpath():
    conffile = os.path.join("res", "stockfish", "path.txt")
    if os.path.exists(conffile):
        with open(conffile, "r") as f:
            return f.read().strip()
 
# Run main code for chess
def main(win, player, level, LOAD, moves=""):
    fish = StockFish(getpath(), level)
    
    if not fish.isActive():
        os.remove(os.path.join("res", "stockfish", "path.txt"))
        return
        
    fish.startGame(moves)
    side, board, flags = convertMoves(moves)
    
    if player == 1 and not moves.strip():
        fish.startEngine()
    
    clock = pygame.time.Clock()
    sel = [0, 0]
    prevsel = [0, 0]
    
    FLIP = LOAD[1] and player

    while True:
        clock.tick(25)
        end = isEnd(side, board, flags)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                fish.close()
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
                        msg = saveGame(fish.moveSequence,
                                       "single", player, level)
                        if prompt(win, msg):
                            fish.close()
                            return
                    elif 0 < x < 80 and 0 < y < 50 and LOAD[4]:
                        fish.undo()
                        side, board, flags = convertMoves(fish.moveSequence)
                            
        showScreen(win, side, board, flags, sel, LOAD, player)
        if side != player:
            if not end and fish.hasMoved():
                fro, to, promote = decode(fish.getMove())
                animate(win, side, board, fro, to, FLIP)
                board = move(side, board, fro, to, promote)
                flags = updateFlags(side, board, fro, to, flags[0])
                side = flip(side)
                sel = [0, 0]
            
        elif isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, side, board, prevsel, sel)
            fish.makeMove(encode(prevsel, sel, promote))
            animate(win, side, board, prevsel, sel, FLIP)
            board = move(side, board, prevsel, sel, promote)
            flags = updateFlags(side, board, prevsel, sel, flags[0])
            side = flip(side)