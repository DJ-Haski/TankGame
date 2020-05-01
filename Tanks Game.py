import pygame
import time
import random

pygame.init()

window_width=1280
window_height=768
UP=0
DOWN=180
RIGHT=-90
LEFT=90

gameWindow=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Tanks game project')
background=pygame.image.load('Map.png')

icon=pygame.image.load("Tank.png") #добавить иконку
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#player


#Shell
Shell=pygame.image.load("Shell.png")
ShellSpeed=500
ShellLifeTime=2000
ShellX=random.randint(0,800)
ShellY=random.randint(50,150)
ShellX_change=4
ShellY_chage=40


#enemy
EnemyImage=pygame.image.load("Tank2.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)

#fonts
s_font=pygame.font.SysFont("comincsansms",25)
m_font=pygame.font.SysFont("comincsansms",50)
l_font=pygame.font.SysFont("comincsansms",85)

gameWindow = pygame.display.set_mode((window_width, window_height))

def score(score):
    text = s_font.render("Score: " + str(score), True, (255, 255, 255))
def txt_obj(text, color, size="small"):
    if size == "small":
        textSurface = s_font.render(text, True, color)
    if size == "medium":
        textSurface = m_font.render(text, True, color)
    if size == "large":
        textSurface = l_font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def txt_btn(msg, color, buttonx, buttony, buttonw, buttonh, size="medium"):
    textSurf, textRect = txt_obj(msg, color, size)
    textRect.center = ((buttonx + (buttonw / 2)), buttony + (buttonh / 2))
    gameWindow.blit(textSurf, textRect)
def msg_screen(msg, color, y_disp=0, size="small"):
    textSurf, textRect = txt_obj(msg, color, size)
    textRect.center = (int(window_width / 2), (int(window_height / 2) + y_disp))
    gameWindow.blit(textSurf, textRect)
def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameWindow.fill((255, 255, 255))
        msg_screen("Game Controls:", (255, 125, 0), -200, size="large")
        msg_screen("To fire press SPACE or LMB", (0, 0, 0), -120, size="small")
        msg_screen("To move use Arrows.", (0, 0, 0), -90, size="small")
        msg_screen("To move tank's turret use mouse", (0, 0, 0), -60, size="small")
        msg_screen("To call pause press P", (0, 0, 0), -30, size="small")
        msg_screen("Press F to pay respect", (0, 0, 0), 0, size="small")
        # msg_screen("Press C to start, P to pause and Q to quit", (0, 0, 0), 90, size="medium")

        button("Solo game", 220, 500, 200, 50, (0, 200, 0), (0, 255, 0), action="play")
        button("Online", 540, 500, 200, 50, (200, 200, 0), (255, 255, 0), action="online")
        button("Quit", 860, 500, 200, 50, (200, 0, 0), (255, 0, 0), action="quit")
        button("Main Menu", 1050, 650, 200, 50, (200, 200, 0), (255, 255, 0), action="Main")

        pygame.display.update()
        clock.tick(15)
def enemy(x, y):
    gameWindow.blit(EnemyImage, (int(x), int(y)))
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameWindow, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
            if action == "online":
                pass
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "Main":
                game_intro()
    else:
        pygame.draw.rect(gameWindow, inactive_color, (x, y, width, height))
    txt_btn(text, (0, 0, 0), x, y, width, height)
def pause():
    paused = True
    msg_screen("Game on Pause", (0, 0, 0), -100, size="large")
    msg_screen("Press C to continue or Q to quit the game", (0, 0, 0), 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)
"""def fireShell(xy,tankx,tanky):
    fire=True
    startingShell=list(xy)
    print("Fire!",xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        print(startingShell[0],startingShell[1])
        gameWindow.blit(Shell,(startingShell[0],startingShell[1]))
        startingShell[0]-=5
        pygame.display.update()
        clock.tick(5)"""
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    quit()
        gameWindow.fill((255, 255, 255))
        msg_screen("Welcome to my first Tank game on python!", (255, 125, 0), -100, size="large")
        msg_screen("The objective is to destroy your opponent's tank", (0, 0, 0), -30, size="small")
        msg_screen("and not get destroyed by enemy", (0, 0, 0), 10, size="small")
        # msg_screen("Press C to start, P to pause and Q to quit", (0, 0, 0), 90, size="medium")

        button("Solo game", 220, 500, 200, 50, (0, 200, 0), (0, 255, 0), action="play")
        button("Online", 540, 500, 200, 50, (200, 200, 0), (255, 255, 0), action="online")
        button("Quit", 860, 500, 200, 50, (200, 0, 0), (255, 0, 0), action="quit")
        button("Controls", 1050, 650, 200, 50, (200, 200, 0), (255, 255, 0), action="controls")

        pygame.display.update()
        clock.tick(15)
def gameLoop():
    speed = 8
    gameExit = False
    gameOver = False
    FPS = 30
    Tank_surf = pygame.image.load('Tank.png')
    Tank_surf.set_colorkey((255, 255, 255))
    Tank_rect = Tank_surf.get_rect(center=(200, 150))

    pygame.display.update()
    rot = pygame.transform.rotate(Tank_surf, 0)
    rot_rect = rot.get_rect(center=(200, 150))
    while not gameExit:
        if gameOver == True:
            msg_screen("GAME OVER", (0, 255, 0), -50, size="large")
            msg_screen("Press C to play again or Q to quit", (0, 0, 0), 50, size="medium")
            pygame.display.update()
            while gameOver == True:
                for event in pygame.quit():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
        a = pygame.event.get()
        for i in a:
            if i.type == pygame.QUIT:  # выход
                pygame.quit()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:  # при нажатии вправо
                rot = pygame.transform.rotate(Tank_surf, -90)  # повернется на -90 градусов
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_UP:  # при нажатии вверх
                rot = pygame.transform.rotate(Tank_surf, 0)  # повернется на 0 градусов
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:  # при нажатии влево
                rot = pygame.transform.rotate(Tank_surf, 90)  # повернется на 90 градусов
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:  # при нажатии вниз
                rot = pygame.transform.rotate(Tank_surf, 180)  # повернется на 180 градусов
            if i.type == pygame.KEYDOWN and i.key == pygame.K_p:
                    pause()
        gameWindow.blit(rot, rot_rect)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            rot_rect.x += 5
        elif keys[pygame.K_UP]:
            rot_rect.y -= 5
        elif keys[pygame.K_LEFT]:
            rot_rect.x -= 5
        elif keys[pygame.K_DOWN]:
            rot_rect.y += 5
        if rot_rect.x <0:
            rot_rect.x+=window_width
        if rot_rect.y < 0:
            rot_rect.y += window_height
        if rot_rect.x > window_width:
            rot_rect.x -= window_width
        if rot_rect.y > window_height:
            rot_rect.y -= window_height

        pygame.time.delay(20)
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(background, (0, 0))
        enemy(enemyX, enemyY)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()