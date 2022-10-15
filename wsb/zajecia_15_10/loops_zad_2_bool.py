uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
szukany_uzytkownik = input('Podaj nazwe uzytkowanika: ')

czy_znaleziono = False
# wersja prosta:
for i in range(len(uzytkownicy)):
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')
        czy_znaleziono = True

# 'nie znaleziono' -> False
# 'znaleziono uzytkowania' -> True
if czy_znaleziono == False:
    print('Nie udalo sie znaleść uzytkownika na liscie')
if czy_znaleziono == True:
    print('Znaleziono podanego uzytkownika')