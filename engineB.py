import pygame
import time
import os
from fontloader import MESSAGE1, MESSAGE2, YES, NO, MSG, putNum
from pref import LOAD

def path(name):
    return os.path.join("pieces", name + ".png")

pygame.init()
pygame.display.set_mode((1,1))
WPAWN = pygame.image.load(path("whitePawn")).convert_alpha()
WROOK = pygame.image.load(path("whiteRook")).convert_alpha()
WKNIGHT = pygame.image.load(path("whiteKnight")).convert_alpha()
WBISHOP = pygame.image.load(path("whiteBishop")).convert_alpha()
WQUEEN = pygame.image.load(path("whiteQueen")).convert_alpha()
WKING = pygame.image.load(path("whiteKing")).convert_alpha()

BPAWN = pygame.image.load(path("blackPawn")).convert_alpha()
BROOK = pygame.image.load(path("blackRook")).convert_alpha()
BKNIGHT = pygame.image.load(path("blackKnight")).convert_alpha()
BBISHOP = pygame.image.load(path("blackBishop")).convert_alpha()
BQUEEN = pygame.image.load(path("blackQueen")).convert_alpha()
BKING = pygame.image.load(path("blackKing")).convert_alpha()
pygame.quit()

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

def drawBoard(win):
    colour = LOAD[5]
    pygame.draw.rect(win, colour, (0, 0, 500, 50))
    pygame.draw.rect(win, colour, (0, 0, 50, 500))
    pygame.draw.rect(win, colour, (450, 0, 50, 500))
    pygame.draw.rect(win, colour, (0, 450, 450, 50))
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                colour = (255, 255, 255)
            else:
                colour = (181, 101, 29)
            pygame.draw.rect(
                win, colour, (50 * (x + 1), 50 * (y + 1), 50, 50))

def drawPieces(win, wboard, bboard):
    for x in wboard:
        if x is not None:
            if x[2] == 'pawn':
                win.blit(WPAWN, (x[0] * 50, x[1] * 50))
            if x[2] == 'knight':
                win.blit(WKNIGHT, (x[0] * 50, x[1] * 50))
            if x[2] == 'bishop':
                win.blit(WBISHOP, (x[0] * 50, x[1] * 50))
            if x[2] == 'rook':
                win.blit(WROOK, (x[0] * 50, x[1] * 50))
            if x[2] == 'queen':
                win.blit(WQUEEN, (x[0] * 50, x[1] * 50))
            if x[2] == 'king':
                win.blit(WKING, (x[0] * 50, x[1] * 50))
    for x in bboard:
        if x is not None:
            if x[2] == 'pawn':
                win.blit(BPAWN, (x[0] * 50, x[1] * 50))
            if x[2] == 'knight':
                win.blit(BKNIGHT, (x[0] * 50, x[1] * 50))
            if x[2] == 'bishop':
                win.blit(BBISHOP, (x[0] * 50, x[1] * 50))
            if x[2] == 'rook':
                win.blit(BROOK, (x[0] * 50, x[1] * 50))
            if x[2] == 'queen':
                win.blit(BQUEEN, (x[0] * 50, x[1] * 50))
            if x[2] == 'king':
                win.blit(BKING, (x[0] * 50, x[1] * 50))
        
def animate(win, side, wboard, bboard, lst, to):
    fro = lst[:2]
    ptype = lst[2]
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
    stepx = (x2 - x1)*(5/2)
    stepy = (y2 - y1)*(5/2)
    for i in range(21):
        drawBoard(win)
        drawPieces(win, wboard, bboard)
        if (x1 +y1) % 2 == 0:
            pygame.draw.rect(win, (255,255,255), (x1*50, y1*50, 50, 50))
        else:
            pygame.draw.rect(win, (181, 101, 29), (x1*50, y1*50, 50, 50))
        win.blit(piece, (x1*50+(i*stepx), y1*50+(i*stepy)))
        time.sleep(0.01)
        pygame.display.update((0, 50, 500, 450))
    drawBoard(win)
    return

def prompt(win, msg=""):
    pygame.draw.rect(win, (0,0,0), (70, 140, 360, 180))
    pygame.draw.rect(win, (255,255,255), (70, 140, 360, 180), 4)
    win.blit(MESSAGE1, (92,140))
    win.blit(MESSAGE2, (142,180))
    if msg != "":
        win.blit(MSG, (80, 280))
        putNum(win, msg, (320, 280), False)
          
    win.blit(YES, (100, 240))
    win.blit(NO, (340,240))
    pygame.draw.rect(win, (255,255,255), (85, 140, 330, 82), 2)
    pygame.draw.rect(win, (255,255,255), (100, 240, 60, 30), 2)
    pygame.draw.rect(win, (255,255,255), (340, 240, 50, 30), 2)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 240 < y < 270:
                    if 100 < x < 160:
                        return True
                    elif 340 < x < 390:
                        return False