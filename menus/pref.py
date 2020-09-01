'''
This file is a part of My-PyChess application.
In this file, we manage the preferences menu which is called when user clicks
preferences button on main menu.

We also define functions to save and load user preferences.
'''

import os.path
import pygame
from tools.loader import PREF, BACK
from tools.utils import rounded_rect

KEYS = ["sounds", "flip", "slideshow", "show_moves", "allow_undo", "show_clock"]

DEFAULTPREFS = {
    "sounds": False,
    "flip": False,
    "slideshow": True,
    "show_moves": True,
    "allow_undo": True,
    "show_clock": False
}

# This function saves user preferences in a text file.
def save(load):
    with open(os.path.join("res", "preferences.txt"), "w") as f:
        for key, val in load.items():
            f.write(key + " = " + str(val) + '\n')

# This function loads user preferences from a text file
def load():
    path = os.path.join("res", "preferences.txt")
    if not os.path.exists(path):
        open(path, "w").close()
    
    with open(path, "r") as f:
        mydict = {}
        for line in f.read().splitlines():
            lsplit = line.split("=")
            if len(lsplit) == 2: 
                val = lsplit[1].strip().lower()
                if val == "true":
                    mydict[lsplit[0].strip()] = True
                elif val == "false":
                    mydict[lsplit[0].strip()] = False
            
        for key in mydict:
            if key not in KEYS:
                mydict.pop(key)
        
        for key in KEYS:
            if key not in mydict:
                mydict[key] = DEFAULTPREFS[key]
        return mydict

# This function displays the prompt screen when a user tries to quit
# User must choose Yes or No, this function returns True or False respectively
def prompt(win):
    rounded_rect(win, (255, 255, 255), (110, 160, 280, 130), 4, 4)

    win.blit(PREF.PROMPT[0], (130, 165))
    win.blit(PREF.PROMPT[1], (130, 190))

    win.blit(PREF.YES, (145, 240))
    win.blit(PREF.NO, (305, 240))
    pygame.draw.rect(win, (255, 255, 255), (140, 240, 60, 28), 2)
    pygame.draw.rect(win, (255, 255, 255), (300, 240, 45, 28), 2)

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
def showScreen(win, prefs):
    win.fill((0, 0, 0))

    rounded_rect(win, (255, 255, 255), (70, 10, 350, 70), 20, 4)
    rounded_rect(win, (255, 255, 255), (10, 85, 480, 360), 12, 4)

    win.blit(BACK, (460, 0))
    win.blit(PREF.HEAD, (110, 15))
    
    rounded_rect(win, (255, 255, 255), (10, 450, 310, 40), 10, 3)
    win.blit(PREF.TIP, (20, 450))
    win.blit(PREF.TIP2, (55, 467))

    win.blit(PREF.SOUNDS, (90, 90))
    win.blit(PREF.FLIP, (25, 150))
    win.blit(PREF.SLIDESHOW, (40, 210))
    win.blit(PREF.MOVE, (100, 270))
    win.blit(PREF.UNDO, (25, 330))
    win.blit(PREF.CLOCK, (25, 390))

    for i in range(6):
        win.blit(PREF.COLON, (225, 90 + (i * 60)))
        if prefs[KEYS[i]]:
            rounded_rect(
                win, (255, 255, 255), (249, 92 + (60 * i), 80, 40), 8, 2)
        else:
            rounded_rect(
                win, (255, 255, 255), (359, 92 + (60 * i), 90, 40), 8, 2)
        win.blit(PREF.TRUE, (250, 90 + (i * 60)))
        win.blit(PREF.FALSE, (360, 90 + (i * 60)))

    rounded_rect(win, (255, 255, 255), (350, 452, 85, 40), 10, 2)
    win.blit(PREF.BSAVE, (350, 450))

    x, y = pygame.mouse.get_pos()
    if 100 < x < 220 and 90 < y < 130:
        pygame.draw.rect(win, (0, 0, 0), (30, 90, 195, 40))
        win.blit(PREF.SOUNDS_H[0], (45, 90))
        win.blit(PREF.SOUNDS_H[1], (80, 110))
    if 25 < x < 220 and 150 < y < 190:
        pygame.draw.rect(win, (0, 0, 0), (15, 150, 210, 50))
        win.blit(PREF.FLIP_H[0], (50, 150))
        win.blit(PREF.FLIP_H[1], (70, 170))
    if 40 < x < 220 and 210 < y < 250:
        pygame.draw.rect(win, (0, 0, 0), (15, 210, 210, 40))
        win.blit(PREF.SLIDESHOW_H[0], (40, 210))
        win.blit(PREF.SLIDESHOW_H[1], (30, 230))
    if 100 < x < 220 and 270 < y < 310:
        pygame.draw.rect(win, (0, 0, 0), (15, 270, 210, 40))
        win.blit(PREF.MOVE_H[0], (35, 270))
        win.blit(PREF.MOVE_H[1], (25, 290))
    if 25 < x < 220 and 330 < y < 370:
        pygame.draw.rect(win, (0, 0, 0), (15, 330, 210, 40))
        win.blit(PREF.UNDO_H[0], (60, 330))
        win.blit(PREF.UNDO_H[1], (85, 350))
    if 25 < x < 220 and 390 < y < 430:
        pygame.draw.rect(win, (0, 0, 0), (15, 390, 210, 40))
        win.blit(PREF.CLOCK_H[0], (50, 390))
        win.blit(PREF.CLOCK_H[1], (40, 410))

# This is the main function, called by the main menu
def main(win):
    prefs = load()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, prefs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50 and prompt(win):
                    return 1

                if 350 < x < 425 and 450 < y < 490:
                    save(prefs)
                    return 1

                for i in range(6):
                    if 90 + i*60 < y < 130 + i*60:
                        if 250 < x < 330:
                            prefs[KEYS[i]] = True
                        if 360 < x < 430:
                            prefs[KEYS[i]] = False
        pygame.display.update()
