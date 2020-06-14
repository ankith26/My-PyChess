'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with the popular stockfish engine with the
help of pyFish module.
For more info, read docs in pyFish module.

For more understanding of the variables used here, checkout multiplayer.py

Level of development = STABLE
'''

from chess.lib import *
from tools.pyFish import StockFish
from tools import sound
 
# Run main code for chess singleplayer (stockfish)
def main(win, player, level, LOAD, moves=""):
    fish = StockFish(getSFpath(), level)
    
    if not fish.isActive():
        rmSFpath()
        return
    
    sound.play_start(LOAD)
    start(win)
        
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
                        
                    if isOccupied(side, board, [x, y]):
                        sound.play_click(LOAD)
                        
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
                        if side == player:
                            fish.undo(2)
                        else:
                            fish.undo()
                        side, board, flags = convertMoves(fish.moveSequence)
                            
        showScreen(win, side, board, flags, sel, LOAD, player)
        if side != player:
            if not end and fish.hasMoved():
                fro, to, promote = decode(fish.getMove())
                
                sound.play_drag(LOAD)
                animate(win, side, board, fro, to, FLIP)
                sound.play_move(LOAD)
                
                side, board, flags = makeMove(
                    side, board, fro, to, flags, promote)
                sel = [0, 0]
            
        elif isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, side, board, prevsel, sel)

            sound.play_drag(LOAD)
            animate(win, side, board, prevsel, sel, FLIP)
            sound.play_move(LOAD)
            
            side, board, flags = makeMove(
                side, board, prevsel, sel, flags, promote)
            fish.makeMove(encode(prevsel, sel, promote))