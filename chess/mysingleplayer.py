'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with a chess engine implemented in python
For more info, read the file at chess.lib.ai

For more understanding of the variables used here, checkout multiplayer.py

Level of development = STABLE
'''

from chess.lib import *
from tools import sound

# Run main code for chess singleplayer
def main(win, player, LOAD, moves=""):
    sound.play_start(LOAD)
    start(win)
    
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
                        
                    if isOccupied(side, board, [x, y]):
                        sound.play_click(LOAD)
                        
                    prevsel = sel
                    sel = [x, y]
                elif side == player or end:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        if prompt(win, saveGame(moves, "mysingle", player)):
                            return
                    elif 0 < x < 80 and 0 < y < 50 and LOAD[4]:
                        moves = undo(moves, 2) if side == player else undo(moves)
                        side, board, flags = convertMoves(moves)
                            
        showScreen(win, side, board, flags, sel, LOAD, player)
        if side != player:
            if not end:
                fro, to = miniMax(side, board, flags)
                
                sound.play_drag(LOAD)
                animate(win, side, board, fro, to, FLIP)
                sound.play_move(LOAD)
                
                promote = getPromote(win, side, board, fro, to, True)
                side, board, flags = makeMove(side, board, fro, to, flags)
                
                moves += " " + encode(fro, to, promote)
                sel = [0, 0]
        
        elif isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, side, board, prevsel, sel)
            
            sound.play_drag(LOAD)
            animate(win, side, board, prevsel, sel, FLIP)
            sound.play_move(LOAD)
            
            side, board, flags = makeMove(
                side, board, prevsel, sel, flags, promote)
            moves += " " + encode(prevsel, sel, promote)      