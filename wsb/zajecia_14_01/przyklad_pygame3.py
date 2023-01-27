import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

#### Create a canvas on which to display everything ####
window = (400, 400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

x = 220 + 100
y = 120 + 70

def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
    pygame.draw.rect(background, (0, 255, 0), (x, y, 50, 50))

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 40
            elif event.key == pygame.K_s:
                y += 40
    paint()
#### Update the the display and wait ####

pygame.quit()
