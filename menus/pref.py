'''
This file is a part of My-PyChess application.
In this file, we manage the preferences menu which is called when user clicks
preferences button on main menu.

We also define functions to save and load user preferences.
'''

import os
import pygame
from loader import PREF
from tools.utils import rounded_rect

def makeBool(x):
    return x.strip() == "True" or x.strip() == "true"

def save(*params):
    text = ""
    text += "(placeholder) = " + str(params[0]) + '\n'
    text += "flip = " + str(params[1]) + '\n'
    text += "slideshow = " + str(params[2]) + '\n'
    text += "show-legal-moves = " + str(params[3]) + '\n'
    text += "allow-undo = " + str(params[4]) + '\n'
    
    with open(os.path.join("res", "preferences.txt"), "w") as f:
        f.write(text)

def load():
    with open(os.path.join("res", "preferences.txt"), "r") as f:
        return [makeBool(i.split("=")[1]) for i in f.read().splitlines()]

def showScreen(win, prefs):
    win.fill((0, 0, 0))
    
    rounded_rect(win, (255, 255, 255), (70, 10, 350, 70), 20, 4)
    rounded_rect(win, (255, 255, 255), (10, 90, 480, 350), 12, 4)
    win.blit(PREF.HEAD, (110, 15))
    win.blit(PREF.TIP, (20, 400))
    win.blit(PREF.TIP2, (55, 417))
    
    win.blit(PREF.PLACEHOLDER, (15, 100))
    win.blit(PREF.FLIP, (25, 160))
    win.blit(PREF.SLIDESHOW, (40, 220))
    win.blit(PREF.MOVE, (100, 280))
    win.blit(PREF.SHUNDO, (25, 340))
    for i in range(5):
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
        win.blit(PREF.PLACEHOLDER_H[0], (30, 100))
        win.blit(PREF.PLACEHOLDER_H[1], (50, 120))
    if 25 < x < 220 and 160 < y < 200:
        pygame.draw.rect(win, (0, 0, 0), (15, 160, 210, 50))
        win.blit(PREF.FLIP_H[0], (50, 160))
        win.blit(PREF.FLIP_H[1], (60, 180))
    if 40 < x < 220 and 220 < y < 260:
        pygame.draw.rect(win, (0, 0, 0), (15, 220, 210, 40))
        win.blit(PREF.SLIDESHOW_H[0], (30, 220))
        win.blit(PREF.SLIDESHOW_H[1], (30, 240))
    if 100 < x < 220 and 280 < y < 320:
        pygame.draw.rect(win, (0, 0, 0), (15, 280, 210, 40))
        win.blit(PREF.MOVE_H[0], (35, 280))
        win.blit(PREF.MOVE_H[1], (25, 300))
    if 25 < x < 220 and 340 < y < 380:
        pygame.draw.rect(win, (0, 0, 0), (15, 340, 210, 40))
        win.blit(PREF.SHUNDO_H[0], (60, 340))
        win.blit(PREF.SHUNDO_H[1], (80, 360))

def main(win):
    prefs = load()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, prefs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
