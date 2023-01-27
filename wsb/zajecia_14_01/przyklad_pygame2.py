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

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background, (0, 255, 255), (20, 20, 40, 40))
pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
pygame.draw.rect(background, (255, 100, 255), (220, 120, 50, 50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background, (0, 0))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()
