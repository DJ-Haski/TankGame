import pygame
import time
import random

pygame.init()

window_width=1280
window_height=720
gameWindow=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Tanks game project')

"""icon=pygame.image.load("") #добавить иконку
pygame.display.set_icon(icon)"""

clock = pygame.time.Clock()
s_font=pygame.font.SysFont("comicsans",25)
m_font=pygame.font.SysFont("comicsans",50)
l_font=pygame.font.SysFont("comicsans",85)

def score(score):
        text=s_font.render("Score: "+str(score),True,(255,255,255))
def txt_obj(text,color,size="small"):
        if size=="small":
                 textSurface=s_font.render(text,True,color)
        if size=="medium":
                 textSurface=m_font.render(text,True,color)
        if size=="large":
                 textSurface=l_font.render(text,True,color)
        return textSurface, textSurface.get_rect()
def txt_btn(msg,color,buttonx,buttony,buttonw,buttonh, size="medium"):
    textSurf,textRect=txt_obj(msg,color,size)
    textRect.center=((buttonx+(buttonw/2)),buttony+(buttonh/2))
    gameWindow.blit(textSurf, textRect)
def msg_screen(msg,color,y_disp=0,size="small"):
    textSurf,textRect= txt_obj(msg,color,size)
    textRect.center=(int(window_width/2),(int(window_height/2)+y_disp))
    gameWindow.blit(textSurf,textRect)
def button(text,x,y,width,height,inactive_color,active_color,action=None):
    cur= pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > cur[0] > x and y+height>cur[1]>y:
        pygame.draw.rect(gameWindow,active_color,(x,y,width,height))
        if click[0]==1:
            pass
    else:
        pygame.draw.rect(gameWindow, inactive_color, (x, y, width, height))
    txt_btn(text,(0,0,0),x,y,width,height)
def pause():
    paused=True
    msg_screen("Game on Pause",(0,0,0),-100,size="large")
    msg_screen("Press C to continue or Q to quit the game",(0,0,0),25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
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

        button("Solo game",220,500,200,50,(0,200,0),(0,255,0),)
        button("Online", 540, 500, 200, 50, (200,200,0),(255,255,0))
        button("Quit", 860, 500, 200, 50,(200,0,0),(255,0,0))

        pygame.display.update()
        clock.tick(15)
game_intro()
def gameLoop():
    gameExit=False
    gameOver=False
    FPS = 15

    while not gameExit:
        if gameOver==True:
            msg_screen("GAME OVER",(0,255,0),-50,size="large")
            msg_screen("Press C to play again or Q to quit",(0,0,0),50,size="medium")
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()
        gameWindow.fill((255,255,255))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
