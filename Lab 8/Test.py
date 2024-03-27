#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0  # Объявляем переменную для подсчета монет
car_passed = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.original_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)  # Случайное местоположение по оси X
        self.rect.y = 0  # Монета появляется в самом верху экрана

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)  # Появление монеты в случайном месте по оси X
            self.rect.y = 0  # Монета появляется снова в самом верху экрана
# Другие машины
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.original_image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)  # Случайное местоположение по оси X
        self.rect.y = 0  # Машины появляется в самом верху экрана

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)  # Появление монеты в случайном месте по оси X
            self.rect.y = 0  # Машины появляется снова в самом верху экрана
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

# Спрайты      
P1 = Player()
E1 = Enemy()

# Группа спрайтов
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

coin = Coin()
coins.add(coin)
all_sprites.add(coin)
 
# Ивенты
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

CREATE_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_COIN, 2000)
 
# Цикл
while True:
    for event in pygame.event.get():
     if event.type == INC_SPEED:
        SPEED += 0.05     
        # Добавляем новые монеты во время игры
        if len(coins) < 3:  # Уменьшаем количество монет до трех
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)
     if event.type == QUIT:
        pygame.quit()
        sys.exit()
 
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Coins: " + str(SCORE), True, BLACK)  # Отображаем количество собранных монет
    DISPLAYSURF.blit(scores, (SCREEN_WIDTH - scores.get_width() - 10, 10))

    # Прорисовка
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Coin):
            entity.move()
            if pygame.sprite.collide_rect(P1, entity):  # Проверяем коллизию между игроком и монетой
                coins.remove(entity)
                all_sprites.remove(entity)
                SCORE += 1  # Увеличиваем счетчик монет при сборе
        elif isinstance(entity, Enemy):
            entity.move()
        elif isinstance(entity, Player):
            entity.move()

    # Столкновение машин
    if pygame.sprite.spritecollideany(P1, enemies):
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
