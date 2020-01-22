import pygame
import random
from engineA import *
from engineB import *

from fontloader import CHECK, CHECKMATE, LOST, STALEMATE, CHOOSE, SAVE

from pref import LOAD

def showAvailMoves(win, side, wboard, bboard, ptype, castle):
    if LOAD[3]:
        for i in availableMoves(side, wboard, bboard, ptype, castle):
            if isOccupied(wboard, bboard, i) != side:
                if moveTest(side, wboard, bboard, ptype[:2], i):
                    x = i[0]*50 + 20
                    y = i[1]*50 + 20
                    pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))

def automove(win, side, wboard, bboard, anim):
    data = [i for i in allMoves(side, wboard, bboard)]
    bestmove = data[random.randint(0,len(data)-1)]
    if moveTest(side, wboard, bboard, bestmove[0], bestmove[1]):
        piece = bestmove[0] + [getType(bboard, bestmove[0])]
        if anim:
            animate(win, side, wboard, bboard, piece, bestmove[1])
        return move(side, wboard, bboard, bestmove[0], bestmove[1])
    else:
        return automove(win, side, wboard, bboard, anim)

def main(win, wmove, wBoard, bBoard, castle):
    anim = LOAD[0]
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
                    msg=saveGame(wmove, wBoard, bBoard, castle, "single")
                    pygame.display.update
                    return prompt(win, msg)
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
                    if isOccupied(wBoard, bBoard, sel) != "w":
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
                                if anim:
                                    animate(win, "w", wBoard, bBoard,
                                            piece, sel)
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
                    wBoard, bBoard = automove(win, "b", wBoard, bBoard, anim)
                    sel = [-1,-1]
                    wmove = True
            if wmove and isOccupied(wBoard, bBoard, sel) == "w":
                pygame.draw.rect(win, (255, 255, 0), (x * 50,
                                                      y * 50, 50, 50))
            drawPieces(win, wBoard, bBoard)
            if wmove:
                seltype = sel + [getType(wBoard, sel)]
                if seltype in wBoard:
                    showAvailMoves(win, "w", wBoard, bBoard, seltype, castle)
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
