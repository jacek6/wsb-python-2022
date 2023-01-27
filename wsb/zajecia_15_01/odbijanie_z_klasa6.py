# refactor
import random

import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)


class FizykaOdbijajacegoSieObiektu:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    def __init__(self, x, y):
        super(PoruszajacySieKwadracik, self).__init__(x, y)

    @property
    def kolor(self):
        return (0, 255, 0)

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def paint(self):
        pygame.draw.circle(background, self.kolor, (self.x + 25, self.y + 25), 25)

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         y -= 40
        #     elif event.key == pygame.K_s:
        #         y += 40
    paint()

    for k in obiekty_na_ekranie:
        k.update()

pygame.quit()
