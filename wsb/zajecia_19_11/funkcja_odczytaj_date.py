"""

Zdefiniuj funkcje podaj_date,


Funkcja ma powiedzieć, co już wie i spytać się o to czego brakuje

Przykładowe użycia:
data = podaj_date(dzien=19, miesiac=11)

Mam podany dzień: 19
Mam podany miesiąc: 11
Proszę podać rok: ...

data = podaj_date(rok=2022)
Podaj dzień...
Podaj miesiesiąc: ...
MAm podany rok: 2022
"""

import datetime
def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)


def podaj_date(**kwargs) -> datetime.date:

    if 'dzien' in kwargs:
        print('Mam podany dzien ', kwargs['dzien'])
    else:
        print('Podaj dzien urodzenia')
        kwargs['dzien'] = podaj_liczbe_z_zakresu(1, 31)

    if 'miesiac' in kwargs:
        print('Mam podany miesiac ', kwargs['miesiac'])
    else:
        print('Podaj miesiac urodzenia')
        kwargs['miesiac'] = podaj_liczbe_z_zakresu(1, 12)

    if 'rok' in kwargs:
        print('Mam podany rok ', kwargs['rok'])
        print(f'Mam podany rok {kwargs["rok"]} ')
    else:
        kwargs['rok'] = int(input('Podaj rok urodzenia: '))

    print('pełny słownik: ', kwargs)
    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')