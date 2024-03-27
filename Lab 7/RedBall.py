import pygame
import sys

pygame.init()


width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")


white = (255, 255, 255)
red = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = width // 2, height // 2
ball_speed = 20


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_y - ball_speed >= 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_speed <= height - ball_radius * 2:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_speed >= 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_speed <= width - ball_radius * 2:
        ball_x += ball_speed

    win.fill(white)

    pygame.draw.circle(win, red, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)

    
    pygame.display.flip()

    
    clock.tick(30)
