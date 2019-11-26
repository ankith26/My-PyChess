import pygame
from myutils import *
def main(win):
    clock = pygame.time.Clock()
    wmove = True
    x = y = -100
    sel = [0, 0]
    prevsel = [0, 0]
    end = [False]
    CHECK = pygame.image.load("images/check.png")
    
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
            if wmove:
                if isChecked("w") and not isCheckmate("w"):
                    win.blit(CHECK, (180,0))
            else:
                if isChecked("b") and not isCheckmate("b"):
                    win.blit(CHECK, (180,0))
                    
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
                                if ptype == "pawn" and sel[1] == 1:
                                    drawPieces(win)
                                    win.blit(CHOOSE, (0,0))
                                    win.blit(WQUEEN, (230, 0))
                                    win.blit(WBISHOP, (280, 0))
                                    win.blit(WROOK, (330, 0))
                                    win.blit(WKNIGHT, (380, 0))
                                    pygame.display.update()
                                if move("w", prevsel, sel):
                                    wmove = False
                                    animate(win, "w", ptype, prevsel, sel)
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
                                if ptype == "pawn" and sel[1] == 8:
                                    drawPieces(win)
                                    win.blit(CHOOSE, (0,0))
                                    win.blit(BQUEEN, (230, 0))
                                    win.blit(BBISHOP, (280, 0))
                                    win.blit(BROOK, (330, 0))
                                    win.blit(BKNIGHT, (380, 0))
                                    pygame.display.update()
                                if move("b", prevsel, sel):
                                    wmove = True
                                    animate(win, "b", ptype, prevsel, sel)
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
