import pygame
import sys 
import random

pygame.init()

SW, SH = 800, 800
SCORE = 0
BLOCK_SIZE = 50
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
        self.level = 0
    
    def update(self):
        global apple, red_apple, blue_apple
        
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True
        
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            red_apple = RedApple()
            blue_apple = BlueApple()
        
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)
    def increase_speed(self):
        self.level += 1
        self.level_up_text = font_small.render(f"Level: {self.level}", True, "white")
        screen.blit(self.level_up_text, (10, SH - 50))
        pygame.display.flip()
        pygame.time.delay(1000)
        self.xdir += 1
        self.ydir += 1

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    
    def update(self):
        pygame.draw.rect(screen, "orange", self.rect)

class RedApple(Apple):
    def __init__(self):
        super().__init__()
    
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

class BlueApple(Apple):
    def __init__(self):
        super().__init__()
        self.timer = 50  # 5 seconds in milliseconds
        self.start_time = pygame.time.get_ticks()
        self.eaten = False

    def update(self):
        self.timer -= clock.get_rawtime()
        if self.timer <= 0:
            self.rect.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.rect.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            self.timer = 50  # Reset timer for next appearance
            self.eaten = False  # Reset the eaten flag
        if not self.eaten:  # Draw blue apple only if not eaten
            pygame.draw.rect(screen, "blue", self.rect)

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

score = font.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))

drawGrid()

snake = Snake()

apple = Apple()
red_apple = RedApple()
blue_apple = BlueApple()

if SCORE % 4 == 0 and SCORE != 0:  # Увеличение скорости каждые 4 очка
      self.increase_speed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()
    
    screen.fill('black')
    drawGrid()

    apple.update()
    red_apple.update()
    blue_apple.update()

    score = font.render(f"{len(snake.body) - 1}", True, "white")

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    screen.blit(score, score_rect)



    if snake.head.colliderect(apple.rect):
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()
        SCORE += 1
    elif snake.head.colliderect(red_apple.rect):
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        red_apple = RedApple()
        SCORE += 2
    elif snake.head.colliderect(blue_apple.rect) and not blue_apple.eaten:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        blue_apple.eaten = True
        SCORE += 1
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()
        if len(snake.body) % 5 == 0:  # уровень
            snake.increase_speed()
    pygame.display.update()
    clock.tick(5)
