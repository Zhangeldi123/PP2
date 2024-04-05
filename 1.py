import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing
pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
# Other Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
N = 0  # число монет
level = 0  # уровень
yummy = True
# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.jpg")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        global N
        global yummy
        self.rect.move_ip(0, 2)
        # если машинка сталкивается с монетой , то счет +=1
        if P1.rect.colliderect(C1.rect):  # готовая функция, возращает 0 или 1
            yummy = True
            N += 1  # число заработанных монет
            SCORE += random.randint(1, 5)  # different weight
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        elif self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class ScoreCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  # Изображение монеты
        self.image = pygame.transform.scale(self.image, (30, 30))  # Масштабируем изображение
        self.rect = self.image.get_rect()  # Получаем прямоугольник для коллизий
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Начальное положение монеты

    def move(self):
        self.rect.move_ip(0, 5)  # Двигаем монету вниз

        # Если монета выходит за пределы экрана, перемещаем ее вверх с новыми координатами
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        # Если машинка сталкивается с монетой, увеличиваем счет на 1 и перемещаем монету
        if P1.rect.colliderect(self.rect):
            global SCORE
            global N
            SCORE += 1
            N += 1
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):

        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:

            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.left > 0:
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)
        


# Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
S1 = ScoreCoin()

# Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(S1)

# A new User Event

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound('background.wav').play(-1)

while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if yummy is True and N % 4 == 0:  # если игрок зарабатывает 4 монеты, скорость вражеской машинки повышается
                level += 1
                SPEED += 2
                yummy = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0, 0))
    # счетчик
    scores = font_small.render("SCORE: " + str(SCORE), True, RED)
    coins = font_small.render("COINS: " + str(N), True, GREEN)
    levels = font_small.render("LEVEL: " + str(level), True, YELLOW)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins, (290, 10))
    DISPLAYSURF.blit(levels, (160, 10))

    # Moves and Re - draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
