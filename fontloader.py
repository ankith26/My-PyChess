import pygame.font
import pygame.display

pygame.display.init()
pygame.display.set_mode((1,1))
pygame.font.init()

head = pygame.font.Font("FreightSansBold.otf", 85)
large = pygame.font.Font("FreightSansBold.otf", 60)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)

#### FOR MAIN ####
HEADING = head.render("PyChess", True, (255,255,255)).convert_alpha()
VERSION = Vsmall.render("Version 2.1", True, (255,255,255)).convert_alpha()

SINGLE = medium.render("Single Player", True, (255,255,255)).convert_alpha()
SINGLE_H = medium.render("Single Player", True, (200,200,200)).convert_alpha()

MULTI = medium.render("MultiPlayer", True, (255,255,255)).convert_alpha()
MULTI_H = medium.render("MultiPlayer", True, (200,200,200)).convert_alpha()

ONLINE = medium.render("Online", True, (255,255,255)).convert_alpha()
ONLINE_H = medium.render("Online", True, (200,200,200)).convert_alpha()

LOAD = medium.render("Load Game", True, (255,255,255)).convert_alpha()
LOAD_H = medium.render("Load Game", True, (200,200,200)).convert_alpha()

ABOUT = medium.render("About", True, (255,255,255)).convert_alpha()
ABOUT_H = medium.render("About", True, (200,200,200)).convert_alpha()

DOCS = medium.render("Docs", True, (255,255,255)).convert_alpha()
DOCS_H = medium.render("Docs", True, (200,200,200)).convert_alpha()

PREF = medium.render("Preferences", True, (255,255,255)).convert_alpha()
PREF_H = medium.render("Preferences", True, (200,200,200)).convert_alpha()

#### FOR CHESS ####

CHECK = small.render("CHECK!", True, (0,0,0)).convert_alpha()
STALEMATE = small.render("STALEMATE!", True, (0,0,0)).convert_alpha()
CHECKMATE = small.render("CHECKMATE!", True, (0,0,0)).convert_alpha()
LOST = small.render("LOST", True, (0,0,0)).convert_alpha()
CHOOSE = small.render("CHOOSE:", True, (0,0,0)).convert_alpha()
SAVE = small.render("Save Game", True, (0,0,0)).convert_alpha()

#### FOR PROMPT ###
MESSAGE1 = small.render("Do you want to go to", True, (255,255,255)).convert_alpha()
MESSAGE2 = small.render("Home screen?", True, (255,255,255)).convert_alpha()
YES = small.render("YES", True, (255,255,255)).convert_alpha()
NO = small.render("NO", True, (255,255,255)).convert_alpha()

#### FOR PREF ####
PREFERENCE = large.render("Preferences", True, (255,255,255)).convert_alpha()

ANIMATION = medium.render("Animate :", True, (255,255,255)).convert_alpha()
SOUND = medium.render("Sounds :", True, (255,255,255)).convert_alpha()
SLIDESHOW = medium.render("Slideshow :", True, (255,255,255)).convert_alpha()
MOVE = medium.render("Show moves:", True, (255,255,255)).convert_alpha()
placeholder = medium.render("________ :", True, (255,255,255)).convert_alpha()

BSAVE = medium.render("Save", True, (255,255,255)).convert_alpha()
PAGE = [medium.render("Page 1", True, (255,255,255)).convert_alpha(),
        medium.render("Page 2", True, (255,255,255)).convert_alpha(),
        medium.render("Page 3", True, (255,255,255)).convert_alpha()]

L = head.render("<", True, (255,255,255)).convert_alpha()
L_H = head.render("<", True, (200,200,200)).convert_alpha()
R = head.render(">", True, (255,255,255)).convert_alpha()
R_H = head.render(">", True, (200,200,200)).convert_alpha()

TRUE = medium.render("True", True, (255,255,255)).convert_alpha()
FALSE = medium.render("False", True, (255,255,255)).convert_alpha()

pygame.display.quit()
pygame.font.quit()
