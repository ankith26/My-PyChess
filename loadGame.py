import os
import pygame
import pygame.font

pygame.font.init()

sans = pygame.font.Font("FreightSansBold.otf", 36)
Vsmall = pygame.font.Font("FreightSansBold.otf", 16)

NOTFOUND = sans.render("File not found", True, (240, 240, 240))
SUCCESS = sans.render("Successfully deleted", True, (240, 240, 240))

def textbox1(win, text):
    pygame.draw.rect(win, (0,0,200), (210, 160, 80, 40), 2)
    pygame.draw.rect(win, (240,240,240), (210, 160, 80, 40))
    win.blit(sans.render(text, True, (0,0,0)), (210,160))

def textbox2(win, text):
    pygame.draw.rect(win, (0,0,200), (210, 360, 80, 40), 2)
    pygame.draw.rect(win, (240,240,240), (210, 360, 80, 40))
    win.blit(sans.render(text, True, (0,0,0)), (210,360))
    
def makeBool(arg):
    for i in arg:
        yield i == "True"
        
def getText(event, text = ""):
    if event.key == pygame.K_BACKSPACE:
        if len(text) == 1:
            text = ""
        elif len(text) == 2:
            text = text[0]
    if len(text) < 2:
        if event.key == pygame.K_0:
            text += "0"
        if event.key == pygame.K_1:
            text += "1"
        if event.key == pygame.K_2:
            text += "2"
        if event.key == pygame.K_3:
            text += "3"
        if event.key == pygame.K_4:
            text += "4"
        if event.key == pygame.K_5:
            text += "5"
        if event.key == pygame.K_6:
            text += "6"
        if event.key == pygame.K_7:
            text += "7"
        if event.key == pygame.K_8:
            text += "8"
        if event.key == pygame.K_9:
            text += "9"
    return text
        
def showMain(win):
    clock = pygame.time.Clock()
    pygame.draw.rect(win, (0,0,0), (0,0,500,500))
    strArray = ["DEPRACATION WARNING: The current format of saving games will",
                "be changed in the next major update, therefore the game will",
                "not to work with games saved via the current format."]
    for cnt, string in enumerate(strArray):
        win.blit(Vsmall.render(string, True, (255,255,255)), (8,16*cnt))
        
    win.blit(sans.render("Enter GameId of the Game", True, (255,255,255)),
             (40,60))
    win.blit(sans.render("you want to load", True, (255,255,255)), (100, 100))
    
    win.blit(sans.render("Enter GameId of the Game", True, (255,255,255)),
             (40, 260))
    win.blit(sans.render("you want to delete", True, (255,255,255)), (90, 300))
    
    pygame.draw.rect(win, (255,255,255), (35,50,420,190), 3)
    pygame.draw.rect(win, (255,255,255), (35,255,420,200), 3)
    
    text1 = text2 = ""
    sel = 1
    while True:
        pygame.display.update()
        clock.tick(10)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 210 < x < 290:
                    if 160 < y < 200:
                        sel = 1
                    elif 360 < y < 400:
                        sel = 2
                    else:
                        sel = 0
                else:
                    sel = 0
            elif event.type == pygame.KEYDOWN:
                if sel == 1:
                    text1 = getText(event, text1)
                    if event.key == pygame.K_RETURN and text1 != '':
                        data = loadGame(int(text1))
                        if data == None:
                            win.blit(NOTFOUND, (140, 200))
                        else:
                            return data
                elif sel == 2:
                    text2 = getText(event, text2)
                    if event.key == pygame.K_RETURN and text2 != '':
                        if not delGame(int(text2)):
                            pygame.draw.rect(win, (0,0,0), (100, 400, 330, 40))
                            win.blit(NOTFOUND, (140, 400))
                        else:
                            pygame.draw.rect(win, (0,0,0), (100, 400, 330, 40))
                            win.blit(SUCCESS, (100, 400))
                            
                    
        textbox1(win, text1)
        textbox2(win, text2)
        pygame.draw.rect(win, (110, 150, 255), (210, sel*200 - 40, 80, 40), 3)
    pygame.font.quit()
    
def delGame(gameId):
    name = os.path.join("savedGames", "game" + str(gameId) + ".txt")
    if os.path.exists(name):
        os.remove(name)
        return True
    else:
        return False
    
def loadGame(gameId):
    name = os.path.join("savedGames", "game" + str(gameId) + ".txt")
    try:
        file = open(name, "r")
    except:
        return None
    lines = file.readlines()
    player = lines[0][:-1]
    move = lines[1][:-1] == "True"
    wBoard = []
    bBoard = []
    
    for i in lines[2].split():
        var = i.split(',')
        if len(var) == 1:
            wBoard.append(None)
        elif len(var) == 4:
            wBoard.append([int(var[0]),int(var[1]), var[2]])   
                
    for i in lines[3].split():
        var = i.split(',')
        if len(var) == 1:
            bBoard.append(None)
        elif len(var) == 4:
            bBoard.append([int(var[0]),int(var[1]), var[2]])  
    routine = [i for i in makeBool(lines[4].split())]
    return [player, move, wBoard, bBoard, routine]
    