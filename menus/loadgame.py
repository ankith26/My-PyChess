'''
This file is a part of My-PyChess application.
In this file, we manage the loadgame menu which is called when user clicks
loadgame button on main menu.

We also define functions to save, load and scan for games.
'''

import os
import pygame
from tools.loader import LOADGAME, BACK, putLargeNum, putDT
from tools.utils import rounded_rect

# This function scans for saved games
def scan():
    for i in range(20):
        pth = os.path.join("res", "savedGames", "game" + str(i) + ".txt")
        if os.path.exists(pth):
            with open(pth, "r") as f:
                data = f.read().splitlines()[:2]
            yield (i, data[0].split(" ")[0], data[1])

# This function deletes a game.
def delGame(gameId):
    name = os.path.join("res", "savedGames", "game" + str(gameId) + ".txt")
    if os.path.exists(name):
        os.remove(name)

# This function loads the game, returns the neccessary data
def loadGame(gameId):
    name = os.path.join("res", "savedGames", "game" + str(gameId) + ".txt")
    if os.path.exists(name):
        with open(name, "r") as file:
            lines = file.read().splitlines()

        if len(lines) < 4:
            lines.extend([""] * (4 - len(lines)))
            
        if lines[0].strip() == "multi":
            temp = list(map(int, lines[3].strip().split()))
            if len(temp) == 0:
                return "multi", None, None, lines[2]
            
            elif len(temp) == 1:
                return "multi", temp[0], None, lines[2]
             
            else:
                return "multi", temp[0], temp[1:], lines[2]
                
        else:
            temp = lines[0].strip().split()
            return [temp[0]] + list(map(int, temp[1:])) + [lines[2]]
    else:
        return None
    
# This prompts the user comfirmation while user deletes a game
def prompt(win):
    rounded_rect(win, (255, 255, 255), (110, 160, 280, 130), 10, 4)
    
    win.blit(LOADGAME.MESSAGE[0], (116, 160))
    win.blit(LOADGAME.MESSAGE[1], (118, 190))
          
    win.blit(LOADGAME.YES, (145, 240))
    win.blit(LOADGAME.NO, (305, 240))
    pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
    pygame.draw.rect(win, (255, 255, 255), (300, 240, 46, 28), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 < event.pos[1] < 270:
                    if 140 < event.pos[0] < 200:
                        return True
                    elif 300 < event.pos[0] < 350:
                        return False

# This function shows the screen
def showScreen(win, pg, scanned):
    win.fill((0, 0, 0))
    rounded_rect(win, (255, 255, 255), (70, 15, 340, 60), 15, 4)
    win.blit(BACK, (460, 0))
    win.blit(LOADGAME.HEAD, (100, 18))
    win.blit(LOADGAME.LIST, (125, 80))
    pygame.draw.line(win, (255, 255, 255), (125, 122), (360, 122), 3)
    
    if not scanned:
        win.blit(LOADGAME.EMPTY, (40, 130))
    
    for cnt, i in enumerate(scanned):
        if cnt // 5 == pg:
            num = 60 * (cnt % 5) + 120
            
            rounded_rect(win, (255, 255, 255), (10, num, 480, 50), 10, 3)
            
            win.blit(LOADGAME.GAME, (15, num + 8))
            putLargeNum(win, i[0], (90, num + 8))
            pygame.draw.line(win, (255, 255, 255), (118, num + 5),
                             (118, num + 45), 2)
            
            win.blit(LOADGAME.TYPHEAD, (122, num + 2))
            win.blit(LOADGAME.TYP[i[1]], (122, num + 23))
            pygame.draw.line(win, (255, 255, 255), (226, num + 5),
                             (226, num + 45), 2)
            
            win.blit(LOADGAME.DATE, (230, num + 2))
            win.blit(LOADGAME.TIME, (230, num + 23))
            putDT(win, i[2], (278, num + 2))
            
            rounded_rect(win, (255, 255, 255), (362, num + 5, 40, 40), 6, 2)
            win.blit(LOADGAME.DEL, (366, num + 9))
            rounded_rect(win, (255, 255, 255), (405, num + 5, 80, 40), 6, 2)
            win.blit(LOADGAME.LOAD, (410, num + 10))
    
    rounded_rect(win, (255, 255, 255), (160, 430, 20, 46), 6, 2)
    win.blit(LOADGAME.LEFT, (160, 430))
    rounded_rect(win, (255, 255, 255), (320, 430, 20, 46), 6, 2)
    win.blit(LOADGAME.RIGHT, (320, 430))
        
    rounded_rect(win, (255, 255, 255), (187, 430, 125, 46), 10, 2)
    win.blit(LOADGAME.PAGE[pg], (190, 430))    
    pygame.display.update()

# This is the main function, called by the main menu
def main(win):
    scanned = tuple(scan())
    pages = (len(scanned) - 1) // 5
    pages = max(pages, 0)
    pg = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, pg, scanned)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                if 460 < x < 500 and 0 < y < 50:
                    return 1
                
                if 430 < y < 476:
                    if 160 < x < 180:
                        pg = pages if pg == 0 else pg - 1
                    elif 320 < x < 340:
                        pg = 0 if pg == pages else pg + 1
                
                if 362 < x < 402:
                    for i in range(5):
                        if 120 + 60*i < y < 160 + 60*i:
                            if scanned == tuple(scan()):
                                if 5*pg + i < len(scanned):
                                    if prompt(win):
                                        delGame(scanned[5*pg + i][0])
                                    scanned = tuple(scan())
                                    pages = (len(scanned) - 1) // 5
                                    pages = max(pages, 0)
                                    if pg > pages:
                                        pg = pages                  
                                    break
                            
                elif 405 < x < 485:
                    for i in range(5):
                        if 120 + 60*i < y < 160 + 60*i:
                            newScan = tuple(scan())
                            if 5*pg + i < len(newScan):
                                return loadGame(newScan[5*pg + i][0])
                            