import pygame
import time
# these are initial pos
wBoard = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7],# pawns
          [1, 8], [8, 8],
          [2, 8], [7, 8],
          [3, 8], [6, 8],
          [4, 8], [5, 8]]  # Queen and king
bBoard = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2],# pawns
          [1, 1], [8, 1],
          [2, 1], [7, 1],
          [3, 1], [6, 1],
          [4, 1], [5, 1]]  # Queen and king
wKingMoved = bKingMoved = False  # Some variables for castling
wRook1Moved = bRook1Moved = False
wRook2Moved = bRook2Moved = False

WPAWN = pygame.image.load("pieces/whitePawn.png")
WROOK = pygame.image.load("pieces/whiteRook.png")
WKNIGHT = pygame.image.load("pieces/whiteKnight.png")
WBISHOP = pygame.image.load("pieces/whiteBishop.png")
WQUEEN = pygame.image.load("pieces/whiteQueen.png")
WKING = pygame.image.load("pieces/whiteKing.png")
BPAWN = pygame.image.load("pieces/blackPawn.png")
BROOK = pygame.image.load("pieces/blackRook.png")
BKNIGHT = pygame.image.load("pieces/blackKnight.png")
BBISHOP = pygame.image.load("pieces/blackBishop.png")
BQUEEN = pygame.image.load("pieces/blackQueen.png")
BKING = pygame.image.load("pieces/blackKing.png")

CHECKMATE = pygame.image.load("images/checkmate.png")
STALEMATE = pygame.image.load("images/stalemate.png")
CHOOSE = pygame.image.load("images/choose.png")

def drawBoard(win):
    colour = (0, 255, 255)
    pygame.draw.rect(win, colour, (0, 0, 500, 50))
    pygame.draw.rect(win, colour, (0, 0, 50, 500))
    pygame.draw.rect(win, colour, (450, 0, 50, 500))
    pygame.draw.rect(win, colour, (0, 450, 500, 50))
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                colour = (255, 255, 255)
            else:
                colour = (181, 101, 29)
            pygame.draw.rect(
                win, colour, (50 * x + 50, 50 * y + 50, 50, 50))
def drawPieces(win):
    count = 0
    for x in wBoard:
        if x is not None:
            if count in range(8):
                win.blit(WPAWN, (x[0] * 50, x[1] * 50))
            elif count in range(8, 10):
                win.blit(WROOK, (x[0] * 50, x[1] * 50))
            elif count in range(10, 12):
                win.blit(WKNIGHT, (x[0] * 50, x[1] * 50))
            elif count in range(12, 14):
                win.blit(WBISHOP, (x[0] * 50, x[1] * 50))
            elif count == 14:
                win.blit(WQUEEN, (x[0] * 50, x[1] * 50))
            elif count == 15:
                win.blit(WKING, (x[0] * 50, x[1] * 50))
            else:
                if x[2] == 'knight':
                    win.blit(WKNIGHT, (x[0] * 50, x[1] * 50))
                if x[2] == 'bishop':
                    win.blit(WBISHOP, (x[0] * 50, x[1] * 50))
                if x[2] == 'rook':
                    win.blit(WROOK, (x[0] * 50, x[1] * 50))
                if x[2] == 'queen':
                    win.blit(WQUEEN, (x[0] * 50, x[1] * 50))
        count += 1
    count = 0
    for x in bBoard:
        if x is not None:
            if count in range(8):
                win.blit(BPAWN, (x[0] * 50, x[1] * 50))
            elif count in range(8, 10):
                win.blit(BROOK, (x[0] * 50, x[1] * 50))
            elif count in range(10, 12):
                win.blit(BKNIGHT, (x[0] * 50, x[1] * 50))
            elif count in range(12, 14):
                win.blit(BBISHOP, (x[0] * 50, x[1] * 50))
            elif count == 14:
                win.blit(BQUEEN, (x[0] * 50, x[1] * 50))
            elif count == 15:
                win.blit(BKING, (x[0] * 50, x[1] * 50))
            else:
                if x[2] == 'knight':
                    win.blit(BKNIGHT, (x[0] * 50, x[1] * 50))
                if x[2] == 'bishop':
                    win.blit(BBISHOP, (x[0] * 50, x[1] * 50))
                if x[2] == 'rook':
                    win.blit(BROOK, (x[0] * 50, x[1] * 50))
                if x[2] == 'queen':
                    win.blit(BQUEEN, (x[0] * 50, x[1] * 50))
        count += 1
        
def animate(win, side, ptype, fro, to):
    if ptype == "pawn":
        if side == "w":
            piece = WPAWN
        else:
            piece = BPAWN
    elif ptype == "rook":
        if side == "w":
            piece = WROOK
        else:
            piece = BROOK
    elif ptype == "knight":
        if side == "w":
            piece = WKNIGHT
        else:
            piece = BKNIGHT
    elif ptype == "bishop":
        if side == "w":
            piece = WBISHOP
        else:
            piece = BBISHOP
    elif ptype == "queen":
        if side == "w":
            piece = WQUEEN
        else:
            piece = BQUEEN
    elif ptype == "king":
        if side == "w":
            piece = WKING
        else:
            piece = BKING
    x1, y1 = fro[0], fro[1]
    x2, y2 = to[0], to[1]
    stepx = (x2 - x1)*5
    stepy = (y2 - y1)*5
    for i in range(10):
        drawBoard(win)
        drawPieces(win)
        if (x2 +y2) % 2 == 0:
            pygame.draw.rect(win, (255,255,255), (x2*50, y2*50, 50, 50))
        else:
            pygame.draw.rect(win, (181, 101, 29), (x2*50, y2*50, 50, 50))
        win.blit(piece, (x1*50+(i*stepx), y1*50+(i*stepy)))
        pygame.display.update()
        time.sleep(0.02)
        
def copy(sboard):
    board = []
    for i in sboard:
        if i is None:
            board.append(None)
        else:
            board.append(list(i))
    return board

def getChoice():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 0 < y < 50:
                    if 230 < x < 280:
                        return "queen"
                    elif 280 < x < 330:
                        return "bishop"
                    elif 330 < x < 380:
                        return "rook"
                    elif 380 < x < 430:
                        return "knight"

def getPiece(side, pos):
    if side == "w":
        Board = wBoard
    elif side == "b":
        Board = bBoard
    for i in range(len(Board)):
        if Board[i] is not None and Board[i][:2] == pos:
            if i in range(8):
                return "pawn"
            elif i in range(8, 10):
                return "rook"
            elif i in range(10, 12):
                return "knight"
            elif i in range(12, 14):
                return "bishop"
            elif i == 14:
                return "queen"
            elif i == 15:
                return "king"
            else:
                return Board[i][2]

def move(side, fro, to, recurse=True, eatpiece=True):
    global wBoard, bBoard
    val = -1
    if side == "w":
        board = copy(wBoard)
        if eatpiece:
            for i in range(len(bBoard)):
                if bBoard[i] is not None and bBoard[i][:2] == to:
                    bBoard[i] = None
                    val = i
        for i in range(len(wBoard)):
            if wBoard[i] is not None and wBoard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2:
                        move("w", [1, 8], [4, 8])
                    elif fro[0] - to[0] == -2:
                        move("w", [8, 8], [6, 8])
                wBoard[i][:2] = to
                if i in range(8):
                    if to[1] == 1:
                        wBoard[i] = None
                        wBoard.append([to[0], 1, getChoice()])
        if isChecked(side) and recurse:
            if board.index(fro) in range(8) and to[1] == 1:
                wBoard.pop()
                wBoard[board.index(fro)] = [fro[0], 2]
            else:
                move(side, to, fro, False)
                if val != -1:
                    bBoard[val] = to
            return False
        else:
            return True
    elif side == "b":
        board = copy(bBoard)
        if eatpiece:
            for i in range(len(wBoard)):
                if wBoard[i] is not None and wBoard[i][:2] == to:
                    wBoard[i] = None
                    val = i
        for i in range(len(bBoard)):
            if bBoard[i] is not None and bBoard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2:
                        move("b", [1, 1], [4, 1])
                    elif fro[0] - to[0] == -2:
                        move("b", [8, 1], [6, 1])
                bBoard[i][:2] = to
                if i in range(8):
                    if to[1] == 8:
                        bBoard[i] = None
                        bBoard.append([to[0], 8, getChoice()])
        if isChecked(side) and recurse:
            if board.index(fro) in range(8) and to[1] == 8:
                bBoard.pop()
                bBoard[board.index(fro)] = [fro[0], 7]
            else:
                move(side, to, fro, False)
                if val != -1:
                    wBoard[val] = to
            return False
        else:
            return True

def doRoutine():
    global wKingMoved, bKingMoved, wRook1Moved, wRook2Moved,\
           bRook1Moved, bRook2Moved
    if wBoard[15] != [5, 8]:
        wKingMoved = True
    if bBoard[15] != [5, 1]:
        bKingMoved = True
    if wBoard[8] != [1, 8]:
        wRook1Moved = True
    if wBoard[9] != [8, 8]:
        wRook2Moved = True
    if bBoard[8] != [1, 1]:
        bRook1Moved = True
    if bBoard[9] != [8, 1]:
        bRook2Moved = True

def isOccupied(x, y, flag="w"):
    if flag == 'w':
        for i in bBoard:
            if i != None and i[:2] == [x, y]:
                return "b"
        for i in wBoard:
            if i != None and i[:2] == [x, y]:
                return "w"
    elif flag == 'b':
        for i in wBoard:
            if i != None and i[:2] == [x, y]:
                return "w"
        for i in bBoard:
            if i != None and i[:2] == [x, y]:
                return "b"
    return "empty"

def allMoves(side, flag=True):
    a = 0
    if side == 'w':
        oside = 'b'
        board = wBoard
    elif side == 'b':
        oside = 'w'
        board = bBoard
    for i in board:
        if i is not None:
            if a in range(8) and side == 'w':
                if i[0] + 1 in range(1, 9) and i[1] - 1 in range(1, 9):
                    if isOccupied(i[0] + 1, i[1] - 1) == oside or not flag:
                        yield [a, [i[0] + 1, i[1] - 1]]
                if i[0] - 1 in range(1, 9) and i[1] - 1 in range(1, 9):
                    if isOccupied(i[0] - 1, i[1] - 1) == oside or not flag:
                        yield [a, [i[0] - 1, i[1] - 1]]
                if i[1] == 7:
                    if isOccupied(i[0], 5) == isOccupied(i[0], 6) == "empty":
                        if flag:
                            yield [a, [i[0], 5]]
                if isOccupied(i[0], i[1] - 1) == "empty":
                    if flag:
                        yield [a, [i[0], i[1] - 1]]
            elif a in range(8) and side == 'b':
                if i[0] + 1 in range(1, 9) and i[1] + 1 in range(1, 9):
                    if isOccupied(i[0] + 1, i[1] + 1) == oside or not flag:
                        yield [a, [i[0] + 1, i[1] + 1]]
                if i[0] - 1 in range(1, 9) and i[1] + 1 in range(1, 9):
                    if isOccupied(i[0] - 1, i[1] + 1) == oside or not flag:
                        yield [a, [i[0] - 1, i[1] + 1]]
                if i[1] == 2:
                    if isOccupied(i[0], 3) == isOccupied(i[0], 4) == "empty":
                        if flag:
                            yield [a, [i[0], 4]]
                if isOccupied(i[0], i[1] + 1) == "empty":
                    if flag:
                        yield [a, [i[0], i[1] + 1]]
            elif a in range(8, 10):
                for j in availableMoves(side, 'rook', i):
                    if isOccupied(j[0], j[1]) != side:
                        yield [a, j]
            elif a in range(10, 12):
                for j in availableMoves(side, 'knight', i):
                    if isOccupied(j[0], j[1]) != side:
                        yield [a, j]
            elif a in range(12, 14):
                for j in availableMoves(side, 'bishop', i):
                    if isOccupied(j[0], j[1]) != side:
                        yield [a, j]
            elif a == 14:
                for j in availableMoves(side, 'queen', i):
                    if isOccupied(j[0], j[1]) != side:
                        yield [a, j]
            elif a == 15:
                x, y = i[0], i[1]
                for j in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                          [x, y - 1], [x, y + 1],
                          [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
                    if j[0] in range(1, 9) and j[1] in range(1, 9):
                        if isOccupied(j[0], j[1]) != side:
                            yield [a, j]
            else:
                for j in availableMoves(side, i[2], i[:2]):
                    if isOccupied(j[0], j[1]) != side:
                        yield [a, j]
        a += 1

def isChecked(side, pos=None):
    if side == 'w':
        if pos is None:
            pos = wBoard[15]
        side = 'b'
    elif side == 'b':
        if pos is None:
            pos = bBoard[15]
        side = 'w'
    for i in allMoves(side, False):
        if i[1] == pos:
            return True
    return False

def isCheckmate(side):
    data = [i for i in allMoves(side)]
    if side == 'w':
        board = wBoard
    elif side == 'b':
        board = bBoard
    for i in reversed(data):
        if board[i[0]] is not None:
            pos = list(board[i[0]])
            if move(side, pos, i[1], eatpiece=False):
                move(side, i[1], pos, False)
                del data
                return False
    del data
    return True

def availableMoves(side, piece, pos):
    x, y = pos[0], pos[1]
    if isOccupied(x, y, side) != side:
        return []
    if piece == 'pawn':
        if side == 'w':
            if y == 7 and isOccupied(x, 5) == isOccupied(x, 6) == "empty":
                yield [x, 5]
            if isOccupied(x + 1, y - 1) == "b":
                yield [x + 1, y - 1]
            if isOccupied(x - 1, y - 1) == "b":
                yield [x - 1, y - 1]
            if isOccupied(x, y - 1) == "empty":
                yield [x, y - 1]
        else:
            if y == 2 and isOccupied(x, 4) == isOccupied(x, 3) == "empty":
                yield [x, 4]
            if isOccupied(x + 1, y + 1) == "w":
                yield [x + 1, y + 1]
            if isOccupied(x - 1, y + 1) == "w":
                yield [x - 1, y + 1]
            if isOccupied(x, y + 1) == "empty":
                yield [x, y + 1]
    elif piece == 'knight':
        for i in [[x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2]
                ,[x + 2, y + 1], [x + 2, y - 1], [x - 2, y + 1], [x - 2, y - 1]]:
            if i[0] in range(1, 9) and i[1] in range(1, 9):
                yield i
    elif piece == 'bishop':
        for i in range(1, 8):
            if x + i in range(1, 9) and y + i in range(1, 9):
                yield [x + i, y + i]
                if isOccupied(x + i, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x + i in range(1, 9) and y - i in range(1, 9):
                yield [x + i, y - i]
                if isOccupied(x + i, y - i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y + i in range(1, 9):
                yield [x - i, y + i]
                if isOccupied(x - i, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y - i in range(1, 9):
                yield [x - i, y - i]
                if isOccupied(x - i, y - i) != "empty":
                    break
    elif piece == 'rook':
        for i in range(1, 8):
            if x + i in range(1, 9) and y in range(1, 9):
                yield [x + i, y]
                if isOccupied(x + i, y) != "empty":
                    break
        for i in range(1, 8):
            if x in range(1, 9) and y + i in range(1, 9):
                yield [x, y + i]
                if isOccupied(x, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y in range(1, 9):
                yield [x - i, y]
                if isOccupied(x - i, y) != "empty":
                    break
        for i in range(1, 8):
            if x in range(1, 9) and y - i in range(1, 9):
                yield [x, y - i]
                if isOccupied(x, y - i) != "empty":
                    break
    elif piece == 'queen':
        for i in availableMoves(side, 'bishop', pos):
            yield i
        for i in availableMoves(side, 'rook', pos):
            yield i
    elif piece == 'king':
        if not isChecked(side):
            if side == 'w':
                if not wKingMoved and not wRook1Moved:
                    if isOccupied(
                            2, 8) == isOccupied(
                            3, 8) == isOccupied(
                            4, 8) == "empty":
                        if not isChecked(
                            'w', [3, 8]) and not isChecked('w', [4, 8]):
                            yield [3, 8]
                if not wKingMoved and not wRook2Moved:
                    if isOccupied(6, 8) == isOccupied(7, 8) == "empty":
                        if not isChecked(
                            'w', [6, 8]) and not isChecked('w', [7, 8]):
                            yield [7, 8]
            else:
                if not bKingMoved and not bRook1Moved:
                    if isOccupied(
                            2, 1) == isOccupied(
                            3, 1) == isOccupied(
                            4, 1) == "empty":
                        if not isChecked(
                            'b', [3, 1]) and not isChecked('b', [4, 1]):
                            yield [3, 1]
                if not bKingMoved and not bRook2Moved:
                    if isOccupied(6, 1) == isOccupied(7, 1) == "empty":
                        if not isChecked(
                            'b', [6, 1]) and not isChecked(
                            'b', [7, 1]):
                            yield [7, 1]
        for i in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                  [x, y - 1], [x, y + 1],
                  [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
            if not isChecked(side, i):
                if i[0] in range(1, 9) and i[1] in range(1, 9):
                    yield i
    else:
        pass
