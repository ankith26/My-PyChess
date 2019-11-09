import pygame
from myutils import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((460, 460))
pygame.display.set_caption('Chess')
running = True

wmove = True
x = y = -100
sel = [0, 0]
prevsel = [0, 0]
wcheckmate = bcheckmate = stalemate = False
def drawBoard(win):
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
def drawPieces(win):
    a = 0
    for x in wBoard:
        if x != None:
            if a in range(8): win.blit(wpawn, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(8,10): win.blit(wrook, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(10,12): win.blit(wknight, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(12,14): win.blit(wbishop, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a == 14: win.blit(wqueen, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a == 15: win.blit(wking, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
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
            if a in range(8): win.blit(bpawn, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(8,10): win.blit(brook, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(10,12): win.blit(bknight, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a in range(12,14): win.blit(bbishop, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a == 14: win.blit(bqueen, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
            elif a == 15: win.blit(bking, ((x[0]-1)*50 + 30, (x[1]-1)*50 + 30))
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
while running:
    clock.tick(24)
    drawBoard(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 30<x<430 and 30<y<430:
                x = ((x - 30) // 50) + 1
                y = ((y - 30) // 50) + 1
                prevsel = sel
                sel = [x, y]
            else: sel = [0, 0]
            
    if wmove and sel != [0, 0]:
        if isChecked("w") and isCheckmate("w"):
            wcheckmate = True
            running = False
        else:
            stalemate = True
            for i in allMoves("w"):
                if i[0] == 15:
                    if not isChecked("w", i[1]):
                        stalemate = False
                else: stalemate = False
        for i in range(len(wBoard)):          
            if wBoard[i] != None and prevsel == wBoard[i][:2]:
                if isOccupied(sel[0], sel[1]) != "w":
                    ptype = getPiece("w", prevsel)
                    if sel in availableMoves("w", ptype, prevsel):
                        if move("w", prevsel, sel): wmove = False
                        else: wmove = True
                        doRoutine()
    elif sel != [0, 0]:
        if isChecked("b") and isCheckmate("b"):
            bcheckmate = True
            running = False
        else:
            stalemate = True
            for i in allMoves("b"):
                if i[0] == 15:
                    if not isChecked("b", i[1]):
                        stalemate = False
                else: stalemate = False
        for i in range(len(bBoard)):
            if bBoard[i] != None and prevsel == bBoard[i][:2]:
                if isOccupied(sel[0], sel[1]) != "b":
                    ptype = getPiece("b", prevsel)
                    if sel in availableMoves("b", ptype, prevsel):
                        if move("b", prevsel, sel): wmove = True
                        else: wmove = False
                        doRoutine()
    if stalemate:
        running = False
    pygame.draw.rect(win, (255,255,0), (x*50-20, y*50-20, 50, 50))
    drawPieces(win)
    pygame.display.update()
if wcheckmate: print("CHECKMATE! White lost")
elif bcheckmate: print("CHECKMATE! Black lost")
elif stalemate: print("DRAW by STALEMATE")
pygame.quit()
