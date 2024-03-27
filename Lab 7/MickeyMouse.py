import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS + 8

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes, and seconds

font = pygame.font.SysFont('Verdana', 60)

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.fill(pygame.Color('black'))  # Fill the screen with black

    # get time now
    t = datetime.now()
    minute, second = t.minute, t.second

    # draw face
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)

    # draw clock
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 6)
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)

    # digital clock
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    surface.blit(time_render, (0, 0))

    # draw arc
    sec_angle = -math.radians(clock60[t.second]) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('black'),
                    (H_WIDTH - RADIUS_ARK, H_HEIGHT - RADIUS_ARK, 2 * RADIUS_ARK, 2 * RADIUS_ARK),
                    math.pi / 2, sec_angle, 8)

    pygame.display.flip()
    clock.tick(20)
