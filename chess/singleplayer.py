'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for singleplayer section of this
application. This interfaces with the popular stockfish engine with the
help of pyFish module.

Interface code at ext.pyFish

For a better understanding of the variables used here, checkout docs.txt
'''

from chess.lib import *
from ext.pyFish import StockFish


def helper_function():
    pass

def nl():
    print("")


# Run main code for chess singleplayer (stockfish)
def main(win, player, level, load, movestr=""):
    fish = StockFish(getSFpath(), level)

    if not fish.isActive():
        rmSFpath()
        return 1

    start(win, load)

    moves = movestr.split()
    fish.startGame(movestr)
    side, board, flags = convertMoves(moves)

    if player == 1 and not moves:
        fish.startEngine()

    clock = pygame.time.Clock()
    sel = prevsel = [0, 0]
    while True:
        clock.tick(25)
        end = isEnd(side, board, flags)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                fish.close()
                return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50 and prompt(win):
                    fish.close()
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
                        fish.makeMove(encode(prevsel, sel, promote))

                elif side == player or end:
                    sel = [0, 0]
                    if 350 < x < 500 and 460 < y < 490:
                        msg = saveGame(fish.moves, "single", player, level)
                        if prompt(win, msg):
                            fish.close()
                            return 1
                    elif 0 < x < 80 and 0 < y < 50 and load["allow_undo"]:
                        if side == player:
                            fish.undo(2)
                        else:
                            fish.undo()
                        side, board, flags = convertMoves(fish.moves)

        end = isEnd(side, board, flags)
        
        showScreen(win, side, board, flags, sel, load, player)
        if side != player and not end and fish.hasMoved():
            fro, to, promote = decode(fish.getMove())
            animate(win, side, board, fro, to, load, player)

            side, board, flags = makeMove(side, board, fro, to, flags, promote)
            sel = [0, 0]
