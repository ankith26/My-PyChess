"""
This file is a part of My-PyChess application.
In this file, we define the core chess-related functions.
For a better understanding of the variables used here, checkout docs.txt
"""
# A simple function to make a copy of the board
def copy(board):
    return [[list(j) for j in board[i]] for i in range(2)]       
        
# Return the type of piece given it's position. Return None if Empty.
def getType(side, board, pos):
    for piece in board[side]:
        if piece[:2] == pos:
            return piece[2]

# Determine wether the position given is occupied by a piece of the given side.
def isOccupied(side, board, pos):
    return getType(side, board, pos) is not None

# Determine wether the position(s) given is(are) empty or not
def isEmpty(board, *poslist):
    for pos in poslist:
        for side in range(2):
            if isOccupied(side, board, pos):
                return False
    return True

# Determine wether the king of a given side is in check or not.
def isChecked(side, board):
    for piece in board[side]:
        if piece[2] == "k":
            for i in board[not side]:
                if piece[:2] in rawMoves(not side, board, i):
                    return True
            return False

# Determine all the possible LEGAL moves available for the side.
def legalMoves(side, board, flags):
    for piece in board[side]:
        for pos in availableMoves(side, board, piece, flags):
            yield [piece[:2], pos]
            
# This function returns wether a game has ended or not
def isEnd(side, board, flags):
    # Check if the king of the given side is present in the board
    king_present = any(piece[2] == "k" for piece in board[side])
    
    # If the king is not present, the game has ended
    return not king_present

# This function moves the piece from one coordinate to other while handling the
# capture of enemy, pawn promotion and en-passent. 
# One thing to note that this function directly modifies global value of the
# board variable from within the function, so pass a copy of the board
# variable if you do not want global modification of the variable.
def move(side, board, fro, to, promote="p"):
    UP = 8 if side else 1
    DOWN = 1 if side else 8
    ALLOWENP = fro[1] == 4 + side and to[0] != fro[0] and isEmpty(board, to)
    for piece in board[not side]:
        if piece[:2] == to:
            board[not side].remove(piece)
            break

    for piece in board[side]:
        if piece[:2] == fro:
            piece[:2] = to
            if piece[2] == "k":
                if fro[0] - to[0] == 2:
                    move(side, board, [1, DOWN], [4, DOWN])
                elif to[0] - fro[0] == 2:
                    move(side, board, [8, DOWN], [6, DOWN])
                    
            if piece[2] == "p":
                if to[1] == UP:
                    board[side].remove(piece)
                    board[side].append([to[0], UP, promote])
                if ALLOWENP:
                    board[not side].remove([to[0], fro[1], "p"])
            break
    return board

# This function returns wether a move puts ones own king at check
def moveTest(side, board, fro, to):
    # return not isChecked(side, move(side, copy(board), fro, to))
    return True

# This function returns wether a move is valid or not
def isValidMove(side, board, flags, fro, to):
    if 0 < to[0] < 9 and 0 < to[1] < 9 and not isOccupied(side, board, to):
        piece = fro + [getType(side, board, fro)]
        if to in rawMoves(side, board, piece, flags):
            return moveTest(side, board, fro, to)

# This is an important wrapper function. It makes the move, updates the
# flags and flips the side, returning the updated data.
def makeMove(side, board, fro, to, flags, promote="q"):
    newboard = move(side, copy(board), fro, to, promote)
    newflags = updateFlags(side, newboard, fro, to, flags)
    if isEnd(side, newboard, newflags):
        print("Game Over! The king has been captured.")
        # You might want to handle the end of the game here
    return not side, newboard, newflags

# Does a routine check to update all the flags required for castling and
# enpassent. This function needs to be called AFTER every move played.
def updateFlags(side, board, fro, to, flags):
    castle = list(flags[0])
    if [5, 8, "k"] not in board[0] or [1, 8, "r"] not in board[0]:
        castle[0] = False
    if [5, 8, "k"] not in board[0] or [8, 8, "r"] not in board[0]:
        castle[1] = False
    if [5, 1, "k"] not in board[1] or [1, 1, "r"] not in board[1]:
        castle[2] = False
    if [5, 1, "k"] not in board[1] or [8, 1, "r"] not in board[1]:
        castle[3] = False

    enP = None
    if getType(side, board, to) == "p":
        if fro[1] - to[1] == 2:
            enP = [to[0], 6]
        elif to[1] - fro[1] == 2:
            enP = [to[0], 3]

    return castle, enP

# Given a side, board and piece, it yields all possible legal moves
# of that piece. This function is an extension/wrapper on rawMoves() 
def availableMoves(side, board, piece, flags):
    for i in rawMoves(side, board, piece, flags):
        if 0 < i[0] < 9 and 0 < i[1] < 9 and not isOccupied(side, board, i):
            if moveTest(side, board, piece[:2], i):
                yield i
    
# Given a side, board and piece, it yields all possible moves by the piece.
# If flags are given, it can also yeild the special moves of chess.
# It also returns moves that are illegal, therefore the function is for
# internal use only
def rawMoves(side, board, piece, flags=[None, None]):  
    x, y, ptype = piece
    if ptype == "p":
        if not side:
            if y == 7 and isEmpty(board, [x, 6], [x, 5]):
                yield [x, 5]
            if isEmpty(board, [x, y - 1]):
                yield [x, y - 1]
                
            for i in ([x + 1, y - 1], [x - 1, y - 1]):
                if isOccupied(1, board, i) or flags[1] == i:
                    yield i
        else:
            if y == 2 and isEmpty(board, [x, 3], [x, 4]):
                yield [x, 4]
            if isEmpty(board, [x, y + 1]):
                yield [x, y + 1]

            for i in ([x + 1, y + 1], [x - 1, y + 1]):
                if isOccupied(0, board, i) or flags[1] == i:
                    yield i

    elif ptype == "n":
        yield from (
            [x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2],
            [x + 2, y + 1], [x + 2, y - 1], [x - 2, y + 1], [x - 2, y - 1]
        )

    elif ptype == "b":
        for i in range(1, 8):
            yield [x + i, y + i]
            if not isEmpty(board, [x + i, y + i]):
                break
        for i in range(1, 8):
            yield [x + i, y - i]
            if not isEmpty(board, [x + i, y - i]):
                break
        for i in range(1, 8):
            yield [x - i, y + i]
            if not isEmpty(board, [x - i, y + i]):
                break
        for i in range(1, 8):
            yield [x - i, y - i]
            if not isEmpty(board, [x - i, y - i]):
                break

    elif ptype == "r":
        for i in range(1, 8):
            yield [x + i, y]
            if not isEmpty(board, [x + i, y]):
                break
        for i in range(1, 8):
            yield [x - i, y]
            if not isEmpty(board, [x - i, y]):
                break
        for i in range(1, 8):
            yield [x, y + i]
            if not isEmpty(board, [x, y + i]):
                break
        for i in range(1, 8):
            yield [x, y - i]
            if not isEmpty(board, [x, y - i]):
                break

    elif ptype == "q":
        yield from rawMoves(side, board, [x, y, "b"])
        yield from rawMoves(side, board, [x, y, "r"])

    elif ptype == "k":
        if flags[0] is not None and not isChecked(side, board):
            if flags[0][0] and isEmpty(board, [2, 8], [3, 8], [4, 8]):
                if moveTest(0, board, [5, 8], [4, 8]):
                    yield [3, 8]
            if flags[0][1] and isEmpty(board, [6, 8], [7, 8]):
                if moveTest(0, board, [5, 8], [6, 8]):
                    yield [7, 8]
            if flags[0][2] and isEmpty(board, [2, 1], [3, 1], [4, 1]):
                if moveTest(1, board, [5, 1], [4, 1]):
                    yield [3, 1]
            if flags[0][3] and isEmpty(board, [6, 1], [7, 1]):
                if moveTest(1, board, [5, 1], [6, 1]):
                    yield [7, 1]

        yield from (
            [x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y],
            [x - 1, y + 1], [x, y + 1], [x + 1, y + 1], [x + 1, y]
        )