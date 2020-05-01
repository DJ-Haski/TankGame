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

icon=pygame.image.load("Tank.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
#Shell
Shell=pygame.image.load("Shell.png")
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

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
def shoot(Tx,Ty):
    bullet = Bullet(Tx.rect.centerx, Ty.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.image.load("Shell.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()
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

        button("1 by 1 game", 220, 500, 200, 50, (0, 200, 0), (0, 255, 0), action="play")
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
    Tank2_surf = pygame.image.load('Tank2.png')
    Tank_surf.set_colorkey((255, 255, 255))
    Tank2_surf.set_colorkey((255, 255, 255))
    Tank_rect = Tank_surf.get_rect(center=(1100, 700))
    Tank2_rect = Tank2_surf.get_rect(center=(200, 150))

    pygame.display.update()
    rot = pygame.transform.rotate(Tank_surf, 0)
    rot_rect = rot.get_rect(center=(1100, 700))
    rot2 = pygame.transform.rotate(Tank2_surf, 0)
    rot2_rect = rot2.get_rect(center=(200, 150))
    def shoot(x):
        bullet = Bullet(rot.rect.centerx, rot_rect.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
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
            if i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:
                rot = pygame.transform.rotate(Tank_surf, -90)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
                rot = pygame.transform.rotate(Tank_surf, 0)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:
                rot = pygame.transform.rotate(Tank_surf, 90)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:
                rot = pygame.transform.rotate(Tank_surf, 180)
            if i.type == pygame.KEYDOWN and i.key == pygame.K_d:
                rot2 = pygame.transform.rotate(Tank2_surf, 90)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_w:
                rot2 = pygame.transform.rotate(Tank2_surf, 180)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_a:
                rot2 = pygame.transform.rotate(Tank2_surf, -90)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_s:
                rot2 = pygame.transform.rotate(Tank2_surf, 0)
            if i.type == pygame.KEYDOWN and i.key == pygame.K_p:
                    pause()
        gameWindow.blit(rot, rot_rect)
        gameWindow.blit(rot2, rot2_rect)
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
        elif keys[pygame.K_BACKSPACE]:
            shoot()
        if rot_rect.x <0:
            rot_rect.x+=window_width
        if rot_rect.y < 0:
            rot_rect.y += window_height
        if rot_rect.x > window_width:
            rot_rect.x -= window_width
        if rot_rect.y > window_height:
            rot_rect.y -= window_height
        elif keys[pygame.K_SPACE]:
            shoot()

        if keys[pygame.K_d]:
            rot2_rect.x += 5
        elif keys[pygame.K_w]:
            rot2_rect.y -= 5
        elif keys[pygame.K_a]:
            rot2_rect.x -= 5
        elif keys[pygame.K_s]:
            rot2_rect.y += 5
        if rot2_rect.x <0:
            rot2_rect.x+=window_width
        if rot2_rect.y < 0:
            rot2_rect.y += window_height
        if rot2_rect.x > window_width:
            rot2_rect.x -= window_width
        if rot2_rect.y > window_height:
            rot2_rect.y -= window_height

        pygame.time.delay(20)
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()