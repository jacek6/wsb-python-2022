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
    print('podano kwargs: ', kwargs)

    if 'dzien' not in kwargs:
        print('Podaj dzien urodzenia')
        kwargs['dzien'] = podaj_liczbe_z_zakresu(1, 31)

    if 'miesiac' not in kwargs:
        print('Podaj miesiac urodzenia')
        kwargs['miesiac'] = podaj_liczbe_z_zakresu(1, 12)

    if 'rok' not in kwargs:
        kwargs['rok'] = int(input('Podaj rok urodzenia: '))

    print('pełny słownik: ', kwargs)
    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')