'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for multiplayer section of this
application. This script uses all its tools from the module chess.lib

Level of development = STABLE

Documentation for commonly used variables:
1. side --> This variable stores which side will play next. If white needs
            To play, it stores an integer 0, if black needs to play, it store
            the integer 1.
2. board -> A 'board' variable stores the current state of the board.
            This is a 2-element tuple, First element is a list of all the
            pieces of white, and the second contains all pieces of black.
3. piece -> A 'piece' variable is a 3-element list. A piece can be denoted
            by its x and y cordinate on the chess board and it's type
            ("k" (king), "q" (queen), etc ...)
            
4. flags -> This stores the required flags for castling and enpassent.
            This is a 2-element list, first element is flag for castling.
            second is for enpassent.
            
The coordinate system used across this game is similar to the system used by
pygame.
The top left square is denoted by [1, 1] and as you go right, x value increases
(x is the first element in the list) and as you go down, y value increases
(y is the second element in the list). By this convention, the bottom right
square becomes [8, 8].
'''
from chess.lib import *
from tools import sound

# run main code for chess
def main(win, LOAD, moves=""):
    sound.play_start(LOAD)
    start(win)
    
    side, board, flags = convertMoves(moves)
    clock = pygame.time.Clock()
    sel = [0, 0]
    prevsel = [0, 0]

    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if LOAD[1] and side:
                        x, y = 9 - x, 9 - y
                        
                    if isOccupied(side, board, [x, y]):
                        sound.play_click(LOAD)
                        
                    prevsel = sel
                    sel = [x, y]
                else:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        if prompt(win, saveGame(moves)):
                            return
                    elif 0 < x < 80 and 0 < y < 50 and LOAD[4]:
                        moves = undo(moves)
                        side, board, flags = convertMoves(moves)
                            
        showScreen(win, side, board, flags, sel, LOAD)     
        if isValidMove(side, board, flags, prevsel, sel):
            promote = getPromote(win, side, board, prevsel, sel)
            
            sound.play_drag(LOAD)
            animate(win, side, board, prevsel, sel, bool(LOAD[1] and side))
            sound.play_move(LOAD)
            
            side, board, flags = makeMove(
                side, board, prevsel, sel, flags, promote)
            moves += " " + encode(prevsel, sel, promote)