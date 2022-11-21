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

pola_daty = {'dzien': [1, 31], 'miesiac': [1, 12], 'rok': [1000, 2022]}

def podaj_date(**kwargs) -> datetime.date:
    for nazwa_pola in pola_daty.keys():
        if nazwa_pola in kwargs:
            print(f'Podano z góry {nazwa_pola}: {kwargs[nazwa_pola]}')
    for nazwa_pola, zakres_pola in pola_daty.items():
        if nazwa_pola not in kwargs:
            print(f'proszę podać {nazwa_pola}:')
            kwargs[nazwa_pola] = podaj_liczbe_z_zakresu(*zakres_pola)
    return stworz_date(**kwargs)


data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')