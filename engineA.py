import os
from engineB import getChoice

def copy(sboard):
    board = []
    for i in sboard:
        if i is None:
            board.append(None)
        else:
            board.append(list(i))
    return board

def getType(board, pos):
    for i in board:
        if i != None and i[:2] == pos:
            return i[2]
    return ""

def saveGame(move, wboard, bboard , castle, player = "multi", cnt = 0):
    name = os.path.join("savedGames" , "game" + str(cnt) + ".txt")
    try:
        file = open(name, 'r')
        file.close()
        saveGame(move, wboard, bboard, castle, player, cnt + 1)
    except:
        file = open(name, "w")
        text = player + '\n'
        text += str(move) + '\n'
        for i in wboard:
            if i != None:
                for j in i:
                    text += str(j) + ','
            else:
                text += 'None'
            text += ' '
        text += '\n'
        for i in bboard:
            if i != None:
                for j in i:
                    text += str(j) + ','
            else:
                text += 'None'
            text += ' '
        text += '\n'
        for i in castle:
            text += str(i) + ' '
        file.write(text)
        file.close()
        
def move(side, wboard, bboard, fro, to):
    if side == "w":
        for i in range(len(bboard)):
            if bboard[i] is not None and bboard[i][:2] == to:
                bboard[i] = None
        for i in range(len(wboard)):
            if wboard[i] is not None and wboard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2:
                        move("w", wboard, bboard, [1, 8], [4, 8])
                    elif fro[0] - to[0] == -2:
                        move("w", wboard, bboard, [8, 8], [6, 8])
                wboard[i][:2] = to
                if i in range(8):
                    if to[1] == 1:
                        wboard[i] = None
                        wboard.append([to[0], 1, getChoice()])
        return wboard, bboard
    elif side == "b":
        for i in range(len(wboard)):
            if wboard[i] is not None and wboard[i][:2] == to:
                wboard[i] = None
        for i in range(len(bboard)):
            if bboard[i] is not None and bboard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2:
                        move("b", wboard, bboard, [1, 1], [4, 1])
                    elif fro[0] - to[0] == -2:
                        move("b", wboard, bboard, [8, 1], [6, 1])
                bboard[i][:2] = to
                if i in range(8):
                    if to[1] == 8:
                        bboard[i] = None
                        bboard.append([to[0], 8, getChoice()])
        return wboard, bboard
    
def moveTest(side, wboard, bboard, fro, to):
    wboard, bboard = copy(wboard), copy(bboard)
    if side == "w":
        for i in range(len(wboard)):
            if wboard[i] is not None and wboard[i][:2] == fro:
                wboard[i][:2] = to
                if isChecked(side, wboard, bboard):
                    return False
                else:
                    return True
    elif side == "b":
        for i in range(len(bboard)):
            if bboard[i] is not None and bboard[i][:2] == fro:
                bboard[i][:2] = to
                if isChecked(side, wboard, bboard):
                    return False
                else:
                    return True
                
def doRoutine(wboard, bboard, castle):
    if wboard[15] != [5, 8, 'king']:
        castle[0] = True
    if bboard[15] != [5, 1, 'king']:
        castle[1] = True
    if wboard[8] != [1, 8, 'rook']:
        castle[2] = True
    if wboard[9] != [8, 8, 'rook']:
        castle[3] = True
    if bboard[8] != [1, 1, 'rook']:
        castle[4] = True
    if bboard[9] != [8, 1, 'rook']:
        castle[5] = True
    return castle

def isOccupied(wboard, bboard, x, y, flag="w"):
    if flag == 'w':
        for i in bboard:
            if i != None and i[:2] == [x, y]:
                return "b"
        for i in wboard:
            if i != None and i[:2] == [x, y]:
                return "w"
    elif flag == 'b':
        for i in wboard:
            if i != None and i[:2] == [x, y]:
                return "w"
        for i in bboard:
            if i != None and i[:2] == [x, y]:
                return "b"
    return "empty"

def allMoves(side, wboard, bboard, flag=True):
    if side == "w":
        cnt = -1
        for i in wboard:
            cnt += 1
            if i != None:
                for j in availableMoves(side, wboard, bboard, i, flag):
                    if isOccupied(wboard, bboard, j[0], j[1], "w") != "w":
                        if wboard[cnt] != None:
                            yield [list(wboard[cnt][:2]), j]
    elif side == "b":
        cnt = -1
        for i in bboard:
            cnt += 1
            if i != None:
                for j in availableMoves(side, wboard, bboard, i, flag):
                    if isOccupied(wboard, bboard, j[0], j[1], "b") != "b":
                        if bboard[cnt] != None:
                            yield [list(bboard[cnt][:2]), j]

def isChecked(side, wboard, bboard, pos=None):
    if side == "w":        
        if pos == None:
            pos = wboard[15]              
        for i in allMoves("b", wboard, bboard, False):
            if i[1] == pos[:2]:
                return True
        return False
    else:
        if pos == None:
            pos = bboard[15]              
        for i in allMoves("w", wboard, bboard, False):
            if i[1] == pos[:2]:
                return True
        return False

def isCheckmate(side, wboard, bboard):
    data = [i for i in allMoves(side, wboard, bboard)]
    if side == "w":
        for i in reversed(data):
            if moveTest(side, wboard, bboard, i[0], i[1]):
                return False
        return True
    else:
        for i in reversed(data):
            if moveTest(side, wboard, bboard, i[0], i[1]):
                return False
        return True
    
def castleMoves(side, wboard, bboard, c):
    if side == 'w':
        if not c[0] and not c[2]:
            if isOccupied(wboard, bboard, 2, 8) == \
               isOccupied(wboard, bboard, 3, 8) == \
               isOccupied(wboard, bboard, 4, 8) == "empty":
                if not isChecked('w', wboard, bboard, [3, 8]) and \
                   not isChecked('w', wboard, bboard, [4, 8]):
                    yield [3, 8]
        if not c[0] and not c[3]:
            if isOccupied(wboard, bboard, 6, 8) == \
               isOccupied(wboard, bboard, 7, 8) == "empty":
                if not isChecked('w', wboard, bboard, [6, 8]) and \
                   not isChecked('w', wboard, bboard, [7, 8]):
                    yield [7, 8]
    else:
        if not c[1] and not c[4]:
            if isOccupied(wboard, bboard, 2, 1) == \
               isOccupied(wboard, bboard, 3, 1) == \
               isOccupied(wboard, bboard, 4, 1) == "empty":
                if not isChecked('b', wboard, bboard, [3, 1]) and \
                   not isChecked('b', wboard, bboard, [4, 1]):
                    yield [3, 1]
        if not c[1] and not c[5]:
            if isOccupied(wboard, bboard, 6, 1) == \
               isOccupied(wboard, bboard, 7, 1) == "empty":
                if not isChecked('b', wboard, bboard, [6, 1]) and \
                   not isChecked('b', wboard, bboard, [7, 1]):
                    yield [7, 1]

def availableMoves(side, wboard, bboard, ptype, flag=True, castle=None):
    x, y = ptype[0], ptype[1]
    piece = ptype[2]
    if isOccupied(wboard, bboard, x, y, side) != side:
        return []
    if piece == 'pawn':
        if side == 'w':
            if y == 7 and isOccupied(wboard, bboard, x, 5) == \
               isOccupied(wboard, bboard, x, 6) == "empty":
                if flag:
                    yield [x, 5]
            if isOccupied(wboard, bboard, x + 1, y - 1, side) == "b":
                yield [x + 1, y - 1]
            if isOccupied(wboard, bboard, x - 1, y - 1, side) == "b":
                yield [x - 1, y - 1]
            if isOccupied(wboard, bboard, x, y - 1) == "empty":
                if flag:
                    yield [x, y - 1]
        else:
            if y == 2 and isOccupied(wboard, bboard, x, 4) ==\
               isOccupied(wboard, bboard, x, 3) == "empty":
                if flag:
                    yield [x, 4]
            if isOccupied(wboard, bboard, x + 1, y + 1, side) == "w":
                yield [x + 1, y + 1]
            if isOccupied(wboard, bboard, x - 1, y + 1, side) == "w":
                yield [x - 1, y + 1]
            if isOccupied(wboard, bboard, x, y + 1) == "empty":
                if flag:
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
                if isOccupied(wboard, bboard, x + i, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x + i in range(1, 9) and y - i in range(1, 9):
                yield [x + i, y - i]
                if isOccupied(wboard, bboard, x + i, y - i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y + i in range(1, 9):
                yield [x - i, y + i]
                if isOccupied(wboard, bboard, x - i, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y - i in range(1, 9):
                yield [x - i, y - i]
                if isOccupied(wboard, bboard, x - i, y - i) != "empty":
                    break
    elif piece == 'rook':
        for i in range(1, 8):
            if x + i in range(1, 9) and y in range(1, 9):
                yield [x + i, y]
                if isOccupied(wboard, bboard, x + i, y) != "empty":
                    break
        for i in range(1, 8):
            if x in range(1, 9) and y + i in range(1, 9):
                yield [x, y + i]
                if isOccupied(wboard, bboard, x, y + i) != "empty":
                    break
        for i in range(1, 8):
            if x - i in range(1, 9) and y in range(1, 9):
                yield [x - i, y]
                if isOccupied(wboard, bboard, x - i, y) != "empty":
                    break
        for i in range(1, 8):
            if x in range(1, 9) and y - i in range(1, 9):
                yield [x, y - i]
                if isOccupied(wboard, bboard, x, y - i) != "empty":
                    break
    elif piece == 'queen':
        for i in availableMoves(side, wboard, bboard, [x, y, 'bishop']):
            yield i
        for i in availableMoves(side, wboard, bboard, [x, y, 'rook']):
            yield i
    elif piece == 'king':
        if castle != None:
            for i in castleMoves(side, wboard, bboard, castle):
                yield i
        for i in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                  [x, y - 1], [x, y + 1],
                  [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
            if i[0] in range(1, 9) and i[1] in range(1, 9):
                    yield i
