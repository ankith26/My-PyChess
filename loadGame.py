import os
import pygame
import pygame.font

pygame.font.init()

sans = pygame.font.Font("FreightSansBold.otf", 36)

TEXT = sans.render("File not found", True, (240, 240, 240))

def textbox(win, text):
    pygame.draw.rect(win, (0,0,200), (210, 160, 80, 40), 2)
    pygame.draw.rect(win, (240,240,240), (210, 160, 80, 40))
    win.blit(sans.render(text, True, (0,0,0)), (210,160))
    
def makeBool(arg):
    for i in arg:
        yield i == "True"

def showMain(win):
    clock = pygame.time.Clock()
    BACKGROUND = pygame.image.load(os.path.join("images", "background.jpg"))
    win.blit(BACKGROUND, (0, 0))
    win.blit(sans.render("Enter GameId of the Game", True, (255,255,255)),
             (40,60))
    win.blit(sans.render("you want to load", True, (255,255,255)), (100, 100))
    
    text = ""
    while True:
        pygame.display.update()
        clock.tick(10)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_RETURN:
                    if text != "":
                        if loadGame(int(text)) == None:
                            win.blit(TEXT, (100, 400))
                        else:
                            return loadGame(int(text))
        textbox(win, text)
    pygame.font.quit()
    
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
    