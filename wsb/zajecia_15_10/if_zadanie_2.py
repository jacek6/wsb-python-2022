liczba_metrow_kw = float(input('Podaj liczbę metrów kw mieszknia: '))
wyskosc_mieszkania = float(input('Podaj wysokosc mieszkanie w metrach: '))

typ_mieszkania = input('Podaj z czego jest mieszkanie (cegla/plyta): ')

objectosc_mieszkania = liczba_metrow_kw * wyskosc_mieszkania

if typ_mieszkania == 'cegla':
    print('Twoj koszt ogrzenia to ', f'{objectosc_mieszkania * 0.3:.2f}', ' zł dziennie')
elif typ_mieszkania == 'plyta':
    print('Twoj koszt ogrzenia to ', objectosc_mieszkania * 0.5, ' zł dziennie')
else:
    print('nie rozpoznano typu mieszknia: ', typ_mieszkania)