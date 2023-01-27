import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

x = 220 + 100
y = 120 + 70

krok_x = 2
krok_y = 3

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
    x += krok_x
    if x < 0:
        krok_x = -krok_x
        x = 0
    elif x + 50 > SZEROKOSC_OKNA:
        krok_x = -krok_x
        x = SZEROKOSC_OKNA - 50
    y += krok_y
    if y < 0:
        krok_y = -krok_y
        y = 0
    elif y + 50 > WYSOKOSC_OKNA:
        krok_y = -krok_y
        y = WYSOKOSC_OKNA - 50

pygame.quit()
