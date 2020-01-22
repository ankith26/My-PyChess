import pygame
from fontloader import *
def save(*params):
    file = open("preferences.txt", "w")
    text = "animations = " + str(params[0]) + '\n'
    text += "sounds = " + str(params[1]) + '\n'
    text += "slideshow = " + str(params[2]) + '\n'
    text += "show-legal-moves = " + str(params[3]) + '\n'
    text += "allow-undo = " + str(params[4]) + '\n'
    text += "border-color = " + makeCol(params[5]) + '\n'
    file.write(text)
    file.close()
    
def load():
    file = open("preferences.txt", "r")
    lines = file.readlines()
    temp = []
    for cnt, line in enumerate(lines):
        if cnt in range(5):
            temp.append(makeBool(line.strip('\n').split("=")[1].strip()))
        elif cnt == 5:
            var = line.split("=")[1].strip('\n')
            temp.append(list(map(int, var.split(","))))
        elif cnt == 6:
            temp.append(line.strip('\n').split("=")[1].strip())
    file.close()
    return temp

def makeBool(x):
    return x == "True" or x == "true"

def makeCol(x):
    data = []
    for i in x:
        try:
            data.append(min(int(i), 255))
        except:
            data.append(0)
    return str(data)[1:-1]

def showScreen(win, prefs, pg, sel):
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
        win.blit(MOVE, (100,280))
        win.blit(SHUNDO, (20,340))
        for i in range(5):
            win.blit(TRUE, (250, 100 + (i * 60)))
            win.blit(FALSE, (360, 100 + (i * 60)))
        
        if prefs[0]:
            pygame.draw.rect(win, (255,255,255), (250, 100, 80, 40), 2)
        else:
            pygame.draw.rect(win, (255,255,255), (360, 100, 90, 40), 2)         
        if prefs[1]:
            pygame.draw.rect(win, (255,255,255), (250, 160, 80, 40), 2)
        else:
            pygame.draw.rect(win, (255,255,255), (360, 160, 90, 40), 2)          
        if prefs[2]:
            pygame.draw.rect(win, (255,255,255), (250, 220, 80, 40), 2)
        else:
            pygame.draw.rect(win, (255,255,255), (360, 220, 90, 40), 2)     
        if prefs[3]:
            pygame.draw.rect(win, (255,255,255), (250, 280, 80, 40), 2)
        else:
            pygame.draw.rect(win, (255,255,255), (360, 280, 90, 40), 2)         
        if prefs[4]:
            pygame.draw.rect(win, (255,255,255), (250, 340, 80, 40), 2)
        else:
            pygame.draw.rect(win, (255,255,255), (360, 340, 90, 40), 2)
    elif pg == 2:
        win.blit(BORCOL, (10, 100))
        pygame.draw.rect(win, (255,255,255), (230, 105, 70, 30))
        pygame.draw.rect(win, (255,255,255), (320, 105, 70, 30))
        pygame.draw.rect(win, (255,255,255), (410, 105, 70, 30))
        
        win.blit(SCSIZE, (30, 160))
        win.blit(SMALL, (80, 200))
        win.blit(MED, (200, 200))
        win.blit(LARGE, (360, 200))
        
        putNum(win, prefs[5][0], (230, 100))
        putNum(win, prefs[5][1], (320, 100))
        putNum(win, prefs[5][2], (410, 100))
        
        pygame.draw.rect(win, (110, 150, 255), (230+(sel*90), 105, 70, 30), 3)
    elif pg == 3:
        win.blit(R_H, (350, 420))
        pygame.draw.rect(win, (180,180,180), (350, 440, 42, 50), 3)
      
    x, y = pygame.mouse.get_pos()
    if pg == 1:
        if 70 < x < 230 and 100 < y < 140:
            pygame.draw.rect(win, (0, 0, 0), (35, 100, 190, 40))
            win.blit(ANIMATION_H[0], (30,100))
            win.blit(ANIMATION_H[1], (20,120))
        if 88 < x < 230 and 160 < y < 200:
            pygame.draw.rect(win, (0, 0, 0), (35, 160, 190, 40))
            win.blit(SOUND_H[0], (70,160))
            win.blit(SOUND_H[1], (70,180))
        if 35 < x < 230 and 220 < y < 260:
            pygame.draw.rect(win, (0, 0, 0), (35, 220, 190, 40))
            win.blit(SLIDESHOW_H[0], (30,220))
            win.blit(SLIDESHOW_H[1], (10,240))
        if 100 < x < 230 and 280 < y < 320:
            pygame.draw.rect(win, (0, 0, 0), (35, 280, 190, 40))
            win.blit(MOVE_H[0], (30,280))
            win.blit(MOVE_H[1], (20,300))
        if 20 < x < 230 and 340 < y < 380:
            pygame.draw.rect(win, (0, 0, 0), (20, 340, 205, 40))
            win.blit(SHUNDO_H[0], (50,340))
            win.blit(SHUNDO_H[1], (70,360))
    if pg == 2:
        if 10 < x < 200 and 100 < y < 140:
            pygame.draw.rect(win, (0, 0, 0), (10, 100, 200, 40))
            win.blit(BORCOL_H[0], (30,100))
            win.blit(BORCOL_H[1], (10,120))
        if 10 < x < 200 and 160 < y < 200:
            pygame.draw.rect(win, (0, 0, 0), (30, 160, 180, 40))
            win.blit(SCSIZE_H[0], (30,160))
            win.blit(SCSIZE_H[1], (25,180))
    if pg == 3:
        pass

LOAD = load()
        
def main(win):
    clock = pygame.time.Clock()
    prefs = load()
    prefs[5] = list(map(str, prefs[5]))
    pg = 1
    sel = 0
    while True:
        clock.tick(24)
        showScreen(win, prefs, pg, sel)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(prefs[5][sel]) == 1:
                        prefs[5][sel] = ""
                    elif len(prefs[5][sel]) == 2:
                        prefs[5][sel] = prefs[5][sel][0]
                    elif len(prefs[5][sel]) == 3:
                        prefs[5][sel] = prefs[5][sel][:2]
                elif len(prefs[5][sel]) < 3:
                    if event.key == pygame.K_0:
                        prefs[5][sel] += "0"
                    if event.key == pygame.K_1:
                        prefs[5][sel] += "1"
                    if event.key == pygame.K_2:
                        prefs[5][sel] += "2"
                    if event.key == pygame.K_3:
                        prefs[5][sel] += "3"
                    if event.key == pygame.K_4:
                        prefs[5][sel] += "4"
                    if event.key == pygame.K_5:
                        prefs[5][sel] += "5"
                    if event.key == pygame.K_6:
                        prefs[5][sel] += "6"
                    if event.key == pygame.K_7:
                        prefs[5][sel] += "7"
                    if event.key == pygame.K_8:
                        prefs[5][sel] += "8"
                    if event.key == pygame.K_9:
                        prefs[5][sel] += "9"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 < x < 285 and 400 < y < 440:
                    save(*prefs)
                    return
                elif 100 < x < 142 and 440 < y < 490:
                    if pg > 1:
                        pg -= 1
                elif 350 < x < 392 and 440 < y < 490:
                    if pg < 3:
                        pg += 1
                if pg == 1:
                    if 250 < x < 330:
                        if 100 < y < 140:
                            prefs[0] = True
                        if 160 < y < 200:
                            prefs[1] = True
                        if 220 < y < 260:
                            prefs[2] = True
                        if 280 < y < 320:
                            prefs[3] = True
                        if 340 < y < 380:
                            prefs[4] = True
                    if 360 < x < 430:
                        if 100 < y < 140:
                            prefs[0] = False
                        if 160 < y < 200:
                            prefs[1] = False
                        if 220 < y < 260:
                            prefs[2] = False
                        if 280 < y < 320:
                            prefs[3] = False
                        if 340 < y < 380:
                            prefs[4] = False
                if pg == 2:
                    if 100 < y < 130:
                        if 230 < x < 300:
                            sel = 0
                        if 320 < x < 390:
                            sel = 1
                        if 410 < x < 480:
                            sel = 2
        pygame.display.update()
    pygame.quit()
