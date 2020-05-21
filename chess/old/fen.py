"""
This file is a file of My-PyChess application.
It is a backup of an old feature that would help with FEN chess notation.
It is no longer used in the My-PyChess library, so transfered here.

Also, the notation for castle flag has changed, so changes will be required
to make this work with the current version of the game.
"""

# Based on the board state, flags and the side that just made a move,
# return a FEN represenation of the same
def makeFEN(side, brd, flags):
    board = [[0 for _ in range(8)] for _ in range(8)]

    for x, y, piece in brd[0]:
        board[y - 1][x - 1] = piece.capitalize()
    for x, y, piece in brd[1]:
        board[y - 1][x - 1] = piece

    stArr = []
    for row in board:
        var = 0
        for cnt, y in enumerate(row):
            if isinstance(y, int):
                var += 1
            else:
                if var != 0 and cnt != 0:
                    row.pop(cnt - 1)
                    row.insert(cnt - 1, var)
                    var = 0

            if cnt == 7 and var != 0:
                row.append(var)

        while row.count(0):
            row.remove(0)

        stArr.append("".join(map(str, row)))

    mystr = "/".join(stArr) + " "

    mystr = mystr + "w " if side else mystr + "b "
    mystr += flags[0] + " "

    if flags[1] is not None:
        mystr += str(LETTER[flags[1][0]]) + str(9 - flags[1][1])
    else:
        mystr += "-"

    return mystr


# Based on a FEN string, return the board state, flags and the side that plays
def fromFEN(fen):
    wboard = []
    bboard = []
    main, side, castle, e = fen.split()

    side = int(side == "b")

    for y, row in enumerate(main.split("/")):
        x = -1
        for col in list(row):
            try:
                x += int(col)
            except:
                x += 1
                if col.isupper():
                    wboard.append([x + 1, y + 1, col.lower()])
                else:
                    bboard.append([x + 1, y + 1, col])

    if e == "-":
        enP = None
    else:
        enP = [LETTER.index(e[0]), 9 - int(e[1])]

    return side, (wboard, bboard), (castle, enP)
