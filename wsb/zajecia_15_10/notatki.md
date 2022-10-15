# Notatki 15.10.2022 Python

## If
Temat czy jest instrukcja warunkowa IF. Patrz sekscje poniżej:
### Definicje
Pokazanie czym jest IF:
plik `if_prosty.py`
```python
wiek = int(input('podaj wiek: '))

if wiek > 18:
    print('jestes pelnoletni')
elif wiek == 18:
    print('masz rowno 18')
else:
    print('nie jestes')

print('koniec programu')
```
### Zadanie 1 a
Zadanie z PDF:
Napisz program, który spyta użytkownika o zarobki brutto oraz o 
liczbę dzieci, a następnie obliczy, ile użytkownik dostanie pieniędzy 
netto.

a) podatek wynosi 20%, a na każde dziecko przysługuje 500 zł


Plik `if_zadanie_1_a.py`
```python
liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))

zarobki_netto = 0.8 * zarobki_brutto + 500 * liczba_dzieci
print('Twoje zarobki netto to: ', zarobki_netto, ' zł')
```
### Zdanie 1 B
Napisz program, który spyta użytkownika o zarobki brutto oraz o 
liczbę dzieci, a następnie obliczy, ile użytkownik dostanie pieniędzy 
netto.

b) podatek wynosi 10%, gdy zarabiamy powyżej 3000 zł i 20%, gdy 
zarabiamy powyżej 5000 zł. Program 500+ przysługuje tylko na 
drugie i trzecie dziecko

plik `if_zadanie_1_b.py`
```python
liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))


if zarobki_brutto < 3000:
    zarobki_netto = zarobki_brutto
elif zarobki_brutto < 5000:
    zarobki_netto = zarobki_brutto * 0.9
else:
    zarobki_netto = zarobki_brutto * 0.8

if liczba_dzieci >= 2:
    zarobki_netto += 500
if liczba_dzieci >= 3:
    zarobki_netto += 500

print('Twoje zarobki netto to: ', zarobki_netto, ' zł')
```

### Zadanie 2

Napisz program, który zapyta o wymiary mieszkania oraz o typ 
mieszkania i wypisze miesięczny koszt ogrania mieszkania.
a) Mieszkanie z cegły - ogrzanie 1m^3 to 30gr dziennie
b) Mieszkanie z płyty - ogrzanie 1m^3 to 50gr dziennie

plik `if_zadanie_2.py`

```python
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
```

### Komnetarz
Pamiętajcie o dodaniu spacji na końcu pytania do użytkownika.

To znaczy aby pisać:
```python
input('Podaj liczbę metrów kw mieszknia: ')
```

a nie:

```python
input('Podaj liczbę metrów kw mieszknia:')
```
## Pętle

### Co to pętla
plik `loops.py`
```python
print('Witamy w programie')
x = int(input('Ile razy chcesz wykonać pętlę? '))
for i in range (x): #wykonanie akcji „x” razy
    print('To jest ', i, ' wykonanie') #wszystkie linie z wcięciem
    print('Lecimy dalej') #wykonają się w petli
print('Koniec pętli')
```

### Zadanie 1.1
Dana jest lista liczb całkowitych
`Lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]`
1. Napisz program, który wyświetli po kolei wszystkie liczby razem 
z ich miejscem w liście

plik `loops_zad_1_1.py`
```python
lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]

print(lista)
print(lista[0])
print(lista[1])
print(len(lista))

for i in range ( len(lista) ):
    print('wykonanie petli nr ', i, ' wartosc listy = ', lista[i])
```

### Zadanie 1.2
Dana jest lista liczb całkowitych
`Lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]`
2. Napisz program, który wyświetli tylko liczby parzyste LUB liczby 
większe od 10

plik `loops_zad_1_2.py`
```python
lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]

for i in range ( len(lista) ):
    if lista[i] % 2 == 0 or lista[i] > 10:
        print('wykonanie petli nr ', i, ' wartosc listy = ', lista[i])

```

### zadanie 2
Dana jest lista nazw użytkowników
`uzytkownicy = ['kamil', 'marek', 'mandarynka98’, 
'nowy1', 'pixi’]`
Napisz program, który zapyta o nazwę użytkownika oraz 
poinformuje, czy nazwa użytkownika jest wolna, a jeśli nie, to 
poinformuje, na którym miejscu w liście jest zapisany dany 
użytkownik.

Etapy rozwiązania i pytania poniżej:


### Sposby iterowania po liście
Są 3 sposoby na jakie można iterować po liście i szukań tam danego elementu.

plik `loops_iterowania.py`

```python
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

```

### range vs. enumarate

`range` przyjmuje TYLKO liczbę

`enumarate` musi dostać całą listę żeby po niej przejść

plik `loops_range_vs_enumerate.py`
```python
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
```

### startowanie nie od zerowego elementu
Trzeba zamienić `range(len(uzytkownicy))` na `range(2, len(uzytkownicy))`.

Czyli tylko dodać od któego elementu zacząć.

plik `loops_range_start.py`
```python
uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
szukany_uzytkownik = 'marek'

print('   # iterowanie normalnie')
for i in range(len(uzytkownicy)):
    print('sprawdzam czy ', szukany_uzytkownik, ' to ', uzytkownicy[i])
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')

print('   # iterowanie od indeksu 2')
for i in range(2, len(uzytkownicy)):
    print('sprawdzam czy ', szukany_uzytkownik, ' to ', uzytkownicy[i])
    if szukany_uzytkownik == uzytkownicy[i]:
        print('Znalezino uzytkownika ', szukany_uzytkownik, ' na pozycji ', i, ' w liscie')
```

### if True False

Wersja prosta:

plik `loops_zad_2.py`
```python
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

```

Wersja ulepszona:

plik `loops_zad_2_bool.py`
```python
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
```

Wersja jeszcze ulepszona

plik: `loops_zad_2_bool_krocej.py`
```python
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
```

wersja nejlepsza:

plik: `loops_zad_2_bool_krocej2.py`
```python
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
```
