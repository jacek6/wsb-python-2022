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

lista_miesiecy = ['styczen', 'luty', 'marzec', 'kwiecen', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrze',
                  'paz', 'listopad', 'grudzien']

def str_do_int_miesiac(nazwa_miesiaca):
    return lista_miesiecy.index(nazwa_miesiaca) + 1


def podaj_date(**kwargs) -> datetime.date:
    if 'miesiac_nazwa' in kwargs:
        kwargs['miesiac'] = str_do_int_miesiac(kwargs['miesiac_nazwa'])
        del kwargs['miesiac_nazwa']
    for nazwa_pola in pola_daty.keys():
        if nazwa_pola in kwargs:
            print(f'Podano z góry {nazwa_pola}: {kwargs[nazwa_pola]}')
    for nazwa_pola, zakres_pola in pola_daty.items():
        if nazwa_pola not in kwargs:
            print(f'proszę podać {nazwa_pola}:')
            kwargs[nazwa_pola] = podaj_liczbe_z_zakresu(*zakres_pola)

    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac_nazwa='listopad')
print(data)
