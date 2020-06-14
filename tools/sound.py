"""
This file is a part of of My-PyChess application.

In this file, we handle all sound related stuff.
THIS SCRIPT IS A WORK-IN-PROGRESS.

Level of development = BETA
"""

import os
import time
import pygame.mixer

pygame.mixer.init()

click = pygame.mixer.Sound(os.path.join("res", "sounds", "click.ogg"))
move = pygame.mixer.Sound(os.path.join("res", "sounds", "move.ogg"))
start = pygame.mixer.Sound(os.path.join("res", "sounds", "start.ogg"))
drag = pygame.mixer.Sound(os.path.join("res", "sounds", "drag.ogg"))

background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))

playable = True

class Music:
    def __init__(self):
        self.playing = False
        
    def play(self, load):
        if load[0]:
            background.play(-1)
            self.playing = True
    
    def stop(self):
        background.stop()
        self.playing = False
        
    def is_playing(self):
        return self.playing

def play_click(load):
    if load[0]:
        click.play()
        time.sleep(0.1)
    
def play_start(load):
    if load[0]:
        start.play()
    
def play_move(load):
    if load[0]:
        move.play()
        time.sleep(0.1)
    
def play_drag(load):
    if load[0]:
        drag.play()
        
pygame.mixer.quit()