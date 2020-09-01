'''
This file is a part of My-PyChess application.
In this file, we manage the stockfish menu.

This is called from either main menu or singleplayer menu
'''
import os
import platform

import pygame
from ext.pyFish import teststockfish
from tools.loader import STOCKFISH, BACK, putLargeNum
from tools.utils import rounded_rect

# This shows a popup on screen wether stockfish is configured or not.
def install(win, pth):
    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)
    win.blit(STOCKFISH.LOADING, (100, 200))
    pygame.display.update()

    pygame.draw.rect(win, (0, 0, 0), (100, 200, 300, 100))
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 4)

    pygame.draw.rect(win, (255, 255, 255), (220, 270, 65, 20), 2)
    win.blit(STOCKFISH.BACK, (220, 270))

    active = teststockfish(pth)
    if active:
        with open(os.path.join("res", "stockfish", "path.txt"), "w") as f:
            f.write(pth)
        for cnt, i in enumerate(STOCKFISH.SUCCESS):
            win.blit(i, (120, 206 + cnt*17))
    else:
        for cnt, i in enumerate(STOCKFISH.NOSUCCESS):
            win.blit(i, (130, 206 + cnt*17))

    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 < event.pos[0] < 285 and 270 < event.pos[1] < 290:
                    if active:
                        return 1
                    else:
                        return 2

# This shows a prompt if user decides to quit before configuring stockfish
def prompt(win):
    pygame.draw.rect(win, (0, 0, 0), (110, 160, 280, 130))
    pygame.draw.rect(win, (255, 255, 255), (110, 160, 280, 130), 4)

    win.blit(STOCKFISH.PROMPT[0], (130, 170))
    win.blit(STOCKFISH.PROMPT[1], (130, 205))

    win.blit(STOCKFISH.YES, (145, 240))
    win.blit(STOCKFISH.NO, (305, 240))
    pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
    pygame.draw.rect(win, (255, 255, 255), (300, 240, 45, 28), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 200:
                        return True
                    elif 300 < event.pos[0] < 345:
                        return False

# This shows the installation guide screen
def guideScreen(win, OS, pg):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (10, 10, 480, 480), 4)
    win.blit(BACK, (460, 0))

    win.blit(STOCKFISH.TEST, (50, 425))

    pygame.draw.rect(win, (255, 255, 255), (180, 450, 90, 30), 2)
    win.blit(STOCKFISH.INSTALL, (187, 450))

    if OS == "Linux":
        win.blit(STOCKFISH.LIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)

        if pg:
            putLargeNum(win, 1, (380, 15))
            for cnt, i in enumerate(STOCKFISH.LIN_TEXT):
                win.blit(i, (20, 50 + cnt*18))

            pygame.draw.rect(win, (255, 255, 255), (210, 380, 80, 20), 2)
            win.blit(STOCKFISH.CLICK, (210, 380))

        else:
            putLargeNum(win, 2, (380, 15))
            for cnt, i in enumerate(STOCKFISH.LIN_TEXT2):
                win.blit(i, (20, 50 + cnt*18))

    elif OS == "Windows":
        win.blit(STOCKFISH.WIN_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (400, 48), 3)

        for cnt, i in enumerate(STOCKFISH.WIN_TEXT):
            win.blit(i, (20, 60 + cnt*18))

    elif OS == "Darwin":
        win.blit(STOCKFISH.MAC_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (340, 48), 3)

        for cnt, i in enumerate(STOCKFISH.MAC_TEXT):
            win.blit(i, (20, 60 + cnt*18))

    else:
        win.blit(STOCKFISH.OTH_HEAD, (20, 15))
        pygame.draw.line(win, (255, 255, 255), (20, 48), (395, 48), 3)

        for cnt, i in enumerate(STOCKFISH.OTH_TEXT):
            win.blit(i, (20, 50 + cnt*18))

# This a function for managing the stockfish install guide
def guideMain(win):
    OS = platform.system()
    pg = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        guideScreen(win, OS, pg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    if pg and prompt(win):
                        return 1
                    else:
                        pg = True

                if OS == "Linux" and 210 < x < 290 and 380 < y < 400 and pg:
                        pg = False

                if 180 < x < 270 and 450 < y < 480:
                    if (OS == "Linux" and pg) or OS == "Darwin":
                        pth = "stockfish"
                    else:
                        pth = "res/stockfish/build/stockfish"

                    return install(win, pth)
        pygame.display.update()

# This shows the screen
def showScreen(win, configured):
    win.fill((0, 0, 0))

    rounded_rect(win, (255, 255, 255), (40, 10, 395, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)
    win.blit(BACK, (460, 0))
    win.blit(STOCKFISH.HEAD, (50, 12))
    for cnt, i in enumerate(STOCKFISH.TEXT):
        win.blit(i, (15, 90 + cnt*18))

    rounded_rect(win, (255, 255, 255), (120, 320, 250, 30), 6, 3)
    win.blit(STOCKFISH.CONFIG, (120, 320))

    if configured:
        for cnt, i in enumerate(STOCKFISH.CONFIGURED):
            win.blit(i, (15, 360 + cnt*18))
    else:
        for cnt, i in enumerate(STOCKFISH.NONCONFIGURED):
            win.blit(i, (15, 360 + cnt*18))

# This is the main function, called by main menu
def main(win):
    pth = os.path.join("res", "stockfish", "path.txt")
    configured = os.path.exists(pth)
    if configured:
        with open(pth, "r") as f:
            configured = teststockfish(f.read().strip())

    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, configured)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 460 < x < 500 and 0 < y < 50:
                    return 1

                if 120 < x < 370 and 320 < y < 350:
                    if configured:
                        os.remove(pth)
                        configured = False

                    ret = guideMain(win)
                    if ret in [0, 1]:
                        return ret

        pygame.display.update()
