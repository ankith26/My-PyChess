"""
This file is a part of My-PyChess application.
This file loads all the images and texts that are used.
All the resources needed are mostly loaded in this file.
Most of the scripts in this application import specific classes from this
module. Each class is a collection of resources for a particular script.
All font-related stuff is done in this file, the functions to put a number
on the screen and display date and time are also defined here
"""

import os
import pygame

# Initialize pygame.font module and load the font file
pygame.font.init()
FONT = os.path.join("res", "Asimov.ttf")

# Load different sizes of the font
head = pygame.font.Font(FONT, 80)
large = pygame.font.Font(FONT, 50)
medium = pygame.font.Font(FONT, 38)
small = pygame.font.Font(FONT, 28)
vsmall = pygame.font.Font(FONT, 17)

# Define RGB color constants for use
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

# Define a few constants that contain loaded texts of numbers and chararters
NUM = [vsmall.render(str(i), True, WHITE) for i in range(10)]
LNUM = [small.render(str(i), True, WHITE) for i in range(10)]
SLASH = vsmall.render("/", True, WHITE)
COLON = vsmall.render(":", True, WHITE)

# This is a function that displays a number in a position on the screen
# Very small sized text used
def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 8), pos[1]))

# This is a function that displays a number in a position on the screen
# Small sized text used
def putLargeNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(LNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))

# This is a function that displays the date and time in a position
# on the screen.
def putDT(win, DT, pos):
    var = DT.split()
    date = var[0].split("/")
    time = var[1].split(":")
    for cnt, num in enumerate(date):
        putNum(win, num, (pos[0] + 24 * cnt - 5, pos[1]))

    win.blit(SLASH, (pos[0] + 13, pos[1]))
    win.blit(SLASH, (pos[0] + 35, pos[1]))

    for cnt, num in enumerate(time):
        putNum(win, num, (pos[0] + 24 * cnt, pos[1] + 21))

    win.blit(COLON, (pos[0] + 20, pos[1] + 21))
    win.blit(COLON, (pos[0] + 43, pos[1] + 21))


# This splits a string at regular intervals of "index" characters
def splitstr(string, index=57):
    data = []
    while len(string) >= index:
        data.append(string[:index])
        string = string[index:]
    data.append(string)
    return data

# Defined important globals for loading background image sprites.
BGSPRITE = pygame.image.load(os.path.join("res", "img", "bgsprites.jpg"))
PSPRITE = pygame.image.load(os.path.join("res", "img", "piecesprite.png"))

class CHESS:   
    PIECES = ({}, {})  
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface((i*50, side*50, 50, 50))

    CHECK = small.render("CHECK!", True, BLACK)
    STALEMATE = small.render("STALEMATE!", True, BLACK)
    CHECKMATE = small.render("CHECKMATE!", True, BLACK)
    LOST = small.render("LOST", True, BLACK)
    CHOOSE = small.render("CHOOSE:", True, BLACK)
    SAVE = small.render("Save Game", True, BLACK)
    UNDO = small.render("Undo", True, BLACK)

    MESSAGE = [
        small.render("Do you want to quit", True, WHITE),
        small.render("this game?", True, WHITE),
    ]

    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)
    MSG = vsmall.render("Game will be saved with ID", True, WHITE)
    SAVE_ERR = vsmall.render("ERROR: SaveGame Limit Exeeded", True, WHITE)
    
    TURN = [small.render("Others turn", True, BLACK),
            small.render("Your turn", True, BLACK)]

class LOADGAME:
    HEAD = large.render("Load Games", True, WHITE)
    LIST = medium.render("List of Games", True, WHITE)
    EMPTY = small.render("There are no saved games yet.....", True, WHITE)
    GAME = small.render("Game", True, WHITE)
    TYPHEAD = vsmall.render("Game Type:", True, WHITE)
    TYP = {
        "single": vsmall.render("SinglePlayer", True, WHITE),
        "mysingle": vsmall.render("SinglePlayer", True, WHITE),
        "multi": vsmall.render("MultiPlayer", True, WHITE),
    }
    DATE = vsmall.render("Date:", True, WHITE)
    TIME = vsmall.render("Time:", True, WHITE)

    DEL = pygame.image.load(os.path.join("res", "img", "delete.jpg"))
    LOAD = small.render("LOAD", True, WHITE)

    MESSAGE = [
        small.render("Are you sure that you", True, WHITE),
        small.render("want to delete game?", True, WHITE),
    ]
    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)

    LEFT = medium.render("<", True, WHITE)
    RIGHT = medium.render(">", True, WHITE)
    PAGE = [medium.render("Page " + str(i), True, WHITE) for i in range(1, 5)]

class MAIN:
    HEADING = head.render("PyChess", True, WHITE)
    VERSION = vsmall.render("Version 3.0", True, WHITE)
    ICON = pygame.image.load(os.path.join("res", "img", "icon.gif")) 
    BG = [BGSPRITE.subsurface((i*500, 0, 500, 500)) for i in range(4)]

    SINGLE = medium.render("SinglePlayer", True, WHITE)
    MULTI = medium.render("MultiPlayer", True, WHITE)
    ONLINE = medium.render("Online", True, WHITE)
    LOAD = medium.render("Load Game", True, WHITE)
    ABOUT = medium.render("About", True, WHITE)
    PREF = medium.render("Preferences", True, WHITE)
    
    SINGLE_H = medium.render("SinglePlayer", True, GREY)
    MULTI_H = medium.render("MultiPlayer", True, GREY)  
    ONLINE_H = medium.render("Online", True, GREY)
    LOAD_H = medium.render("Load Game", True, GREY)
    ABOUT_H = medium.render("About", True, GREY)
    PREF_H = medium.render("Preferences", True, GREY)

class PREF:
    HEAD = large.render("Preferences", True, WHITE)

    PLACEHOLDER = medium.render("Placeholder :", True, WHITE)
    FLIP = medium.render("Flip screen :", True, WHITE)
    SLIDESHOW = medium.render("Slideshow :", True, WHITE)
    MOVE = medium.render("Moves :", True, WHITE)
    SHUNDO = medium.render("Allow undo :", True, WHITE)

    TRUE = medium.render("True", True, WHITE)
    FALSE = medium.render("False", True, WHITE)

    PLACEHOLDER_H = [
        vsmall.render("This is a placeholder", True, WHITE),
        vsmall.render("for future update", True, WHITE),
    ]
    FLIP_H = [
        vsmall.render("This flips the screen", True, WHITE),
        vsmall.render("after each move", True, WHITE),
    ]
    SLIDESHOW_H = [
        vsmall.render("This shows a slide of", True, WHITE),
        vsmall.render("backgrounds on screen", True, WHITE),
    ]
    MOVE_H = [
        vsmall.render("This shows all the legal", True, WHITE),
        vsmall.render("moves of a selected piece", True, WHITE),
    ]
    SHUNDO_H = [
        vsmall.render("This allowes undo if", True, WHITE),
        vsmall.render("set to be true", True, WHITE),
    ]

    BSAVE = medium.render("Save", True, WHITE)
    TIP = vsmall.render(
        "TIP: Hover the mouse over the feature name to know", True, WHITE)
    TIP2 = vsmall.render("more about it.", True, WHITE)

class ONLINE:
    TRYCONN = small.render("Trying to connect....", True, WHITE)
    ERRCONN = small.render("Could not connect to server", True, WHITE)
    ERRVER = small.render("Server refused connection due to version error",
                          True, WHITE)
    ERRBUSY = small.render("Server Busy", True, WHITE)

    EMPTY = small.render("No one's online, you are alone.", True, WHITE)

    LOBBY = large.render("Online Lobby", True, WHITE)
    LIST = medium.render("List of Players", True, WHITE)
    PLAYER = small.render("Player", True, WHITE)
    DOT = small.render(".", True, WHITE)
    ACTIVE = small.render("ACTIVE", True, GREEN)
    BUSY = small.render("BUSY", True, RED)
    REQ = small.render("Send Request", True, WHITE)
    YOUARE = medium.render("You Are", True, WHITE)

    REFRESH = pygame.image.load(os.path.join("res", "img", "refresh.png"))

    MSG1 = (
        vsmall.render("Please wait for the other player to", True, WHITE),
        vsmall.render("accept your request. Game will begin", True, WHITE),
        vsmall.render("shortly. You will play as white", True, WHITE),
    )
    MSG2 = (
        vsmall.render("Player", True, WHITE),
        vsmall.render("wants to play with you.", True, WHITE),
        vsmall.render("Accept to play. You will play as black", True, WHITE),
    )
    MSG3 = (
        vsmall.render("Your Opponent Quit. You are disconnected", True, WHITE),
        vsmall.render("from server. Go back to main menu?", True, WHITE),
    )
    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)
    OK = small.render("OK", True, WHITE)

class ONLINEMENU:
    HEAD = large.render("Online", True, WHITE)
    with open(os.path.join("res", "texts", "online.txt")) as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
        
    with open(os.path.join("res", "texts", "onlinehowto.txt")) as f:
        TEXT2 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
        
    CLICK = vsmall.render("Click Here", True, WHITE)
    BACK = vsmall.render("Go Back", True, WHITE)
    CONNECT = small.render("Connect", True, WHITE)
       
class SINGLE:
    HEAD = large.render("Singleplayer", True, WHITE)
    _PARA1 = [
        "Play chess against a chess player algorithm implemented in",
        "python. This is called MiniMax algorithm and is used with",
        "alpha-beta optimisation technique. Currently, it is setup",
        "to play like a average (weak) player of chess.",
    ]
    PARA1 = [vsmall.render(i, True, WHITE) for i in _PARA1]
    SELECT = pygame.image.load(os.path.join("res", "img", "select.png"))
    CHOOSE = small.render("Choose:", True, WHITE)
    START = small.render("Start Game", True, WHITE)
    OR = medium.render("OR", True, WHITE)
    _PARA2 = [
        "Play chess against the StockFish Chess Engine, the best",
        "chess engine in the world. This can play chess with a variety",
        "of difficulty settings, the hardest levels can easily defeat",
        "chess grandmasters.",
    ]
    PARA2 = [vsmall.render(i, True, WHITE) for i in _PARA2]
    LEVEL = small.render("Level:", True, WHITE)
    
    BACK = vsmall.render("Go Back", True, WHITE)
    _CONFIG = [
        "It looks like you have not configured",
        "stockfish. To play, you have to do",
        "that."
    ]
    CONFIG = [vsmall.render(i, True, WHITE) for i in _CONFIG]
    OK = vsmall.render("Ok", True, WHITE)
    NOTNOW = vsmall.render("Not Now", True, WHITE)

class STOCKFISH:
    HEAD = large.render("Stockfish Engine", True, WHITE)
    CONFIG = small.render("Configure Stockfish", True, WHITE)
    with open(os.path.join("res", "texts", "stockfish.txt"), "r") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
        
    with open(os.path.join("res", "texts", "configd.txt"), "r") as f:
        CONFIGURED = [vsmall.render(i, True, GREEN)
                       for i in f.read().splitlines()]
    
    with open(os.path.join("res", "texts", "nonconfigd.txt"), "r") as f:
        NONCONFIGURED = [vsmall.render(i, True, RED)
                       for i in f.read().splitlines()]


class INSTALL:
    CLICK = vsmall.render("Click Here", True, WHITE)
    BACK = vsmall.render("Go Back", True, WHITE)
    INSTALL = small.render("Test Install", True, WHITE)
    TEST = vsmall.render(
        "After all steps are complete, press button below", True, WHITE)
    
    WIN_HEAD = small.render("Installation Guide for Windows", True, WHITE)
    LIN_HEAD = small.render("Installation Guide for Linux -", True, WHITE)
    MAC_HEAD = small.render("Installation Guide for Mac", True, WHITE)
    OTH_HEAD = small.render("Installation Guide for Other OS", True, WHITE)

    with open(os.path.join("res", "texts", "win.txt"), "r") as f:
        WIN_TEXT = [vsmall.render(i, True, WHITE)
                    for i in f.read().splitlines()]
    
    with open(os.path.join("res", "texts", "linux.txt"), "r") as f:
        LIN_TEXT = [vsmall.render(i, True, WHITE)
                    for i in f.read().splitlines()]
    
    with open(os.path.join("res", "texts", "linux2.txt"), "r") as f:
        LIN_TEXT2 = [vsmall.render(i, True, WHITE)
                     for i in f.read().splitlines()]
        
    with open(os.path.join("res", "texts", "mac.txt"), "r") as f:
        MAC_TEXT = [vsmall.render(i, True, WHITE)
                    for i in f.read().splitlines()]
        
    with open(os.path.join("res", "texts", "other.txt"), "r") as f:
        OTH_TEXT = [vsmall.render(i, True, WHITE)
                    for i in f.read().splitlines()]
    
    for line in splitstr(os.path.abspath("res/stockfish/build/stockfish.exe")):
        WIN_TEXT.append(vsmall.render(line, True, WHITE))
        
    for line in splitstr(os.path.abspath("res/stockfish/build/stockfish")):
        LIN_TEXT2.append(vsmall.render(line, True, WHITE))
        OTH_TEXT.append(vsmall.render(line, True, WHITE))
        
    LOADING = head.render("Loading", True, WHITE)
    _SUCCESS = ["Setup successful, now you can go", "back and play chess."]
    _NOSUCCESS = ["Setup unsuccessful, try to re-",
                  "configure. Follow instuctions",
                  "carefully and try again."]
    
    SUCCESS = [vsmall.render(i, True, GREEN) for i in _SUCCESS]
    NOSUCCESS = [vsmall.render(i, True, RED) for i in _NOSUCCESS]

class ABOUT:
    HEAD = large.render("About My-PyChess", True, WHITE)
    SOON = medium.render("Coming Soon!", True, WHITE)
    
    STOCKFIG = small.render("Want to configure stockfish?", True, WHITE)
    CLICK = small.render("Click Here", True, WHITE)

pygame.font.quit()