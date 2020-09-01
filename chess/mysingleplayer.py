'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with a chess engine implemented in pure python.
For the Python Chess Engine, see file at chess.lib.ai

For a better understanding of the variables used here, checkout docs.txt
'''

from chess.lib import *

# Run main code for chess singleplayer
def main(win, player, load, movestr=""):
    start(win, load)

    moves = movestr.split()
    side, board, flags = convertMoves(moves)

    clock = pygame.time.Clock()
    sel = prevsel = [0, 0]
    while True:
        clock.tick(25)
        end = isEnd(side, board, flags)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50 and prompt(win):
                    return 1

                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if load["flip"] and player:
                        x, y = 9 - x, 9 - y

                    if isOccupied(side, board, [x, y]):
                        sound.play_click(load)

                    prevsel = sel
                    sel = [x, y]

                    if (side == player
                        and isValidMove(side, board, flags, prevsel, sel)):
                        promote = getPromote(win, side, board, prevsel, sel)
                        animate(win, side, board, prevsel, sel, load, player)

                        side, board, flags = makeMove(
                            side, board, prevsel, sel, flags, promote)
                        moves.append(encode(prevsel, sel, promote))

                elif side == player or end:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        if prompt(win, saveGame(moves, "mysingle", player)):
                            return 1
                    elif 0 < x < 80 and 0 < y < 50 and load["allow_undo"]:
                        moves = undo(moves, 2) if side == player else undo(moves)
                        side, board, flags = convertMoves(moves)

        showScreen(win, side, board, flags, sel, load, player)
        
        end = isEnd(side, board, flags)
        if side != player and not end:
            fro, to = miniMax(side, board, flags)
            animate(win, side, board, fro, to, load, player)

            promote = getPromote(win, side, board, fro, to, True)
            side, board, flags = makeMove(side, board, fro, to, flags)

            moves.append(encode(fro, to, promote))
            sel = [0, 0]
