uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
szukany_uzytkownik = input('Podaj nazwe uzytkowanika: ')

czy_znaleziono = 'nie znaleziono'
for i in range(len(uzytkownicy)):
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')
        czy_znaleziono = 'znaleziono uzytkowania'

if czy_znaleziono == 'nie znaleziono':
    print('Nie udalo sie znaleść uzytkownika na liscie')
if czy_znaleziono == 'znaleziono uzytkowania':
    print('Znaleziono podanego uzytkownika')
