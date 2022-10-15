uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

szukany_uzytkownik = 'marek'

# wersja prosta:
for i in range(len(uzytkownicy)):
    print('sprawdzam czy ', szukany_uzytkownik, ' to ', uzytkownicy[i])
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')

# wersja skrótowa bez indeksu
for u in uzytkownicy:
    if szukany_uzytkownik == u:
        print('znaleziono ', u)

# wersja skrótowa z indeksem
for i, u in enumerate(uzytkownicy):
    if szukany_uzytkownik == u:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')
