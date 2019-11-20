import pygame
import chess
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PyChess')

HEADING = pygame.image.load('images/heading.png')
SINGLEPLAYER = pygame.image.load('images/singleplayer.png')#220*80
MULTIPLAYER = pygame.image.load('images/multiplayer.png')#220*80
ONLINE = pygame.image.load('images/online.png')#220*80
#VERSION = pygame.image.load('images/version.png')
SOON1 = pygame.image.load('images/soon.png')#100*100
SOON2 = pygame.image.load('images/soon2.png')#100*100
ABOUT = pygame.image.load('images/about.png')#100*40
DOCS = pygame.image.load('images/docs.png')#100*40

def showMain():
    pygame.draw.rect(win,(0,0,0),(0,0,460,460))
    win.blit(HEADING,(100,20))
    win.blit(DOCS,(0,460))
    win.blit(ABOUT,(400,460))
    win.blit(SINGLEPLAYER,(110,140))
    win.blit(MULTIPLAYER,(110,220))
    win.blit(ONLINE,(110,300))

showMain()
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            #singleplayer
            if 110 < x < 330 and 140 < y < 220:
                win.blit(SOON2,(322,150))
            #multiplayer
            elif 110 < x < 330 and 220 < y < 300:
                chess.main(win)
                running = False
            #online
            if 110 < x < 330 and 300 < y < 380:
                win.blit(SOON2,(322,310))
            #docs
            if 0 < x < 100 and 460 < y < 500:
                win.blit(SOON1,(0,362))
            #about
            if 370 < x < 460 and 460 < y < 500:
                win.blit(SOON1,(400,362))
    pygame.display.update()
pygame.quit()
