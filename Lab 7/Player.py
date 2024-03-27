import pygame
import sys

pygame.init()

# Set up the screen (not used in this example, but Pygame requires it)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

# Set up colors
white = (255, 255, 255)


font = pygame.font.Font(None, 36)


playlist = ["NICO Touches the Walls_Diver.mp3",
            "07.  Niwaka Ame Nimo Makezu.mp3",
            "Sukima SwitchLINE.mp3"]
current_track = 0
print("Loading:", playlist[current_track])
pygame.mixer.music.load(playlist[current_track])

is_playing = False


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:  # Play/Pause
        if is_playing:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        is_playing = not is_playing

    elif keys[pygame.K_n]:  # Next track
        current_track = (current_track + 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

    elif keys[pygame.K_p]:  # Previous track
        current_track = (current_track - 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

    elif keys[pygame.K_s]:  # Stop
        pygame.mixer.music.stop()
        is_playing = False

    
    screen.fill(white)

    
    text = font.render("Space: Play/Pause | N: Next | P: Previous | S: Stop", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    
    pygame.display.flip()

    
    clock.tick(30)
