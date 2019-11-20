import pygame
from myutils import *
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
                win, colour, (50 + (x * 50), 50 + (y * 50), 50, 50))

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

CHECKMATE = pygame.image.load("images/checkmate.png")
STALEMATE = pygame.image.load("images/stalemate.png")
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

def main(win):
    clock = pygame.time.Clock()
    wmove = True
    x = y = -100
    sel = [0, 0]
    prevsel = [0, 0]
    end = [False]
    
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 < x < 450 and 50 < y < 450:
                    x = x // 50
                    y = y // 50
                    prevsel = sel
                    sel = [x, y]
                else:
                    sel = [0, 0]
        if not end[0]:
            drawBoard(win)
            if wmove and sel != [0, 0]:
                if isChecked("w") and isCheckmate("w"):
                    end = [True, "w"]
                else:
                    for i in allMoves("w"):
                        if i[0] == 15:
                            if not isChecked("w", i[1]):
                                break
                        else:
                            break
                    else:
                        end = [True, "s"]
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
                    end = [True, "b"]
                else:
                    for i in allMoves("b"):
                        if i[0] == 15:
                            if not isChecked("b", i[1]):
                                break
                        else:
                            break
                    else:
                        end = [True, "s"]
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
            if wmove and isOccupied(sel[0], sel[1]) == "w":
                pygame.draw.rect(win, (255, 255, 0), (x * 50,
                                                      y * 50, 50, 50))
            if not wmove and isOccupied(sel[0], sel[1]) == "b":
                pygame.draw.rect(win, (255, 255, 0), (x * 50,
                                                      y * 50, 50, 50))
            drawPieces(win)
        else:
            if end[1] == "w":
                win.blit(CHECKMATE,(130,0))
                win.blit(WKING,(270,0))
            elif end[1] == "b":
                win.blit(CHECKMATE,(130,0))
                win.blit(BKING,(270,0))
            elif end[1] == "s":
                win.blit(STALEMATE,(120,0))
        pygame.display.update()
