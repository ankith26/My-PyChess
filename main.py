import pygame
from myutils import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((460, 460))
pygame.display.set_caption('Chess')

wmove = True
x = y = -100
sel = [0, 0]
prevsel = [0, 0]
wCheckmate = bCheckmate = stalemate = False

def drawBoard(win):
    colour = (255, 0, 255)
    pygame.draw.rect(win, colour, (0, 0, 460, 30))
    pygame.draw.rect(win, colour, (0, 0, 30, 460))
    pygame.draw.rect(win, colour, (430, 0, 30, 460))
    pygame.draw.rect(win, colour, (0, 430, 460, 30))
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                colour = (255, 255, 255)
            else:
                colour = (181, 101, 29)
            pygame.draw.rect(
                win, colour, (30 + (x * 50), 30 + (y * 50), 50, 50))

WPAWN = pygame.image.load("images/whitePawn.png")
WROOK = pygame.image.load("images/whiteRook.png")
WKNIGHT = pygame.image.load("images/whiteKnight.png")
WBISHOP = pygame.image.load("images/whiteBishop.png")
WQUEEN = pygame.image.load("images/whiteQueen.png")
WKING = pygame.image.load("images/whiteKing.png")
BPAWN = pygame.image.load("images/blackPawn.png")
BROOK = pygame.image.load("images/blackRook.png")
BKNIGHT = pygame.image.load("images/blackKnight.png")
BBISHOP = pygame.image.load("images/blackBishop.png")
BQUEEN = pygame.image.load("images/blackQueen.png")
BKING = pygame.image.load("images/blackKing.png")

def drawPieces(win):
    count = 0
    for x in wBoard:
        if x is not None:
            if count in range(8):
                win.blit(WPAWN, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(8, 10):
                win.blit(WROOK, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(10, 12):
                win.blit(WKNIGHT, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(12, 14):
                win.blit(WBISHOP, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count == 14:
                win.blit(WQUEEN, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count == 15:
                win.blit(WKING, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            else:
                if x[2] == 'knight':
                    win.blit(WKNIGHT, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'bishop':
                    win.blit(WBISHOP, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'rook':
                    win.blit(WROOK, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'queen':
                    win.blit(WQUEEN, (x[0] * 50 - 20, x[1] * 50 - 20))
        count += 1
    count = 0
    for x in bBoard:
        if x is not None:
            if count in range(8):
                win.blit(BPAWN, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(8, 10):
                win.blit(BROOK, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(10, 12):
                win.blit(BKNIGHT, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count in range(12, 14):
                win.blit(BBISHOP, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count == 14:
                win.blit(BQUEEN, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            elif count == 15:
                win.blit(BKING, ((x[0] - 1) * 50 + 30, (x[1] - 1) * 50 + 30))
            else:
                if x[2] == 'knight':
                    win.blit(BKNIGHT, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'bishop':
                    win.blit(BBISHOP, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'rook':
                    win.blit(BROOK, (x[0] * 50 - 20, x[1] * 50 - 20))
                if x[2] == 'queen':
                    win.blit(BQUEEN, (x[0] * 50 - 20, x[1] * 50 - 20))
        count += 1

while True:
    clock.tick(24)
    drawBoard(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 30 < x < 430 and 30 < y < 430:
                x = ((x - 30) // 50) + 1
                y = ((y - 30) // 50) + 1
                prevsel = sel
                sel = [x, y]
            else:
                sel = [0, 0]

    if wmove and sel != [0, 0]:
        if isChecked("w") and isCheckmate("w"):
            wCheckmate = True
            break
        else:
            stalemate = True
            for i in allMoves("w"):
                if i[0] == 15:
                    if not isChecked("w", i[1]):
                        stalemate = False
                else:
                    stalemate = False
        for i in range(len(wBoard)):
            if wBoard[i] is not None and prevsel == wBoard[i][:2]:
                if isOccupied(sel[0], sel[1]) != "w":
                    ptype = getPiece("w", prevsel)
                    if sel in availableMoves("w", ptype, prevsel):
                        if move("w", prevsel, sel):
                            wmove = False
                        else:
                            wmove = True
                        doRoutine()
    elif sel != [0, 0]:
        if isChecked("b") and isCheckmate("b"):
            bCheckmate = True
            break
        else:
            stalemate = True
            for i in allMoves("b"):
                if i[0] == 15:
                    if not isChecked("b", i[1]):
                        stalemate = False
                else:
                    stalemate = False
        for i in range(len(bBoard)):
            if bBoard[i] is not None and prevsel == bBoard[i][:2]:
                if isOccupied(sel[0], sel[1]) != "b":
                    ptype = getPiece("b", prevsel)
                    if sel in availableMoves("b", ptype, prevsel):
                        if move("b", prevsel, sel):
                            wmove = True
                        else:
                            wmove = False
                        doRoutine()
    if stalemate:
        break
    if wmove and isOccupied(sel[0], sel[1]) == "w":
        pygame.draw.rect(win, (255, 255, 0), (x * 50 - 20, y * 50 - 20, 50, 50))
    if not wmove and isOccupied(sel[0], sel[1]) == "b":
        pygame.draw.rect(win, (255, 255, 0), (x * 50 - 20, y * 50 - 20, 50, 50))
    drawPieces(win)
    pygame.display.update()
if wCheckmate:
    print("CHECKMATE! White lost")
elif bCheckmate:
    print("CHECKMATE! Black lost")
elif stalemate:
    print("DRAW by STALEMATE")
pygame.quit()
