"""
This file is a file of My-PyChess application.
This file gets imported whenever one tries to do
>>> from chess.lib import *
In this file, we import all the useful functions for chess from the
respective modules.
Some functions that need utility of other functions from various other modules
are defined here.

For more understanding of the variables used here, checkout multiplayer.py

Level of development = STABLE
"""

from chess.lib.core import (
    flip,
    getType,
    isOccupied,
    isChecked,  
    moveTest,
    isEnd,
    isValidMove,
    availableMoves,
    makeMove, 
)
from chess.lib.gui import (
    pygame,
    CHESS,
    getChoice,
    drawBoard,
    drawPieces,
    prompt,
    start, 
)
from chess.lib.utils import encode, decode, undo, getSFpath, rmSFpath, saveGame
from chess.lib.ai import miniMax

# This function converts a string of moves(move sequence) of standard notation
# into the notation used by the game.
def convertMoves(moves):
    side = 0
    board = (
        [
            [1, 7, "p"], [2, 7, "p"], [3, 7, "p"], [4, 7, "p"],
            [5, 7, "p"], [6, 7, "p"], [7, 7, "p"], [8, 7, "p"],
            [1, 8, "r"], [2, 8, "n"], [3, 8, "b"], [4, 8, "q"],
            [5, 8, "k"], [6, 8, "b"], [7, 8, "n"], [8, 8, "r"],
        ], [
            [1, 2, "p"], [2, 2, "p"], [3, 2, "p"], [4, 2, "p"],
            [5, 2, "p"], [6, 2, "p"], [7, 2, "p"], [8, 2, "p"],
            [1, 1, "r"], [2, 1, "n"], [3, 1, "b"], [4, 1, "q"],
            [5, 1, "k"], [6, 1, "b"], [7, 1, "n"], [8, 1, "r"],
        ]
    )
    flags = [[True for _ in range(4)], None]

    movelist = map(decode, filter(lambda x: x != "", moves.strip().split(" ")))

    for fro, to, promote in movelist:
        side, board, flags = makeMove(side, board, fro, to, flags, promote)

    return side, board, flags

# This is a wrapper for the getChoice GUI function.
# getPromote() first checks wether a pawn has reaches promotion state
# Then, if the game is multiplayer, getPromote() returns getChoice()
# Returns queen otherwise
def getPromote(win, side, board, fro, to, single=False):
    if getType(side, board, fro) == "p":
        if (side == 0 and to[1] == 1) or (side == 1 and to[1] == 8):
            if single:
                return "q"
            else:
                return getChoice(win, side)

# This is a gui function that draws green squares marking the legal moves of
# a seleced piece.
def showAvailMoves(win, side, board, pos, flags, flip):
    piece = pos + [getType(side, board, pos)]
    for i in availableMoves(side, board, piece, flags):
        if not isOccupied(side, board, i) and moveTest(side, board, pos, i):
            x = 470 - i[0] * 50 if flip else i[0] * 50 + 20
            y = 470 - i[1] * 50 if flip else i[1] * 50 + 20
            pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))

# This function makes a gentle animation of a piece that is getting moved.
# This function needs to be called BEFORE the actual move takes place
def animate(win, side, board, fro, to, flip):
    piece = CHESS.PIECES[side][getType(side, board, fro)]
    x1, y1 = fro[0] * 50, fro[1] * 50
    x2, y2 = to[0] * 50, to[1] * 50
    if flip:
        x1, y1 = 450 - x1, 450 - y1
        x2, y2 = 450 - x2, 450 - y2

    stepx = (x2 - x1) / 50
    stepy = (y2 - y1) / 50
    
    col = (180, 100, 30) if (fro[0] + fro[1]) % 2 else (220, 240, 240)
    
    clk = pygame.time.Clock()
    for i in range(51):
        clk.tick(120)
        drawBoard(win)
        drawPieces(win, board, flip)

        pygame.draw.rect(win, col, (x1, y1, 50, 50))
        win.blit(piece, (x1 + (i * stepx), y1 + (i * stepy)))
        pygame.display.update()
    drawBoard(win)

# This is a compilation of all gui functions. This handles the display of the
# screen when chess gameplay takes place. This tool needs to be called
# everytime in the game loop.
def showScreen(win, side, board, flags, pos, LOAD, player=None, online=False):
    multi = False
    if player is None:
        multi = True
        player = side

    flip = LOAD[1] and player

    drawBoard(win)
    
    if not multi:
        win.blit(CHESS.TURN[int(side == player)], (10, 460))
        
    if online:
        win.blit(CHESS.DRAW, (10, 12))
        win.blit(CHESS.RESIGN, (400, 462))    
    else:
        if LOAD[4]:
            win.blit(CHESS.UNDO, (10, 12))
        win.blit(CHESS.SAVE, (350, 462))

    if isEnd(side, board, flags):
        if isChecked(side, board):
            win.blit(CHESS.CHECKMATE, (100, 12))
            win.blit(CHESS.LOST, (320, 12))
            win.blit(CHESS.PIECES[side]["k"], (270, 0))
        else:
            win.blit(CHESS.STALEMATE, (160, 12))
    else:
        if isChecked(side, board):
            win.blit(CHESS.CHECK, (200, 12))

        if isOccupied(side, board, pos) and side == player:
            x = (9 - pos[0]) * 50 if flip else pos[0] * 50
            y = (9 - pos[1]) * 50 if flip else pos[1] * 50
            pygame.draw.rect(win, (255, 255, 0), (x, y, 50, 50))

    drawPieces(win, board, flip)
    if LOAD[3] and side == player:
        showAvailMoves(win, side, board, pos, flags, flip)
    pygame.display.update()
