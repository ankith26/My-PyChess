'''
This file is a part of My-PyChess application.
In this file, we manage the about menu which is called when user clicks
about button on main menu.
'''
import webbrowser

import pygame
from tools.loader import HOWTO, BACK
from tools.utils import rounded_rect

LINK = (
    "https://www.instructables.com/id/Playing-Chess/",
    "https://www.chess.com/learn-how-to-play-chess",
    "https://www.instructables.com/id/Learning-to-Play-Chess/",
    "https://www.thechesswebsite.com/learn-to-play-chess/",
    "https://lichess.org/learn#/",
)

# This shows the screen
def showScreen(win):
    win.fill((0, 0, 0))
    rounded_rect(win, (255, 255, 255), (70, 10, 360, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)
    
    # (40, 200, 100, 20) https://www.instructables.com/id/Playing-Chess/
    # (40, 236, 90, 20) https://www.chess.com/learn-how-to-play-chess
    # (40, 272, 160, 20) https://www.instructables.com/id/Learning-to-Play-Chess/
    # (40, 308, 170, 20) https://www.thechesswebsite.com/learn-to-play-chess/
    # (40, 344, 60, 20) https://lichess.org/learn#/

    pygame.draw.line(win, (255, 255, 255), (40, 218), (140, 218), 2)
    pygame.draw.line(win, (255, 255, 255), (40, 254), (130, 254), 2)
    pygame.draw.line(win, (255, 255, 255), (40, 290), (200, 290), 2)
    pygame.draw.line(win, (255, 255, 255), (40, 326), (210, 326), 2)
    pygame.draw.line(win, (255, 255, 255), (40, 362), (100, 362), 2)

    win.blit(HOWTO.HEAD, (100, 12))
    for cnt, i in enumerate(HOWTO.TEXT):
        win.blit(i, (20, 90 + cnt*18))

    win.blit(BACK, (460, 0))
    pygame.display.update()

# This is the main function, called from main menu
def main(win):
    showScreen(win)
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    return 1
                
                if 40 < x < 140 and 200 < y < 220:
                    webbrowser.open(LINK[0])
                
                elif 40 < x < 130 and 236 < y < 256:
                    webbrowser.open(LINK[1])
                
                elif 40 < x < 200 and 272 < y < 292:
                    webbrowser.open(LINK[2])
                
                elif 40 < x < 210 and 308 < y < 328:
                    webbrowser.open(LINK[3])

                elif 40 < x < 100 and 344 < y < 364:
                    webbrowser.open(LINK[4])
