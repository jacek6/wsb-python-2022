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