import datetime


def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def podaj_date_urodzenia() -> datetime.date:
    print('Podaj dzien urodzenia')
    dzien = podaj_liczbe_z_zakresu(1, 31)

    print('Podaj miesiac urodzenia')
    miesiec = podaj_liczbe_z_zakresu(1, 12)

    rok = int(input('Podaj rok urodzenia: '))

    return datetime.date(year=rok, month=miesiec, day=dzien)

def wypisz_ile_czasu_minelo(od_kiedy: datetime.date):
    do_kiedy = datetime.date.today()
    roznica_w_czasie = do_kiedy - od_kiedy
    roznica_w_dniach = roznica_w_czasie.days
    print('od czasu uordzania ', od_kiedy, ' minęło ', roznica_w_dniach, ' dni')

    roznica_w_latach = roznica_w_dniach // 365
    print('od czasu uordzania ', od_kiedy, ' minęło ', roznica_w_latach, ' lat i ', roznica_w_dniach % 365, ' dni')

data_urodzenia = podaj_date_urodzenia()

print('data_urodzenia = ', data_urodzenia)

wypisz_ile_czasu_minelo(data_urodzenia)