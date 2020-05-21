"""
This file is the main file of My-PyChess application.
Run this file to launch the program.

In this file, we handle the main menu which gets displayed at runtime.
"""

import pygame

import chess
import menus
from loader import MAIN

# Some initialisation
pygame.init()
clock = pygame.time.Clock()

# Initialise display, set the caption and icon
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My-PyChess")
pygame.display.set_icon(MAIN.ICON)

# Then, constants are defined which mark the positions of buttons on the menu
# Each constant is denoted by a tuple consisting four integers.
# Imagine a button as a rectangular area -
# We can represent a rectangle by the coordinates of its top-left point
# and its length and breadth
# So, each constant is of the form (x, y, length, breadth)
# x and y denote the coordinates of the top-left point
single = (260, 140, 220, 40)
multi = (280, 200, 200, 40)
online = (365, 260, 110, 40)
load = (280, 320, 200, 40)
prefer = (0, 450, 210, 40)
about = (0, 400, 110, 40)

# This is the function that displays the main screen.
# "prefs" value is passed, prefs is a list of all the user settings
def showMain(prefs):
    # cnt and image are two global variables, cnt is an integer that is
    # incremented in every frame, when cnt reaches 210, it is setback to zero.
    # img variable denotes the image that is displayed on the screen
    # it can have a value from 0 to 3 (both inclusive)
    global cnt, img

    # First, blit background image (based on the img variable)
    win.blit(MAIN.BG[img], (0, 0))

    # Then we check wether user has enabled background animate feature
    if prefs[2]:
        # Background animations is a feature that shows a slideshow of images
        # in the background, each image having a time duration of 7 seconds.
        # Slow fading of screen is also seen.
        # To achieve this, a frame counter variable "cnt" is incremented
        # every frame. The intended framerate of the game is 30 fps, so
        # after seven seconds, the frame counter reaches 210 after which,
        # it needs to be reset to zero.
        cnt += 1
        if cnt >= 150:
            # If the counter has reached a value of 150 (means 5 seconds have
            # elapsed), then start to slowly fade the image.
            # This is achieved by blitting a surface onto the screen
            # whose transparancy keeps reducing as each frame goes
            s = pygame.Surface((500, 500))
            s.set_alpha((cnt - 150) * 4)
            s.fill((0, 0, 0))
            win.blit(s, (0, 0))

        if cnt == 210:
            # Reset the counter
            cnt = 0
            # Set image value to zero if it is at 3, or else increment it
            # This variable controls which image is seen on screen.
            img = 0 if img == 3 else img + 1
    else:
        # User has disabled screen animations, reset the variables
        cnt = -150
        img = 0

    # Now blit all the texts onto the screen one by one
    win.blit(MAIN.HEADING, (80, 20))
    pygame.draw.line(win, (255, 255, 255), (80, 100), (130, 100), 4)
    pygame.draw.line(win, (255, 255, 255), (165, 100), (340, 100), 4)
    win.blit(MAIN.VERSION, (345, 95))

    win.blit(MAIN.SINGLE, single[:2])
    win.blit(MAIN.MULTI, multi[:2])
    win.blit(MAIN.ONLINE, online[:2])
    win.blit(MAIN.LOAD, load[:2])
    win.blit(MAIN.PREF, prefer[:2])
    win.blit(MAIN.ABOUT, about[:2])


# Initialize a few more variables
cnt = 0
img = 0
running = True

# Load the settings of the player
LOAD = menus.pref.load()
while running:
    # Start the game loop at 30fps, show the screen every time at first
    clock.tick(30)
    showMain(LOAD)

    # We need to get the position of the mouse so that we can blit an image
    # on the text over which the mouse hovers
    x, y = pygame.mouse.get_pos()
    # singleplayer
    if (single[0] < x < single[0] + single[2] and
        single[1] < y < single[1] + single[3]):
        win.blit(MAIN.SINGLE_H, single[:2])
    # multiplayer
    elif (multi[0] < x < multi[0] + multi[2] and
          multi[1] < y < multi[1] + multi[3]):
        win.blit(MAIN.MULTI_H, multi[:2])
    # online
    elif (online[0] < x < online[0] + online[2] and
          online[1] < y < online[1] + online[3]):
        win.blit(MAIN.ONLINE_H, online[:2])
    # Load Game
    elif load[0] < x < load[0] + load[2] and load[1] < y < load[1] + load[3]:
        win.blit(MAIN.LOAD_H, load[:2])
    # Pref
    elif (prefer[0] < x < prefer[0] + prefer[2] and
          prefer[1] < y < prefer[1] + prefer[3]):
        win.blit(MAIN.PREF_H, prefer[:2])
    # about
    elif (about[0] < x < about[0] + about[2] and
          about[1] < y < about[1] + about[3]):
        win.blit(MAIN.ABOUT_H, about[:2])

    # Begin pygame event loop to catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User has clicked somewhere, determine which button and
            # Call a function to handle the game into a different window.
            # All functions defined in the chess module open up the chess
            # board and a game begins based on the type of game
            x, y = event.pos
            # singleplayer
            if (single[0] < x < single[0] + single[2] and
                single[1] < y < single[1] + single[3]):
                data = menus.splayermenu(win)
                if data is not None:
                    if data[0]:
                        chess.mysingleplayer(win, data[1], LOAD)
                    else:
                        chess.singleplayer(win, data[1], data[2], LOAD)
            # multiplayer
            elif (multi[0] < x < multi[0] + multi[2] and
                  multi[1] < y < multi[1] + multi[3]):
                chess.multiplayer(win, LOAD)
            # online
            elif (online[0] < x < online[0] + online[2] and
                  online[1] < y < online[1] + online[3]):
                chess.online(win, menus.onlinemenu(win), LOAD)
            # Load Game
            elif (load[0] < x < load[0] + load[2] and
                  load[1] < y < load[1] + load[3]):
                game = menus.loadgamemenu(win)
                if game is not None:
                    if game[0] == "multi":
                        chess.multiplayer(win, LOAD, game[1])
                    elif game[0] == "single":
                        chess.singleplayer(win, int(game[1]), int(game[2]),
                                           LOAD, game[3])
                    elif game[0] == "mysingle":
                        chess.mysingleplayer(win, int(game[1]), LOAD, game[2])
            # prefer
            elif (prefer[0] < x < prefer[0] + prefer[2] and
                  prefer[1] < y < prefer[1] + prefer[3]):
                menus.prefmenu(win)
                LOAD = menus.pref.load()
            # about
            elif (about[0] < x < about[0] + about[2] and
                about[1] < y < about[1] + about[3]):
                menus.aboutmenu(win)

    # Update the screen every frame
    pygame.display.flip()

# Quit pygame after the loop is done
pygame.quit()