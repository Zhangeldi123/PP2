import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    eraser_mode = False
    
    running = True  # условие
    
    while running:  # цикл ивентов
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False  # Завершаем цикл при нажатии на крестик окна
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    running = False  # Завершаем цикл при нажатии Ctrl + W
                if event.key == pygame.K_F4 and alt_held:
                    running = False  # Завершаем цикл при нажатии Alt + F4
                if event.key == pygame.K_ESCAPE:
                    running = False  # Завершаем цикл при нажатии Esc
                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                if not eraser_mode:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                else:
                    position = event.pos
                    points = [p for p in points if (p[0] - position[0]) ** 2 + (p[1] - position[1]) ** 2 > radius ** 2]
        
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()  # завершения цикла

def drawLineBetween(screen, index, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)  
    elif color_mode == 'red':
        color = (255, 0, 0)  
    elif color_mode == 'green':
        color = (0, 255, 0)  
    elif color_mode == 'erase':
        color = (0, 0, 0)    
    else:
        color = (255, 255, 255)  
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
