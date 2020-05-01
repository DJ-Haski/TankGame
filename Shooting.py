import pygame
import random
pygame.init()
file = 'SabatonPrimoVic.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1) # -1 для зацикливания
window_width = 1280
window_height = 768
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
pygame.init()
pygame.mixer.init()
gameWindow = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()
pygame.display.set_caption('Tanks game project')
background=pygame.image.load('Map.png')
icon=pygame.image.load("Tank.png")
pygame.display.set_icon(icon)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.image.load("Tank.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width / 2
        self.rect.bottom = window_height - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -8
        if key[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > window_width:
            self.rect.right = window_width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.image.load("Tank2.png")
        self.image = pygame.image.load("Tank2.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(window_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > window_height + 10 or self.rect.left < -25 or self.rect.right > window_width + 20:
            self.rect.x = random.randrange(window_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

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
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(4):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False


    gameWindow.fill(BLACK)

    all_sprites.draw(gameWindow)
    background = pygame.image.load('Map.png')

    pygame.display.flip()

pygame.quit()