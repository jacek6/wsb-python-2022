uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
szukany_uzytkownik = 'marek'

print('   # iterowanie normalnie')
for i in range(len(uzytkownicy)):
    print('sprawdzam czy ', szukany_uzytkownik, ' to ', uzytkownicy[i])
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')

print('   # iterowanie enumarate')
for i, u in enumerate(uzytkownicy):
    print('sprawdzam czy ', szukany_uzytkownik, ' to ', u)
    if szukany_uzytkownik == u:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')

print()
print()
print()

for i in range(5):
    print('range zwrocil ', i)