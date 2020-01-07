import pygame.font
pygame.font.init()

large = pygame.font.Font("FreightSansBold.otf", 85)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)

#### FOR MAIN ####
HEADING = large.render("PyChess", True, (255,255,255))
VERSION = Vsmall.render("Version 2.0", True, (255,255,255))

SINGLE = medium.render("Single Player", True, (255,255,255))
SINGLE_H = medium.render("Single Player", True, (200,200,200))

MULTI = medium.render("MultiPlayer", True, (255,255,255))
MULTI_H = medium.render("MultiPlayer", True, (200,200,200))

ONLINE = medium.render("Online", True, (255,255,255))
ONLINE_H = medium.render("Online", True, (200,200,200))

LOAD = medium.render("Load Game", True, (255,255,255))
LOAD_H = medium.render("Load Game", True, (200,200,200))

ABOUT = medium.render("About", True, (255,255,255))
ABOUT_H = medium.render("About", True, (200,200,200))

DOCS = medium.render("Docs", True, (255,255,255))
DOCS_H = medium.render("Docs", True, (200,200,200))

#### FOR CHESS ####

CHECK = small.render("CHECK!", True, (0,0,0))
STALEMATE = small.render("STALEMATE!", True, (0,0,0))
CHECKMATE = small.render("CHECKMATE!", True, (0,0,0))
LOST = small.render("LOST", True, (0,0,0))
CHOOSE = small.render("CHOOSE:", True, (0,0,0))
SAVE = small.render("Save Game", True, (0,0,0))

MESSAGE1 = small.render("Do you want to go to", True, (255,255,255))
MESSAGE2 = small.render("Home screen?", True, (255,255,255))
YES = small.render("YES", True, (255,255,255))
NO = small.render("NO", True, (255,255,255))
pygame.font.quit()
