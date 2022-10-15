uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
szukany_uzytkownik = input('Podaj nazwe uzytkowanika: ')

czy_znaleziono = False
for i in range(len(uzytkownicy)):
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')
        czy_znaleziono = True

if czy_znaleziono:
    print('Znaleziono podanego uzytkownika')
else:
    print('Nie udalo sie znaleść uzytkownika na liscie')