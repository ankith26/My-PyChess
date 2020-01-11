import pygame
from fontloader import PREFERENCE, ANIMATION, SOUND, SLIDESHOW, placeholder,\
     MOVE, BSAVE, TRUE, FALSE, L, L_H, R, R_H, PAGE

def save(a, b, c, d):
    file = open("preferences.txt", "w")
    text = "animations = " + str(a) + '\n'
    text += "sounds = " + str(b) + '\n'
    text += "slideshow = " + str(c) + '\n'
    text += "show-legal-moves = " + str(d) + '\n'
    file.write(text)
    file.close()
    
def load():
    file = open("preferences.txt", "r")
    lines = file.readlines()
    temp = []
    for line in lines:
        temp.append(makeBool(line.strip('\n').split("=")[1].strip()))
    file.close()
    return temp

def makeBool(x):
    return x == "True"

def screen(win, pg=1):
    pygame.draw.rect(win, (0,0,0), (0,0,500,500))
    win.blit(PREFERENCE, (85,20))
    
    win.blit(BSAVE, (200,400))
    win.blit(PAGE[pg-1], (200, 450))
    win.blit(L, (100, 420))
    win.blit(R, (350, 420))
    pygame.draw.rect(win, (255,255,255), (200, 400, 85, 40), 3)
    pygame.draw.rect(win, (255,255,255), (100, 440, 42, 50), 3)
    pygame.draw.rect(win, (255,255,255), (350, 440, 42, 50), 3)
    
    if pg == 1:
        win.blit(L_H, (100, 420))
        pygame.draw.rect(win, (180,180,180), (100, 440, 42, 50), 3)
        win.blit(ANIMATION, (70,100))
        win.blit(SOUND, (88,160))
        win.blit(SLIDESHOW, (35,220))
        win.blit(MOVE, (10,280))
        win.blit(placeholder, (30,340))
        for i in range(5):
            win.blit(TRUE, (250, 100 + (i * 60)))
            win.blit(FALSE, (360, 100 + (i * 60)))
    elif pg == 2:
        pass
    elif pg == 3:
        win.blit(R_H, (350, 420))
        pygame.draw.rect(win, (180,180,180), (350, 440, 42, 50), 3)
        pass
    
def main(win):
    clock = pygame.time.Clock()
    var = load()
    animate, sound, slideshow, move = var[0], var[1], var[2], var[3]
    pg = 1
    while True:
        clock.tick(10)
        screen(win, pg)
        if pg == 1:
            if animate:
                pygame.draw.rect(win, (255,255,255), (250, 100, 80, 40), 2)
            else:
                pygame.draw.rect(win, (255,255,255), (360, 100, 90, 40), 2)
                
            if sound:
                pygame.draw.rect(win, (255,255,255), (250, 160, 80, 40), 2)
            else:
                pygame.draw.rect(win, (255,255,255), (360, 160, 90, 40), 2)
                
            if slideshow:
                pygame.draw.rect(win, (255,255,255), (250, 220, 80, 40), 2)
            else:
                pygame.draw.rect(win, (255,255,255), (360, 220, 90, 40), 2)
            
            if move:
                pygame.draw.rect(win, (255,255,255), (250, 280, 80, 40), 2)
            else:
                pygame.draw.rect(win, (255,255,255), (360, 280, 90, 40), 2)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 < x < 285 and 400 < y < 440:
                    save(animate, sound, slideshow, move)
                    return
                elif 100 < x < 142 and 440 < y < 490:
                    if pg > 1:
                        pg -= 1
                elif 350 < x < 392 and 440 < y < 490:
                    if pg < 3:
                        pg += 1
                if pg == 1:
                    if 250 < x < 330 and 100 < y < 140:
                        animate = True
                    if 250 < x < 330 and 160 < y < 200:
                        sound = True
                    if 250 < x < 330 and 220 < y < 260:
                        slideshow = True
                    if 250 < x < 330 and 280 < y < 320:
                        move = True
                    if 250 < x < 330 and 340 < y < 380:
                        _ = True
                    
                    if 360 < x < 430 and 100 < y < 140:
                        animate = False
                    if 360 < x < 430 and 160 < y < 200:
                        sound = False
                    if 360 < x < 430 and 220 < y < 260:
                        slideshow = False
                    if 360 < x < 430 and 280 < y < 320:
                        move = False
                    if 360 < x < 430 and 340 < y < 380:
                        _ = False
        pygame.display.update()
