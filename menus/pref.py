'''
This file is a part of My-PyChess application.
In this file, we manage the preferences menu which is called when user clicks
preferences button on main menu.

We also define functions to save and load user preferences.

Level of development = STABLE
'''

import os.path
import pygame
from loader import PREF
from tools.utils import rounded_rect

# This function returns a boolean from a string.
def makeBool(x):
    return x.strip() == "True" or x.strip() == "true"

# This function saves user preferences in a text file.
def save(*params):
    text = ""
    text += "sounds = " + str(params[0]) + '\n'
    text += "flip = " + str(params[1]) + '\n'
    text += "slideshow = " + str(params[2]) + '\n'
    text += "show_legal_moves = " + str(params[3]) + '\n'
    text += "allow_undo = " + str(params[4]) + '\n'
    
    with open(os.path.join("res", "preferences.txt"), "w") as f:
        f.write(text)

# This function loads user preferences from a text file
def load():
    with open(os.path.join("res", "preferences.txt"), "r") as f:
        return [makeBool(i.split("=")[1]) for i in f.read().splitlines()]
    
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
    rounded_rect(win, (255, 255, 255), (10, 90, 480, 350), 12, 4)
    win.blit(PREF.HEAD, (110, 15))
    win.blit(PREF.TIP, (20, 400))
    win.blit(PREF.TIP2, (55, 417))
    
    win.blit(PREF.SOUNDS, (90, 100))
    win.blit(PREF.FLIP, (25, 160))
    win.blit(PREF.SLIDESHOW, (40, 220))
    win.blit(PREF.MOVE, (100, 280))
    win.blit(PREF.UNDO, (25, 340))
    for i in range(5):
        win.blit(PREF.COLON, (225, 100 + (i * 60)))
        if prefs[i]:
            rounded_rect(win, (255, 255, 255), (249, 102 + (60 * i), 80, 40), 8, 2)
        else:
            rounded_rect(win, (255, 255, 255), (359, 102 + (60 * i), 90, 40), 8, 2)
        win.blit(PREF.TRUE, (250, 100 + (i * 60)))
        win.blit(PREF.FALSE, (360, 100 + (i * 60)))
    
    rounded_rect(win, (255, 255, 255), (200, 452, 85, 40), 10, 3)
    win.blit(PREF.BSAVE, (200, 450))
        
    x, y = pygame.mouse.get_pos()
    if 100 < x < 220 and 100 < y < 140:
        pygame.draw.rect(win, (0, 0, 0), (15, 100, 210, 40))
        win.blit(PREF.SOUNDS_H[0], (45, 100))
        win.blit(PREF.SOUNDS_H[1], (80, 120))
    if 25 < x < 220 and 160 < y < 200:
        pygame.draw.rect(win, (0, 0, 0), (15, 160, 210, 50))
        win.blit(PREF.FLIP_H[0], (50, 160))
        win.blit(PREF.FLIP_H[1], (70, 180))
    if 40 < x < 220 and 220 < y < 260:
        pygame.draw.rect(win, (0, 0, 0), (15, 220, 210, 40))
        win.blit(PREF.SLIDESHOW_H[0], (40, 220))
        win.blit(PREF.SLIDESHOW_H[1], (30, 240))
    if 100 < x < 220 and 280 < y < 320:
        pygame.draw.rect(win, (0, 0, 0), (15, 280, 210, 40))
        win.blit(PREF.MOVE_H[0], (35, 280))
        win.blit(PREF.MOVE_H[1], (25, 300))
    if 25 < x < 220 and 340 < y < 380:
        pygame.draw.rect(win, (0, 0, 0), (15, 340, 210, 40))
        win.blit(PREF.UNDO_H[0], (60, 340))
        win.blit(PREF.UNDO_H[1], (85, 360))

# This is the main function, called by the main menu
def main(win):
    prefs = load()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, prefs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 200 < event.pos[0] < 285 and 450 < event.pos[1] < 490:
                    save(*prefs)
                    return
                for cnt in range(5):
                    if 100 + cnt*60 < event.pos[1] < 140 + cnt*60:
                        if 250 < event.pos[0] < 330:
                            prefs[cnt] = True
                        if 360 < event.pos[0] < 430:
                            prefs[cnt] = False                  
        pygame.display.update()
