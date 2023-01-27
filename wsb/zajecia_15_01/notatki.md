




### Program odbijanie_z_klasa1.py

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3

    def paint(self):
        pygame.draw.rect(background, (0, 255, 0), (self.x, self.y, 50, 50))

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + 50 > SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = SZEROKOSC_OKNA - 50
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + 50 > WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = WYSOKOSC_OKNA - 50


kwadracik1 = PoruszajacySieKwadracik(120, 220)
kwadracik2 = PoruszajacySieKwadracik(220, 220)
kwadracik3 = PoruszajacySieKwadracik(120, 120)


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    kwadracik1.paint()
    kwadracik2.paint()
    kwadracik3.paint()

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

    kwadracik1.update()
    kwadracik2.update()
    kwadracik3.update()

pygame.quit()

```





### Program odbijanie_z_klasa2.py

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3

    def paint(self):
        pygame.draw.rect(background, (0, 255, 0), (self.x, self.y, 50, 50))

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + 50 > SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = SZEROKOSC_OKNA - 50
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + 50 > WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = WYSOKOSC_OKNA - 50


kwadraciki = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220), PoruszajacySieKwadracik(120, 120)]


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in kwadraciki:
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

    for k in kwadraciki:
        k.update()

pygame.quit()

```





### Program odbijanie_z_klasa3.py

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3

    def paint(self):
        pygame.draw.rect(background, (0, 255, 0), (self.x, self.y, 50, 50))

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + 50 > SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = SZEROKOSC_OKNA - 50
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + 50 > WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = WYSOKOSC_OKNA - 50


class Kolo(PoruszajacySieKwadracik):

    def paint(self):
        # pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, 50, 50))
        pygame.draw.circle(background, (0, 255, 0), (self.x + 25, self.y + 25), 25)

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]


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

```





### Program odbijanie_z_klasa4.py

Kod programu:
```python
# refactoring wcześniejszego programu
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


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50
        self.kolor = (0, 255, 0)

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

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
obiekty_na_ekranie[0].kolor = losowy_kolor()


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

```





### Program odbijanie_z_klasa5.py

Kod programu:
```python
# zmienianie koloru
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


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50
        # self.kolor = (0, 255, 0)

    @property
    def kolor(self):
        return losowy_kolor()

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

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
obiekty_na_ekranie[0].kolor = losowy_kolor()


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

```





### Program odbijanie_z_klasa6.py

Kod programu:
```python
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

```





### Program odbijanie_z_klasa7.py

Kod programu:
```python
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

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


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

```





### Program odbijanie_z_klasa8.py

Kod programu:
```python
# poprawa aby zdrzak koła był taki sam jak rysowane koło
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
        if self._czy_ustawiac_wymiary:
            self.szerokosc = 50
            self.wysokosc = 50

    @property
    def _czy_ustawiac_wymiary(self):
        return True

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

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def _czy_ustawiac_wymiary(self):
        return False

    @property
    def wysokosc(self):
        return 2 * self.promien

    @property
    def szerokosc(self):
        return 2 * self.promien

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


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

```





### Program odbijanie_z_klasa9.py

Kod programu:
```python
# rysowanie lini od myszki
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
        if self._czy_ustawiac_wymiary:
            self.szerokosc = 50
            self.wysokosc = 50

    @property
    def _czy_ustawiac_wymiary(self):
        return True

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

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def _czy_ustawiac_wymiary(self):
        return False

    @property
    def wysokosc(self):
        return 2 * self.promien

    @property
    def szerokosc(self):
        return 2 * self.promien

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = pygame.mouse.get_pos()
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))

def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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

```





### Program odbijanie_z_klasa10.py

Kod programu:
```python
# rysowanie lini od myszki do środka każdego obiektu
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
        if self._czy_ustawiac_wymiary:
            self.szerokosc = 50
            self.wysokosc = 50

    @property
    def _czy_ustawiac_wymiary(self):
        return True

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

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

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def _czy_ustawiac_wymiary(self):
        return False

    @property
    def wysokosc(self):
        return 2 * self.promien

    @property
    def szerokosc(self):
        return 2 * self.promien

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = pygame.mouse.get_pos()
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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

```





### Program sortowanie_w_konsoli

Kod programu:
```python
lista = [8, 2, 5, 1, 78, 2, -90, -3, -1]

print(sorted(lista))
# print(sorted(lista, reverse=True))


def mysl_o_innej_wartosci(wartosc_z_listy):
    return wartosc_z_listy * wartosc_z_listy

print(sorted(lista, key=mysl_o_innej_wartosci))

print(sorted(lista, key=lambda wartosc_z_listy: wartosc_z_listy * wartosc_z_listy))
print(sorted(lista, key=lambda x: x * x))

# funkcja jako wartość zmiennej
mysl_o_innej_wartosci2 = lambda wartosc_z_listy: wartosc_z_listy * wartosc_z_listy

print(mysl_o_innej_wartosci(-2))
print(mysl_o_innej_wartosci2(-2))

funckja_mnozaca_w_jendej_lini = lambda a, b, c: a * b * c
print(funckja_mnozaca_w_jendej_lini(2, 3, 4))

def funckja_mnozaca_normna(a, b, c):
    return a * b * c
```



Output:
```
[-90, -3, -1, 1, 2, 2, 5, 8, 78]
[1, -1, 2, 2, -3, 5, 8, 78, -90]
[1, -1, 2, 2, -3, 5, 8, 78, -90]
[1, -1, 2, 2, -3, 5, 8, 78, -90]
4
4
24

```





### Program sortowanie_obiektow1.py

Kod programu:
```python
# rysowanie lini od myszki do środka każdego obiektu i sortowanie obiektów przy tym
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
        if self._czy_ustawiac_wymiary:
            self.szerokosc = 50
            self.wysokosc = 50

    @property
    def _czy_ustawiac_wymiary(self):
        return True

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def _czy_ustawiac_wymiary(self):
        return False

    @property
    def wysokosc(self):
        return 2 * self.promien

    @property
    def szerokosc(self):
        return 2 * self.promien

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = pygame.mouse.get_pos()
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci

pygame.quit()

```





### Program sortowanie_obiektow2.py

Kod programu:
```python
# rysowanie lini od obiektu najbliższego myszce: do środka każdego obiektu i sortowanie obiektów przy tym
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
        if self._czy_ustawiac_wymiary:
            self.szerokosc = 50
            self.wysokosc = 50

    @property
    def _czy_ustawiac_wymiary(self):
        return True

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def _czy_ustawiac_wymiary(self):
        return False

    @property
    def wysokosc(self):
        return 2 * self.promien

    @property
    def szerokosc(self):
        return 2 * self.promien

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia


def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]
punkt_od_ktorego_rysujemy_linie = (0, 0)

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = punkt_od_ktorego_rysujemy_linie
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    obiekt_najblizszy_myszcze = posortowane_obiekty[0]
    srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
    punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
    # *args, **kwargs - rozpakowanie w Python

    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(*srodek_obiektu_najbliszego_myszce))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci

pygame.quit()

```





### Program sortowanie_obiektow3.py

Kod programu:
```python
# rysowanie lini od obiektu najbliższego myszce: do środka każdego obiektu i sortowanie obiektów przy tym
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

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik(120, 220), PoruszajacySieKwadracik(220, 220),
                      PoruszajacySieKwadracik(120, 120),
                      Kolo(80, 100)]
punkt_od_ktorego_rysujemy_linie = (0, 0)

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = punkt_od_ktorego_rysujemy_linie
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    obiekt_najblizszy_myszcze = posortowane_obiekty[0]
    srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
    punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
    # *args, **kwargs - rozpakowanie w Python

    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(*srodek_obiektu_najbliszego_myszce))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci
    guzik1, guzik2, guzik3 =  pygame.mouse.get_pressed()
    if guzik1:
        obiekt_najblizszy_myszcze.szerokosc += 4

pygame.quit()

```





### Program ukladanie_obiektow1.py

Kod programu:
```python
# rysowanie lini od obiektu najbliższego myszce: do środka każdego obiektu i sortowanie obiektów przy tym
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

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def nowy_kwadrat():
    return PoruszajacySieKwadracik(random.randint(0, SZEROKOSC_OKNA), random.randint(0, WYSOKOSC_OKNA))

obiekty_na_ekranie = [nowy_kwadrat(), nowy_kwadrat(), nowy_kwadrat(),
                      Kolo(80, 100)]
punkt_od_ktorego_rysujemy_linie = (0, 0)

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = punkt_od_ktorego_rysujemy_linie
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    obiekt_najblizszy_myszcze = posortowane_obiekty[0]
    srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
    punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
    # *args, **kwargs - rozpakowanie w Python

    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(*srodek_obiektu_najbliszego_myszce))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci
    guzik1, guzik2, guzik3 =  pygame.mouse.get_pressed()
    if guzik1:
        obiekt_najblizszy_myszcze.szerokosc += 4

pygame.quit()

```





### Program ukladanie_obiektow2.py

Kod programu:
```python
# rysowanie lini od obiektu najbliższego myszce: do środka każdego obiektu i sortowanie obiektów przy tym
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

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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

    @staticmethod
    def nowy_kwadrat():
        return PoruszajacySieKwadracik(random.randint(0, SZEROKOSC_OKNA), random.randint(0, WYSOKOSC_OKNA))

    def __init__(self, x, y):
        super(PoruszajacySieKwadracik, self).__init__(x, y)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_kwadrat(),
                      PoruszajacySieKwadracik.nowy_kwadrat(),
                      Kolo(80, 100)]
punkt_od_ktorego_rysujemy_linie = (0, 0)

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = punkt_od_ktorego_rysujemy_linie
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    obiekt_najblizszy_myszcze = posortowane_obiekty[0]
    srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
    punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
    # *args, **kwargs - rozpakowanie w Python

    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(*srodek_obiektu_najbliszego_myszce))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci
    guzik1, guzik2, guzik3 =  pygame.mouse.get_pressed()
    if guzik1:
        obiekt_najblizszy_myszcze.szerokosc += 4

pygame.quit()

```





### Program ukladanie_obiektow3.py

Kod programu:
```python
# rysowanie lini od obiektu najbliższego myszce: do środka każdego obiektu i sortowanie obiektów przy tym
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

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

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

    @staticmethod
    def nowy_kwadrat():
        return PoruszajacySieKwadracik(random.randint(0, SZEROKOSC_OKNA), random.randint(0, WYSOKOSC_OKNA))

    @classmethod
    def nowy_obiekt(cls):
        return PoruszajacySieKwadracik(random.randint(0, SZEROKOSC_OKNA), random.randint(0, WYSOKOSC_OKNA))

    def __init__(self, x, y):
        super(PoruszajacySieKwadracik, self).__init__(x, y)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls):
        return Kolo(random.randint(0, SZEROKOSC_OKNA), random.randint(0, WYSOKOSC_OKNA))

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(),
                      PoruszajacySieKwadracik.nowy_obiekt(),
                      Kolo.nowy_obiekt(),
                      ]
punkt_od_ktorego_rysujemy_linie = (0, 0)

obiekty_na_ekranie[0].szerokosc = 90
obiekty_na_ekranie[1].wysokosc = 90


def paint_myszka():
    x, y = punkt_od_ktorego_rysujemy_linie
    # pygame.draw.line(background, (0, 0, 0), (0, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, 0), (x, y))
    # pygame.draw.line(background, (0, 0, 0), (SZEROKOSC_OKNA, WYSOKOSC_OKNA), (x, y))

    pygame.draw.line(background, (0, 0, 0), (0, y), (SZEROKOSC_OKNA, y))
    pygame.draw.line(background, (0, 0, 0), (x, 0), (x, WYSOKOSC_OKNA))
    for o in obiekty_na_ekranie:
        pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    for k in obiekty_na_ekranie:
        k.paint()
    paint_myszka()

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
    x, y = pygame.mouse.get_pos()
    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
    obiekt_najblizszy_myszcze = posortowane_obiekty[0]
    srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
    punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
    # *args, **kwargs - rozpakowanie w Python

    posortowane_obiekty = sorted(obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(*srodek_obiektu_najbliszego_myszce))
    for idx, o in enumerate(posortowane_obiekty):
        stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
        o.stopien_szarosci = stopien_szarosci
    guzik1, guzik2, guzik3 =  pygame.mouse.get_pressed()
    if guzik1:
        obiekt_najblizszy_myszcze.szerokosc += 4

pygame.quit()

```





### Program mediatorem_gry1.py

Kod programu:
```python
import random

import pygame

mediator = None

class FizykaOdbijajacegoSieObiektu:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > mediator.SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = mediator.SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > mediator.WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = mediator.WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    @classmethod
    def nowy_obiekt(cls):
        return PoruszajacySieKwadracik(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA))

    def __init__(self, x, y):
        super(PoruszajacySieKwadracik, self).__init__(x, y)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self, background):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls):
        return Kolo(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA))

    @classmethod
    def ile_wynosi_dodawanie(cls, a, b):
        return a + b

    def __init__(self, x, y):
        super(Kolo, self).__init__(x, y)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self, background):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Mediator:

    def __init__(self):
        self.obiekty_na_ekranie = []
        self.punkt_od_ktorego_rysujemy_linie = (0, 0)

        pygame.init()

        self.SZEROKOSC_OKNA = 400
        self.WYSOKOSC_OKNA = 400
        self.window = (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA)
        self.screen = pygame.display.set_mode(self.window)
        self.background = pygame.Surface(self.window)

    def uruchom_gre(self):
        self.obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(),
                                   PoruszajacySieKwadracik.nowy_obiekt(),
                                   Kolo.nowy_obiekt(),
                                   ]
        self.obiekty_na_ekranie[0].szerokosc = 90
        self.obiekty_na_ekranie[1].wysokosc = 90

        FPS = 60  # Frames per second.
        clock = pygame.time.Clock()
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
            self._paint(self.background)

            for k in self.obiekty_na_ekranie:
                k.update()
            x, y = pygame.mouse.get_pos()
            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
            obiekt_najblizszy_myszcze = posortowane_obiekty[0]
            srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
            self.punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
            # *args, **kwargs - rozpakowanie w Python

            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(
                *srodek_obiektu_najbliszego_myszce))
            for idx, o in enumerate(posortowane_obiekty):
                stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
                o.stopien_szarosci = stopien_szarosci
            guzik1, guzik2, guzik3 = pygame.mouse.get_pressed()
            if guzik1:
                obiekt_najblizszy_myszcze.szerokosc += 4

        pygame.quit()


    def _paint(self, background):
        pygame.draw.rect(self.background, (255, 255, 255), (0, 0, *self.window))

        for k in self.obiekty_na_ekranie:
            k.paint(background)
        self._paint_myszka(background)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def _update(self):
        pass

    def _paint_myszka(self, background):
        x, y = self.punkt_od_ktorego_rysujemy_linie

        pygame.draw.line(background, (0, 0, 0), (0, y), (self.SZEROKOSC_OKNA, y))
        pygame.draw.line(background, (0, 0, 0), (x, 0), (x, self.WYSOKOSC_OKNA))
        for o in self.obiekty_na_ekranie:
            pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


mediator = Mediator()
mediator.uruchom_gre()
```





### Program mediatorem_gry2.py

Kod programu:
```python
# brak globalnego mediatora

import random

import pygame

class PodwladnyMediatora:

    def __init__(self, mediator):
        self.mediator = mediator


class FizykaOdbijajacegoSieObiektu(PodwladnyMediatora):

    def __init__(self, x, y, mediator):
        super(FizykaOdbijajacegoSieObiektu, self).__init__(mediator)
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > self.mediator.SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = self.mediator.SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > self.mediator.WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = self.mediator.WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return PoruszajacySieKwadracik(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                                       mediator)

    def __init__(self, x, y, mediator):
        super(PoruszajacySieKwadracik, self).__init__(x, y, mediator)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self, background):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return Kolo(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                    mediator)

    @classmethod
    def ile_wynosi_dodawanie(cls, a, b):
        return a + b

    def __init__(self, x, y, mediator):
        super(Kolo, self).__init__(x, y, mediator)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self, background):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Mediator:

    def __init__(self):
        self.SZEROKOSC_OKNA = 400
        self.WYSOKOSC_OKNA = 400
        self.obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(self),
                                   PoruszajacySieKwadracik.nowy_obiekt(self),
                                   Kolo.nowy_obiekt(self),
                                   ]
        self.obiekty_na_ekranie[0].szerokosc = 90
        self.obiekty_na_ekranie[1].wysokosc = 90

        self.punkt_od_ktorego_rysujemy_linie = (0, 0)

    @property
    def window(self):
        return (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA)

    def uruchom_gre(self):
        pygame.init()

        screen = pygame.display.set_mode(self.window)
        background = pygame.Surface(self.window)

        FPS = 60  # Frames per second.
        clock = pygame.time.Clock()
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
            self._paint(background, screen)

            for k in self.obiekty_na_ekranie:
                k.update()
            x, y = pygame.mouse.get_pos()
            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
            obiekt_najblizszy_myszcze = posortowane_obiekty[0]
            srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
            self.punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
            # *args, **kwargs - rozpakowanie w Python

            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(
                *srodek_obiektu_najbliszego_myszce))
            for idx, o in enumerate(posortowane_obiekty):
                stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
                o.stopien_szarosci = stopien_szarosci
            guzik1, guzik2, guzik3 = pygame.mouse.get_pressed()
            if guzik1:
                obiekt_najblizszy_myszcze.szerokosc += 4

        pygame.quit()


    def _paint(self, background, screen):
        pygame.draw.rect(background, (255, 255, 255), (0, 0, *self.window))

        for k in self.obiekty_na_ekranie:
            k.paint(background)
        self._paint_myszka(background)

        screen.blit(background, (0, 0))
        pygame.display.flip()

    def _update(self):
        pass

    def _paint_myszka(self, background):
        x, y = self.punkt_od_ktorego_rysujemy_linie

        pygame.draw.line(background, (0, 0, 0), (0, y), (self.SZEROKOSC_OKNA, y))
        pygame.draw.line(background, (0, 0, 0), (x, 0), (x, self.WYSOKOSC_OKNA))
        for o in self.obiekty_na_ekranie:
            pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


ukryta_zmienna_mediator = Mediator()
ukryta_zmienna_mediator.uruchom_gre()
```





### Program mediatorem_gry3.py

Kod programu:
```python
# brak globalnego mediatora

import random

import pygame

class PodwladnyMediatora:

    def __init__(self, mediator):
        self.mediator = mediator


class FizykaOdbijajacegoSieObiektu(PodwladnyMediatora):

    def __init__(self, x, y, mediator):
        super(FizykaOdbijajacegoSieObiektu, self).__init__(mediator)
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > self.mediator.SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = self.mediator.SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > self.mediator.WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = self.mediator.WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return PoruszajacySieKwadracik(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                                       mediator)

    def __init__(self, x, y, mediator):
        super(PoruszajacySieKwadracik, self).__init__(x, y, mediator)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self, background):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return Kolo(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                    mediator)

    @classmethod
    def ile_wynosi_dodawanie(cls, a, b):
        return a + b

    def __init__(self, x, y, mediator):
        super(Kolo, self).__init__(x, y, mediator)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self, background):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Mediator:

    def __init__(self):
        self.SZEROKOSC_OKNA = 400
        self.WYSOKOSC_OKNA = 400
        self.obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(self),
                                   PoruszajacySieKwadracik.nowy_obiekt(self),
                                   Kolo.nowy_obiekt(self),
                                   ]
        self.obiekty_na_ekranie[0].szerokosc = 90
        self.obiekty_na_ekranie[1].wysokosc = 90

        self.punkt_od_ktorego_rysujemy_linie = (0, 0)

    def __add__(self, other):
        wynik = Mediator()
        wynik.obiekty_na_ekranie = self.obiekty_na_ekranie + other.obiekty_na_ekranie
        return wynik

    @property
    def window(self):
        return (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA)

    def uruchom_gre(self):
        pygame.init()

        screen = pygame.display.set_mode(self.window)
        background = pygame.Surface(self.window)

        FPS = 60  # Frames per second.
        clock = pygame.time.Clock()
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
            self._paint(background, screen)

            for k in self.obiekty_na_ekranie:
                k.update()
            x, y = pygame.mouse.get_pos()
            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
            obiekt_najblizszy_myszcze = posortowane_obiekty[0]
            srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
            self.punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
            # *args, **kwargs - rozpakowanie w Python

            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(
                *srodek_obiektu_najbliszego_myszce))
            for idx, o in enumerate(posortowane_obiekty):
                stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
                o.stopien_szarosci = stopien_szarosci
            guzik1, guzik2, guzik3 = pygame.mouse.get_pressed()
            if guzik1:
                obiekt_najblizszy_myszcze.szerokosc += 4

        pygame.quit()


    def _paint(self, background, screen):
        pygame.draw.rect(background, (255, 255, 255), (0, 0, *self.window))

        for k in self.obiekty_na_ekranie:
            k.paint(background)
        self._paint_myszka(background)

        screen.blit(background, (0, 0))
        pygame.display.flip()

    def _update(self):
        pass

    def _paint_myszka(self, background):
        x, y = self.punkt_od_ktorego_rysujemy_linie

        pygame.draw.line(background, (0, 0, 0), (0, y), (self.SZEROKOSC_OKNA, y))
        pygame.draw.line(background, (0, 0, 0), (x, 0), (x, self.WYSOKOSC_OKNA))
        for o in self.obiekty_na_ekranie:
            pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


mediator1 = Mediator()
mediator2 = Mediator()

koncowy_mediator = mediator1 + mediator2
koncowy_mediator.uruchom_gre()
```





### Program mediatorem_gry4.py

Kod programu:
```python
# metody madiczne madediatorze, dodawanie mediatorów

import random

import pygame

class PodwladnyMediatora:

    def __init__(self, mediator):
        self.mediator = mediator


class FizykaOdbijajacegoSieObiektu(PodwladnyMediatora):

    def __init__(self, x, y, mediator):
        super(FizykaOdbijajacegoSieObiektu, self).__init__(mediator)
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > self.mediator.SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = self.mediator.SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > self.mediator.WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = self.mediator.WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return PoruszajacySieKwadracik(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                                       mediator)

    def __init__(self, x, y, mediator):
        super(PoruszajacySieKwadracik, self).__init__(x, y, mediator)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self, background):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return Kolo(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                    mediator)

    @classmethod
    def ile_wynosi_dodawanie(cls, a, b):
        return a + b

    def __init__(self, x, y, mediator):
        super(Kolo, self).__init__(x, y, mediator)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self, background):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Mediator:

    def __init__(self):
        self.SZEROKOSC_OKNA = 400
        self.WYSOKOSC_OKNA = 400
        self.obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(self),
                                   PoruszajacySieKwadracik.nowy_obiekt(self),
                                   Kolo.nowy_obiekt(self),
                                   ]
        self.obiekty_na_ekranie[0].szerokosc = 90
        self.obiekty_na_ekranie[1].wysokosc = 90

        self.punkt_od_ktorego_rysujemy_linie = (0, 0)

    def __add__(self, other):
        if isinstance(other, Mediator):
            wynik = Mediator()
            wynik.obiekty_na_ekranie = self.obiekty_na_ekranie + other.obiekty_na_ekranie
            for o in wynik.obiekty_na_ekranie:
                o.mediator = wynik
            return wynik
        if isinstance(other, int):
            wynik = Mediator()
            wynik.obiekty_na_ekranie = self.obiekty_na_ekranie
            for o in wynik.obiekty_na_ekranie:
                o.mediator = wynik
            wynik.SZEROKOSC_OKNA = self.SZEROKOSC_OKNA + other
            wynik.WYSOKOSC_OKNA = self.WYSOKOSC_OKNA + other
            return wynik

    def __sub__(self, other):
        if isinstance(other, int):
            return self + (-other)

    @property
    def window(self):
        return (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA)

    def uruchom_gre(self):
        pygame.init()

        screen = pygame.display.set_mode(self.window)
        background = pygame.Surface(self.window)

        FPS = 60  # Frames per second.
        clock = pygame.time.Clock()
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
            self._paint(background, screen)

            for k in self.obiekty_na_ekranie:
                k.update()
            x, y = pygame.mouse.get_pos()
            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
            obiekt_najblizszy_myszcze = posortowane_obiekty[0]
            srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
            self.punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
            # *args, **kwargs - rozpakowanie w Python

            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(
                *srodek_obiektu_najbliszego_myszce))
            for idx, o in enumerate(posortowane_obiekty):
                stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
                o.stopien_szarosci = stopien_szarosci
            guzik1, guzik2, guzik3 = pygame.mouse.get_pressed()
            if guzik1:
                obiekt_najblizszy_myszcze.szerokosc += 4

        pygame.quit()


    def _paint(self, background, screen):
        pygame.draw.rect(background, (255, 255, 255), (0, 0, *self.window))

        for k in self.obiekty_na_ekranie:
            k.paint(background)
        self._paint_myszka(background)

        screen.blit(background, (0, 0))
        pygame.display.flip()

    def _update(self):
        pass

    def _paint_myszka(self, background):
        x, y = self.punkt_od_ktorego_rysujemy_linie

        pygame.draw.line(background, (0, 0, 0), (0, y), (self.SZEROKOSC_OKNA, y))
        pygame.draw.line(background, (0, 0, 0), (x, 0), (x, self.WYSOKOSC_OKNA))
        for o in self.obiekty_na_ekranie:
            pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


mediator1 = Mediator()
mediator2 = Mediator()

koncowy_mediator = mediator1 + mediator2
koncowy_mediator += 150
koncowy_mediator -= 90
koncowy_mediator.uruchom_gre()
```





### Program mediatorem_gry5.py

Kod programu:
```python
# metody madiczne madediatorze, dodawanie mediatorów
import math
import random

import pygame

class PodwladnyMediatora:

    def __init__(self, mediator):
        self.mediator = mediator


class FizykaOdbijajacegoSieObiektu(PodwladnyMediatora):

    def __init__(self, x, y, mediator):
        super(FizykaOdbijajacegoSieObiektu, self).__init__(mediator)
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3
        self.szerokosc = 50
        self.wysokosc = 50

    @property
    def srodek_obiektu_x(self):
        return self.x + self.szerokosc / 2

    @property
    def srodek_obiektu_y(self):
        return self.y + self.wysokosc / 2

    def oblicz_kw_odleglosci(self, x, y):
        return (self.srodek_obiektu_x - x)**2 + (self.srodek_obiektu_y - y)**2

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + self.szerokosc > self.mediator.SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = self.mediator.SZEROKOSC_OKNA - self.szerokosc
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + self.wysokosc > self.mediator.WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = self.mediator.WYSOKOSC_OKNA - self.wysokosc


class PoruszajacySieKwadracik(FizykaOdbijajacegoSieObiektu):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return PoruszajacySieKwadracik(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                                       mediator)

    def __init__(self, x, y, mediator):
        super(PoruszajacySieKwadracik, self).__init__(x, y, mediator)
        self.stopien_szarosci = 0.5

    @property
    def kolor(self):
        return (int(255*self.stopien_szarosci), int(255*self.stopien_szarosci), int(255*self.stopien_szarosci))

    def paint(self, background):
        pygame.draw.rect(background, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))

    def __str__(self):
        return f'Kwadrat o wymiarach ({self.szerokosc}, {self.wysokosc})'

    def __repr__(self):
        return f'< PoruszajacySieKwadracik({self.x}, {self.y}, {repr(self.mediator)}) >'

    def __float__(self):
        return float(self.szerokosc * self.wysokosc)

class Kolo(PoruszajacySieKwadracik):

    @classmethod
    def nowy_obiekt(cls, mediator):
        return Kolo(random.randint(0, mediator.SZEROKOSC_OKNA), random.randint(0, mediator.WYSOKOSC_OKNA),
                    mediator)

    @classmethod
    def ile_wynosi_dodawanie(cls, a, b):
        return a + b

    def __init__(self, x, y, mediator):
        super(Kolo, self).__init__(x, y, mediator)
        self.promien = 25
        self.krok_zmiany_promienia = 0.1

    def paint(self, background):
        pygame.draw.rect(background, (255, 0, 0), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.circle(background, self.kolor, (self.x + self.promien, self.y + self.promien), self.promien)

    @property
    def wysokosc(self):
        return 2 * self.promien

    @wysokosc.setter
    def wysokosc(self, nowa_wysokosc):
        self.promien = nowa_wysokosc / 2

    @property
    def szerokosc(self):
        return 2 * self.promien

    @szerokosc.setter
    def szerokosc(self, nowa_szerokosc):
        self.promien = nowa_szerokosc / 2

    def update(self):
        super(Kolo, self).update()

        self.promien += self.krok_zmiany_promienia
        if self.promien > 50:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia
        elif self.promien < 10:
            self.krok_zmiany_promienia = -self.krok_zmiany_promienia

    def __str__(self):
        return f'Kolo o promieniu {self.promien}'

    def __float__(self):
        return math.pi * self.promien ** 2

def losowy_kolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Mediator:

    def __init__(self):
        self.SZEROKOSC_OKNA = 400
        self.WYSOKOSC_OKNA = 400
        self.obiekty_na_ekranie = [PoruszajacySieKwadracik.nowy_obiekt(self),
                                   PoruszajacySieKwadracik.nowy_obiekt(self),
                                   Kolo.nowy_obiekt(self),
                                   ]
        self.obiekty_na_ekranie[0].szerokosc = 90
        self.obiekty_na_ekranie[1].wysokosc = 90

        self.punkt_od_ktorego_rysujemy_linie = (0, 0)

    def __add__(self, other):
        if isinstance(other, Mediator):
            wynik = Mediator()
            wynik.obiekty_na_ekranie = self.obiekty_na_ekranie + other.obiekty_na_ekranie
            for o in wynik.obiekty_na_ekranie:
                o.mediator = wynik
            return wynik
        if isinstance(other, int):
            wynik = Mediator()
            wynik.obiekty_na_ekranie = self.obiekty_na_ekranie
            for o in wynik.obiekty_na_ekranie:
                o.mediator = wynik
            wynik.SZEROKOSC_OKNA = self.SZEROKOSC_OKNA + other
            wynik.WYSOKOSC_OKNA = self.WYSOKOSC_OKNA + other
            return wynik

    def __sub__(self, other):
        if isinstance(other, int):
            return self + (-other)

    def __iter__(self):
        return iter(self.obiekty_na_ekranie)

    def __int__(self):
        return len(self.obiekty_na_ekranie)

    @property
    def window(self):
        return (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA)

    def uruchom_gre(self):
        pygame.init()

        screen = pygame.display.set_mode(self.window)
        background = pygame.Surface(self.window)

        FPS = 60  # Frames per second.
        clock = pygame.time.Clock()
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
            self._paint(background, screen)

            for k in self.obiekty_na_ekranie:
                k.update()
            x, y = pygame.mouse.get_pos()
            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(x, y))
            obiekt_najblizszy_myszcze = posortowane_obiekty[0]
            srodek_obiektu_najbliszego_myszce = obiekt_najblizszy_myszcze.srodek_obiektu_x, obiekt_najblizszy_myszcze.srodek_obiektu_y
            self.punkt_od_ktorego_rysujemy_linie = srodek_obiektu_najbliszego_myszce
            # *args, **kwargs - rozpakowanie w Python

            posortowane_obiekty = sorted(self.obiekty_na_ekranie, key=lambda obiekt: obiekt.oblicz_kw_odleglosci(
                *srodek_obiektu_najbliszego_myszce))
            for idx, o in enumerate(posortowane_obiekty):
                stopien_szarosci = (len(posortowane_obiekty) - idx) / (len(posortowane_obiekty) + 1)
                o.stopien_szarosci = stopien_szarosci
            guzik1, guzik2, guzik3 = pygame.mouse.get_pressed()
            if guzik1:
                obiekt_najblizszy_myszcze.szerokosc += 4

        pygame.quit()


    def _paint(self, background, screen):
        pygame.draw.rect(background, (255, 255, 255), (0, 0, *self.window))

        for k in self.obiekty_na_ekranie:
            k.paint(background)
        self._paint_myszka(background)

        screen.blit(background, (0, 0))
        pygame.display.flip()

    def _update(self):
        pass

    def _paint_myszka(self, background):
        x, y = self.punkt_od_ktorego_rysujemy_linie

        pygame.draw.line(background, (0, 0, 0), (0, y), (self.SZEROKOSC_OKNA, y))
        pygame.draw.line(background, (0, 0, 0), (x, 0), (x, self.WYSOKOSC_OKNA))
        for o in self.obiekty_na_ekranie:
            pygame.draw.line(background, (0, 0, 0), (x, y), (o.srodek_obiektu_x, o.srodek_obiektu_y))


mediator1 = Mediator()
mediator2 = Mediator()

koncowy_mediator = mediator1 + mediator2
koncowy_mediator += 150
koncowy_mediator -= 90

print(f'Kocowy mediator ma {int(koncowy_mediator)} obiektów')

koncowy_mediator.uruchom_gre()

for o in koncowy_mediator:
    print(f'{o} ma pole {float(o)}')
```





### Program dekoratory_w_konsoli1.py

Kod programu:
```python
lista = [-4, 56, -7, 66, 102, 9]

print(sorted(lista, key=lambda x: x * x))

funkcja_jako_zmienna = lambda x: x * x

def funkcja(a, b):
    return a + b

def funkcja2_(a, b):
    return 2 * funkcja(a, b)

funkcja2 = lambda a, b: 2 * funkcja(a, b)

print(funkcja2(2, 3))
print(funkcja2_(2, 3))


def dekorator(orginalna_funckja):
    return lambda a, b: 2 * orginalna_funckja(a, b)

@dekorator
def funkcja(a, b):
    return a + b

# funkcja = dekorator(funkcja)

print(funkcja(2, 3))

def printuj(orginalna_funckja):
    def _nowa_funkcja(a, b):
        print(f'dekortor otoczył wywołanie z {a, b}')
        return orginalna_funckja(a, b)
    return _nowa_funkcja

@printuj
def funkcja(a, b):
    return a + b

print(funkcja(2, 3))
```



Output:
```
[-4, -7, 9, 56, 66, 102]
10
10
10
dekortor otoczył wywołanie z (2, 3)
5

```





### Program dekoratory_w_konsoli2.py

Kod programu:
```python
def printuj(orginalna_funckja):
    def _nowa_funkcja(*args, **kwargs):
        print(f'dekortor otoczył wywołanie z {args, kwargs}')
        return orginalna_funckja(*args, **kwargs)
    return _nowa_funkcja

@printuj
def funkcja(a, b, c):
    return a + b + c

def dekorator_dodaj_wszystko(orginalna_funckja):
    def _nowa_funkcja(*args):
        suma = sum(args)
        return orginalna_funckja(suma)
    return _nowa_funkcja

print(funkcja(2, 3, 9))

@printuj
@dekorator_dodaj_wszystko
@printuj
def wypisz_jedna_liczbe(x):
    print(f'x = {x}')

wypisz_jedna_liczbe(88)
wypisz_jedna_liczbe(88, 12)
```



Output:
```
dekortor otoczył wywołanie z ((2, 3, 9), {})
14
dekortor otoczył wywołanie z ((88,), {})
dekortor otoczył wywołanie z ((88,), {})
x = 88
dekortor otoczył wywołanie z ((88, 12), {})
dekortor otoczył wywołanie z ((100,), {})
x = 100

```





### Program dekoratory_w_konsoli3.py

Kod programu:
```python
def dekorator(funkcja):
    if 'cicha' in funkcja.__name__:
        return funkcja
    def _nowa_funkcja(*args, **kwargs):
        print(f'wywołano: {funkcja.__name__}')
        return funkcja(*args, **kwargs)
    return _nowa_funkcja

@dekorator
def funkcja_sumujaca(a, b):
    return a + b

@dekorator
def cicha_funkcja_sumujaca(a, b):
    return a + b

@dekorator
def mnozenie(a, b, c):
    return a * b * c

print(funkcja_sumujaca(1, 2))
print(cicha_funkcja_sumujaca(1, 2))
print(mnozenie(1, 2, 3))
```



Output:
```
wywołano: funkcja_sumujaca
3
3
wywołano: mnozenie
6

```





### Program dekoratory_w_konsoli4.py

Kod programu:
```python
lista_opcji = []

def dodaj_jako_opcje_programu(funckja):
    lista_opcji.append((funckja.__name__, funckja))
    return funckja

@dodaj_jako_opcje_programu
def pokaz_liste():
    print('pokazuje liste..')

@dodaj_jako_opcje_programu
def dodaj_do_listy():
    print('dodaje do listy')

for i, (nazwa, _) in enumerate(lista_opcji):
    print(f'{i+1}. {nazwa}')
odp = int(input('Co chcesz zrobić?: '))
funckcja_do_wykonania = lista_opcji[odp-1][1]
funckcja_do_wykonania()
```



PRzerobiony materiał:
 - gettery i settery

 - paradygmat funkcyjny

[//]: # (funkcja rysująca jako atrybut)
 - sortowanie obiektów na ekranie, podanie funkcji sortującej
 - sortowanie obiektów na ekranie, podanie funkcji sortującej przez lambda
 - lambda

[//]: # (dekoratory)

[//]: # ( - instance, static, class methods)

 - mediator do zarządzania całą grą
 - iterator obiektów
 - porównywanie obiektów przez ich pole powierzchni
 - własne dekoratory