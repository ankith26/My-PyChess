"""
This file is a part of of My-PyChess application.

In this file, we handle all sound related stuff.
"""

import os.path
import time

try:
    import pygame.mixer
    pygame.mixer.init()
    
    SUCCESS = pygame.mixer.get_init() is not None

except (ImportError, RuntimeError):
    SUCCESS = False

if SUCCESS:
    click = pygame.mixer.Sound(os.path.join("res", "sounds", "click.ogg"))
    move = pygame.mixer.Sound(os.path.join("res", "sounds", "move.ogg"))
    start = pygame.mixer.Sound(os.path.join("res", "sounds", "start.ogg"))
    drag = pygame.mixer.Sound(os.path.join("res", "sounds", "drag.ogg"))

    background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))

class Music:
    def __init__(self):
        self.playing = False
        
    def play(self, load):
        if SUCCESS and load["sounds"]:
            background.play(-1)
            self.playing = True
    
    def stop(self):
        if SUCCESS:
            background.stop()
        self.playing = False
        
    def is_playing(self):
        return self.playing

def play_click(load):
    if SUCCESS and load["sounds"]:
        click.play()
        time.sleep(0.1)
    
def play_start(load):
    if SUCCESS and load["sounds"]:
        start.play()
    
def play_move(load):
    if SUCCESS and load["sounds"]:
        move.play()
        time.sleep(0.1)
    
def play_drag(load):
    if SUCCESS and load["sounds"]:
        drag.play()

if SUCCESS:
    pygame.mixer.quit()
