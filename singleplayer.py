import pygame
import random
from engineA import *
from engineB import *

from fontloader import CHECK, CHECKMATE, LOST, STALEMATE, CHOOSE, SAVE

def automove(win, side, wboard, bboard):
    data = [i for i in allMoves(side, wboard, bboard)]
    bestmove = data[random.randint(0,len(data)-1)]
    if moveTest(side, wboard, bboard, bestmove[0], bestmove[1]):
        piece = bestmove[0] + [getType(bboard, bestmove[0])]
        animate(win, side, wboard, bboard, piece, bestmove[1])
        return move(side, wboard, bboard, bestmove[0], bestmove[1])
    else:
        return automove(win, side, wboard, bboard)

def main(win, wmove, wBoard, bBoard, castle):
    clock = pygame.time.Clock()
    x = y = -100
    sel = [0, 0]
    prevsel = [0, 0]
    end = [False]
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return prompt(win)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    prevsel = sel
                    sel = [x, y]
                elif 330 < x < 500 and 460 < y < 490:
                    saveGame(wmove, wBoard, bBoard, castle, "single")
                    return prompt(win)
        if not end[0]:
            drawBoard(win)
            win.blit(SAVE,(330,460))
            if wmove:
                if isChecked("w", wBoard, bBoard):
                    if isCheckmate("w", wBoard, bBoard):
                        end = [True, "w"]
                    else:
                        win.blit(CHECK, (180,10))
                else:
                    for i in allMoves("w", wBoard, bBoard):
                        if i[0] == wBoard[15][:2]:
                            if not isChecked("w", wBoard, bBoard, i[1]):
                                break
                        else:
                            break
                    else:
                        end = [True, "s"]
                piece = [prevsel[0], prevsel[1], getType(wBoard, prevsel)]
                if piece in wBoard:
                    if isOccupied(wBoard, bBoard, sel[0], sel[1]) != "w":
                        if sel in availableMoves("w", wBoard, bBoard, piece,
                                                 castle=castle):
                            castle = doRoutine(wBoard, bBoard, castle)
                            if piece[2] == "pawn" and sel[1] == 1:
                                drawPieces(win, wBoard, bBoard)
                                win.blit(CHOOSE, (70,10))
                                win.blit(WQUEEN, (230, 0))
                                win.blit(WBISHOP, (280, 0))
                                win.blit(WROOK, (330, 0))
                                win.blit(WKNIGHT, (380, 0))
                                pygame.display.update()
                            if moveTest("w", wBoard, bBoard, prevsel, sel):
                                wmove = False
                                animate(win, "w", wBoard, bBoard, piece, sel)
                                wBoard, bBoard = move("w", wBoard, bBoard,
                                                      prevsel, sel)
            else:
                if isChecked("b", wBoard, bBoard):
                    if isCheckmate("b", wBoard, bBoard):
                        end = [True, "b"]
                    else:
                        win.blit(CHECK, (180,10))
                else:
                    for i in allMoves("b", wBoard, bBoard):
                        if i[0] == bBoard[15][:2]:
                            if not isChecked("b", wBoard, bBoard, i[1]):
                                break
                        else:
                            break
                    else:
                        end = [True, "s"]
                if not end[0]:
                    castle = doRoutine(wBoard, bBoard, castle)
                    wBoard, bBoard = automove(win, "b", wBoard, bBoard)
                    sel = [-1,-1]
                    wmove = True
            if wmove and isOccupied(wBoard, bBoard, sel[0], sel[1]) == "w":
                pygame.draw.rect(win, (255, 255, 0), (x * 50,
                                                      y * 50, 50, 50))
            if not wmove and isOccupied(wBoard, bBoard, sel[0], sel[1]) == "b":
                pygame.draw.rect(win, (255, 255, 0), (x * 50,
                                                      y * 50, 50, 50))
            drawPieces(win, wBoard, bBoard)
        else:
            if end[1] == "w":
                win.blit(CHECKMATE,(60,10))
                win.blit(WKING,(280,0))
                win.blit(LOST,(330,10))
            elif end[1] == "b":
                win.blit(CHECKMATE,(60,10))
                win.blit(BKING,(280,0))
                win.blit(LOST,(330,10))
            elif end[1] == "s":
                win.blit(STALEMATE,(130,10))
        pygame.display.update()
