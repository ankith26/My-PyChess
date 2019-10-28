import pygame
#these are initial pos           
wBoard = [[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],# pawns
          [1,8],[8,8],[2,8],[7,8],[3,8],[6,8],#rooks,knights and bishops
          [4,8],[5,8]#Queen and king
          ]
bBoard = [[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],# pawns
          [1,1],[8,1],[2,1],[7,1],[3,1],[6,1],#rooks,knights and bishops
          [4,1],[5,1]#Queen and king
          ]
wKingMoved = bKingMoved = False
wRook1Moved = bRook1Moved = False
wRook2Moved = bRook2Moved = False

wpawn = pygame.image.load("images/whitePawn.png")
wrook = pygame.image.load("images/whiteRook.png")
wknight = pygame.image.load("images/whiteKnight.png")
wbishop = pygame.image.load("images/whiteBishop.png")
wqueen = pygame.image.load("images/whiteQueen.png")
wking = pygame.image.load("images/whiteKing.png")
bpawn = pygame.image.load("images/blackPawn.png")
brook = pygame.image.load("images/blackRook.png")
bknight = pygame.image.load("images/blackKnight.png")
bbishop = pygame.image.load("images/blackBishop.png")
bqueen = pygame.image.load("images/blackQueen.png")
bking = pygame.image.load("images/blackKing.png")
def getchoice():
    return "queen"
def drawboard(win):
    colour = (255, 0, 255)
    pygame.draw.rect(win, colour, (0, 0, 460, 30))
    pygame.draw.rect(win, colour, (0, 0, 30, 460))
    pygame.draw.rect(win, colour, (430, 0, 30, 460))
    pygame.draw.rect(win, colour, (0, 430, 460, 30))
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0: colour = (255, 255, 255)
            else: colour = (181,101,29)
            pygame.draw.rect(win, colour, (30+(x*50), 30+(y*50), 50, 50))
def getpiece(colour, pos):
    if colour == "w": Board = wBoard
    elif colour == "b": Board = bBoard
    for i in range(len(Board)):
        if Board[i] != None and Board[i][:2] == pos:
            if i in range(8): return colour + "pawn"
            elif i in range(8,10): return colour + "rook"
            elif i in range(10,12): return colour + "knight"
            elif i in range(12,14): return colour + "bishop"
            elif i == 14: return colour + "queen"
            elif i == 15: return colour + "king"
            else: return colour + Board[i][2]
def move(colour, fro, to, var = True):
    global wBoard, bBoard
    val = -1
    if colour == "w":
        for i in range(len(bBoard)):
            if bBoard[i] != None and bBoard[i][:2] == to:
                bBoard[i] = None
                val = i
        for i in range(len(wBoard)):
            if wBoard[i] != None and wBoard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2: move("w", [1,8], [4,8])
                    elif fro[0] - to[0] == -2: move("w", [8,8], [6,8])             
                wBoard[i][:2] = to          
                if i in range(8):
                    if to[1] == 1:
                        wBoard[i] = None
                        wBoard.append([to[0], 1, getchoice()])
        if is_checked(colour) and var:
            move(colour, to, fro, False)
            if val != -1: bBoard[val] = to
            return False
        else: return True
    elif colour == "b":
        for i in range(len(wBoard)):
            if wBoard[i] != None and wBoard[i][:2] == to:
                wBoard[i] = None
                val = i
        for i in range(len(bBoard)):
            if bBoard[i] != None and bBoard[i][:2] == fro:
                if i == 15:
                    if fro[0] - to[0] == 2: move("b", [1,1], [4,1])
                    elif fro[0] - to[0] == -2: move("b", [8,1], [6,1])             
                bBoard[i][:2] = to          
                if i in range(8):
                    if to[1] == 1:
                        bBoard[i] = None
                        bBoard.append([to[0], 1, getchoice()])
        if is_checked(colour) and var:
            move(colour, to, fro, False)
            if val != -1: wBoard[val] = to
            return False
        else: return True
def doroutine():
    global wKingMoved,bKingMoved,wRook1Moved,wRook2Moved,bRook1Moved,bRook2Moved
    if wBoard[15] != [5,8]: wKingMoved = True
    if bBoard[15] != [5,1]: bKingMoved = True
    if wBoard[8] != [1,8]: wRook1Moved = True
    if wBoard[9] != [8,8]: wRook2Moved = True
    if bBoard[8] != [1,1]: bRook1Moved = True
    if bBoard[9] != [8,1]: bRook2Moved = True
def drawpieces(win):
    a = 0
    for x in wBoard:
        if x != None:
            if a in range(8): win.blit(wpawn, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(8,10): win.blit(wrook, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(10,12): win.blit(wknight, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(12,14): win.blit(wbishop, (x[0]*50 - 20, x[1]*50 - 20))
            elif a == 14: win.blit(wqueen, (x[0]*50 - 20, x[1]*50 - 20))
            elif a == 15: win.blit(wking, (x[0]*50 - 20, x[1]*50 - 20))
            else:
                if x[2] == 'knight':
                    win.blit(wknight, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'bishop':
                    win.blit(wbishop, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'rook':
                    win.blit(wrook, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'queen':
                    win.blit(wqueen, (x[0]*50 - 20, x[1]*50 - 20))
        a += 1
    a = 0
    for x in bBoard:
        if x != None:
            if a in range(8): win.blit(bpawn, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(8,10): win.blit(brook, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(10,12): win.blit(bknight, (x[0]*50 - 20, x[1]*50 - 20))
            elif a in range(12,14): win.blit(bbishop, (x[0]*50 - 20, x[1]*50 - 20))
            elif a == 14: win.blit(bqueen, (x[0]*50 - 20, x[1]*50 - 20))
            elif a == 15: win.blit(bking, (x[0]*50 - 20, x[1]*50 - 20))
            else:
                if x[2] == 'knight':
                    win.blit(bknight, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'bishop':
                    win.blit(bbishop, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'rook':
                    win.blit(brook, (x[0]*50 - 20, x[1]*50 - 20))
                if x[2] == 'queen':
                    win.blit(bqueen, (x[0]*50 - 20, x[1]*50 - 20))
        a += 1
def isoccupied(*pos):
    for i in bBoard:
        if i != None and i[:2] == list(pos): return "black"      
    for i in wBoard:
        if i != None and i[:2] == list(pos): return "white"
    return "empty"
def allmoves(side):
    a = 0
    if side == 'w': var = wBoard
    elif side == 'b': var = bBoard
    for i in var:
        if i != None:
            if a in range(8) and side == 'w':
                if i[0]+1 in range(1,9) and i[1]+1 in range(1,9):
                    yield [a,[i[0]+1, i[1]-1]]
                if i[0]-1 in range(1,9) and i[1]+1 in range(1,9):
                    yield [a,[i[0]-1, i[1]-1]]
                if i[1] == 7 and isoccupied(i[0],5) == isoccupied(i[0],6) == "empty":
                    yield [a,[i[0], 5], True]
                if isoccupied(i[0], i[1]-1) == "empty":
                    yield [a,[i[0], i[1]-1], True]
            elif a in range(8) and side == 'b':
                if i[0]+1 in range(1,9) and i[1]-1 in range(1,9):
                    yield [a,[i[0]+1, i[1]+1]]
                if i[0]-1 in range(1,9) and i[1]-1 in range(1,9):
                    yield [a,[i[0]-1, i[1]+1]]
                if i[1] == 2 and isoccupied(i[0],3) == isoccupied(i[0],4) == "empty":
                    yield [a,[i[0], 4], True]
                if isoccupied(i[0], i[1]+1) == "empty":
                    yield [a,[i[0], i[1]+1], True]
            elif a in range(8,10):
                for j in availableMoves(side+'rook', i): yield [a,j]
            elif a in range(10,12):
                for j in availableMoves(side+'knight', i): yield [a,j]
            elif a in range(12,14):
                for j in availableMoves(side+'bishop', i): yield [a,j]
            elif a == 14:
                for j in availableMoves(side+'queen', i): yield [a,j]
            elif a == 15:
                x,y = i[0],i[1]
                for j in [[x-1,y-1], [x-1,y], [x-1,y+1],
                            [x,y-1], [x,y+1],
                            [x+1,y-1], [x+1,y], [x+1,y+1]]:
                    if j[0] in range(1,9) and j[1] in range(1,9): yield [a,j]
            else:
                for j in availableMoves(side+i[2], i[:2]): yield [a,j]
        a += 1
def is_checked(side, pos=None):
    if side == 'w':
        if pos == None: pos = wBoard[15]
        side = 'b'
    elif side == 'b':
        if pos == None: pos = bBoard[15]
        side = 'w'
    for i in allmoves(side):
        if i[1] == pos and len(i) != 3: return True
    return False
def availableMoves(ptype, pos):
    x, y = pos[0], pos[1]
    side, piece = ptype[0], ptype[1:]  
    if piece == 'pawn':
        if side == 'w':
            if y == 7 and isoccupied(x,5) == isoccupied(x,6) == "empty":
                yield [x, 5]
            if isoccupied(x+1, y-1) == "black": yield [x+1, y-1]
            if isoccupied(x-1, y-1) == "black": yield [x-1, y-1]
            if isoccupied(x, y-1) == "empty": yield [x, y-1]
        else:
            if y == 2 and isoccupied(x,4) == isoccupied(x,3) == "empty":
                yield [x, 4]
            if isoccupied(x+1, y+1) == "white": yield [x+1, y+1]
            if isoccupied(x-1, y+1) == "white": yield [x-1, y+1]
            if isoccupied(x, y+1) == "empty": yield [x, y+1]
    elif piece == 'knight':
        for i in [[x+1,y+2], [x+1,y-2], [x-1,y+2], [x-1,y-2],
                  [x+2,y+1], [x+2,y-1], [x-2,y+1], [x-2,y-1]]:
            if i[0] in range(1,9) and i[1] in range(1,9): yield i      
    elif piece == 'bishop':
        for i in range(1,8):
            if x+i in range(1,9) and y+i in range(1,9):
                if isoccupied(x+i,y+i) != "empty":
                    yield [x+i,y+i]
                    break
                else: yield [x+i, y+i]
        for i in range(1,8):
            if x+i in range(1,9) and y-i in range(1,9):
                if isoccupied(x+i,y-i) != "empty":
                    yield [x+i,y-i]
                    break
                else: yield [x+i, y-i]
        for i in range(1,8):
            if x-i in range(1,9) and y+i in range(1,9):
                if isoccupied(x-i,y+i) != "empty":
                    yield [x-i,y+i]
                    break
                else: yield [x-i, y+i]
        for i in range(1,8):
            if x-i in range(1,9) and y-i in range(1,9):
                if isoccupied(x-i,y-i) != "empty":
                    yield [x-i,y-i]
                    break
                else: yield [x-i, y-i]
    elif piece == 'rook':
        for i in range(1,8):
            if x+i in range(1,9) and y in range(1,9):
                if isoccupied(x+i,y) != "empty":
                    yield [x+i,y]
                    break
                else: yield [x+i, y]
        for i in range(1,8):
            if x in range(1,9) and y+i in range(1,9):
                if isoccupied(x,y+i) != "empty":
                    yield [x,y+i]
                    break
                else: yield [x, y+i]        
        for i in range(1,8):
            if x-i in range(1,9) and y in range(1,9):
                if isoccupied(x-i,y) != "empty":
                    yield [x-i,y]
                    break
                else: yield [x-i, y]          
        for i in range(1,8):
            if x in range(1,9) and y-i in range(1,9):
                if isoccupied(x,y-i) != "empty":
                    yield [x,y-i]
                    break
                else: yield [x, y-i]
    elif piece == 'queen':
        for i in availableMoves(side + 'bishop', pos): yield i
        for i in availableMoves(side + 'rook', pos): yield i
    elif piece == 'king':
        if side == 'w':
            if not wKingMoved and not wRook1Moved:
                if isoccupied(2,8) == isoccupied(3,8) == isoccupied(4,8) == "empty":
                    if not is_checked('w',[3,8]) and not is_checked('w',[4,8]):
                        if not is_checked(side): yield [3,8]
            if not wKingMoved and not wRook2Moved:
                if isoccupied(6,8) == isoccupied(7,8) == "empty":
                    if not is_checked('w',[6,8]) and not is_checked('w',[7,8]):
                        if not is_checked(side): yield [7,8]
        else:
            if not bKingMoved and not bRook1Moved:
                if isoccupied(2,1) == isoccupied(3,1) == isoccupied(4,1) == "empty":
                    if not is_checked('b',[3,1]) and not is_checked('b',[4,1]):
                        if not is_checked(side): yield [3,1]
            if not bKingMoved and not bRook2Moved:
                if isoccupied(6,1) == isoccupied(7,1) == "empty":
                    if not is_checked('b',[6,1]) and not is_checked('b',[7,1]):
                        if not is_checked(side): yield [7,1]
        for i in [[x-1,y-1], [x-1,y], [x-1,y+1],
                    [x,y-1], [x,y+1],
                    [x+1,y-1], [x+1,y], [x+1,y+1]]:
            if not is_checked(side, i):
                if i[0] in range(1, 9) and i[1] in range(1,9): yield i
    else: pass
