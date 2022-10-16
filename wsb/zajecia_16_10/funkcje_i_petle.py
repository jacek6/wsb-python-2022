szukany_uzytkownik = input('Podaj nazwe uzytkowanika: ') # marek

uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

def sprawdz_uzytkownika():
    print('sprawdzam czy ', szukany_uzytkownik, ' jest wśród ', len(uzytkownicy))
    for u in uzytkownicy:
        print('porownuje z uzytkownikem ', u)
        if u == szukany_uzytkownik:
            return True
    return False

if sprawdz_uzytkownika():
    print('znaleziono uzytkownika')
else:
    print('nie znaleziono uzytkownika')
