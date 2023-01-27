
## Zbiory
Podstawowe operacje na zbiorach:



### Program zbiory_przyklad1

Kod programu:
```python
zbior = {1, 2, 3, 4}

print(zbior)

print()
print('Dodawanie zbiorów')
print(zbior.union({1, 2}))
print('Dodawaie listy:')
print([1, 2, 3, 4] + [1, 2])

print()
print('Dodawanie zbiorów')
print(zbior.union({1, 2, 'A'}))
```



Output:
```
{1, 2, 3, 4}



Dodawanie zbiorów

{1, 2, 3, 4}

Dodawaie listy:

[1, 2, 3, 4, 1, 2]



Dodawanie zbiorów

{1, 2, 3, 4, 'A'}


```





### Program zbiory_przyklad2

Kod programu:
```python
A = {1, 2, 3, 4}
B = {1, 2, 30, 40}

print("Suma:", A.union(B))  # wszystkie elementy zbiorów A i B
print("Część wspólna:", A.intersection(B))  # część wspólna zbiorów A i B
print("Różnica A-B:", A.difference(B))
print("Różnica B-A:", B.difference(A))
print("Różnica symetryczna:", A.symmetric_difference(B))

print("Zbior A ma długość ", len(A), " - zbior A: ", A)

```



Output:
```
Suma: {1, 2, 3, 4, 40, 30}

Część wspólna: {1, 2}

Różnica A-B: {3, 4}

Różnica B-A: {40, 30}

Różnica symetryczna: {3, 4, 40, 30}

Zbior A ma długość  4  - zbior A:  {1, 2, 3, 4}


```



## Zadania

Sprawdźmy:
 - ile jest osób, które chorowały w ostatnim roku na Krzykach.
 - ile jest osób z Krzyków chorowało w ostatnim roku.
 - ile osób chorowało w ostatnim miesiącu w centrum.
 - ile osób mieszka w sumie w centrum i na krzykach.




### Program zbiory_zadanie1

Kod programu:
```python
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# Sprawdźmy:
# ile jest osób, które chorowały w ostatnim roku na Krzykach.
print('ile jest osób, które chorowały w ostatnim roku na Krzykach: ', len(krzyki.intersection(chorzy_rok)))
# ile jest osób z Krzyków chorowało w ostatnim roku.
print('ile jest osób z Krzyków chorowało w ostatnim roku: ', len(krzyki.intersection(chorzy_rok)))
# ile osób chorowało w ostatnim miesiącu w centrum.
print('ile osób chorowało w ostatnim miesiącu w centrum: ', len(centrum.intersection(chorzy_miesiac)))
# ile osób mieszka w sumie w centrum i na krzykach.
print('ile osób mieszka w sumie w centrum i na krzykach: ', len(centrum.union(krzyki)))

print('ile jest osób z Krzyków chorowało w ostatnim miesiacu: ', len(krzyki.intersection(chorzy_miesiac)))


```



Output:
```
ile jest osób, które chorowały w ostatnim roku na Krzykach:  5

ile jest osób z Krzyków chorowało w ostatnim roku:  5

ile osób chorowało w ostatnim miesiącu w centrum:  2

ile osób mieszka w sumie w centrum i na krzykach:  13

ile jest osób z Krzyków chorowało w ostatnim miesiacu:  2


```



Sprawdźmy poprawność danych: 
 - każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.
 - nikt nie powinien mieszkać jednocześnie w Centrum i na Krzykach – jeśli tak, trzeba usunąć.
 - każdy: chory, zdrowy, z Krzyków i z Centrum, powinien być w bazie NFZ, jeśli nie ma, trzeba dopisać.




### Program zbiory_zadanie2

Kod programu:
```python
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()
#  Sprawdźmy poprawność danych:
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.
if chorzy_rok.intersection(chorzy_miesiac) == chorzy_miesiac:
    print('każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.')
else:
    print('BŁĄD !')

# nikt nie powinien mieszkać jednocześnie w Centrum i na Krzykach – jeśli tak, trzeba usunąć.
if krzyki.intersection(centrum):
    print("Ktoś mieszka na krzykach i w centrum: ", krzyki.intersection(centrum))

# każdy: chory, zdrowy, z Krzyków i z Centrum, powinien być w bazie NFZ, jeśli nie ma, trzeba dopisać.
osoby_do_dopisania_do_NFZ = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    if NFZ.intersection(zbior) != zbior:
        kto_jest_poza_nfz = zbior.difference(NFZ.intersection(zbior))
        assert NFZ.union(kto_jest_poza_nfz).intersection(zbior) == zbior
        print("ktoś jest poza bazą NFZ, ze zbioru: ", nazwa, " te osoby to ", kto_jest_poza_nfz)
        osoby_do_dopisania_do_NFZ = osoby_do_dopisania_do_NFZ.union(kto_jest_poza_nfz)

print("dopisze do NFZ osoby: ", osoby_do_dopisania_do_NFZ)
NFZ = NFZ.union(osoby_do_dopisania_do_NFZ)

print('teraz NFZ to: ', NFZ)
```



Output:
```
każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.

Ktoś mieszka na krzykach i w centrum:  {2345, 3254}

ktoś jest poza bazą NFZ, ze zbioru:  chorzy_rok  te osoby to  {3098}

ktoś jest poza bazą NFZ, ze zbioru:  chorzy_miesiac  te osoby to  {3098}

ktoś jest poza bazą NFZ, ze zbioru:  centrum  te osoby to  {3987}

dopisze do NFZ osoby:  {3098, 3987}

teraz NFZ to:  {4544, 8769, 6532, 7688, 6732, 1234, 1298, 3476, 3987, 3098, 1243, 3423, 7648, 6435, 2345, 2356, 3254, 5436}


```



Żeńskie Numery PESEL mają ostatnią cyfrę parzystą, męskie – nieparzystą. Zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ).



### Program zbiory_zadanie3

Kod programu:
```python
 # Żeńskie Numery PESEL mają ostatnią cyfrę parzystą, męskie – nieparzystą.
 # Zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ).

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

def podziel_zbiory(zbior):
    damski = set()
    meski = set()
    for e in zbior:
        if e % 2 == 0:
            damski.add(e)
            # damski = damski.union({e})
        else:
            meski.add(e)
    return damski, meski

zbior_wszystkich = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    damski, meski = podziel_zbiory(zbior)
    print()
    print('W zbiorze ', nazwa)
    print('kobiety to ', damski)
    print('mężczyźni to ', meski)

    zbior_wszystkich = zbior_wszystkich.union(zbior)

damski, meski = podziel_zbiory(zbior_wszystkich)
print('wszystkich kobiet jest ', len(damski))
print('wszystkich mężczyzn jest ', len(meski))
```



Output:
```


W zbiorze  chorzy_rok

kobiety to  {4544, 1234, 3476, 3254, 3098, 5436}

mężczyźni to  {8769, 3423}



W zbiorze  chorzy_miesiac

kobiety to  {4544, 1234, 3098, 3476}

mężczyźni to  {3423}



W zbiorze  krzyki

kobiety to  {4544, 6532, 5436, 3254}

mężczyźni to  {8769, 1243, 3423, 2345}



W zbiorze  centrum

kobiety to  {7648, 1234, 3476, 2356, 3254}

mężczyźni to  {2345, 3987}

wszystkich kobiet jest  9

wszystkich mężczyzn jest  5


```





### Program zbiory_zadanie3_ver2.py

Kod programu:
```python
 # Żeńskie Numery PESEL mają ostatnią cyfrę parzystą, męskie – nieparzystą.
 # Zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ).

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

def podziel_zbiory(zbior):
    damski = {e for e in zbior if e % 2 == 0}
    meski = {e for e in zbior if e % 2 == 1}
    return damski, meski

zbior_wszystkich = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    damski, meski = podziel_zbiory(zbior)
    print()
    print('W zbiorze ', nazwa)
    print('kobiety to ', damski)
    print('mężczyźni to ', meski)

    zbior_wszystkich = zbior_wszystkich.union(zbior)

damski, meski = podziel_zbiory(zbior_wszystkich)
print('wszystkich kobiet jest ', len(damski))
print('wszystkich mężczyzn jest ', len(meski))
```



Output:
```


W zbiorze  chorzy_rok

kobiety to  {4544, 1234, 3476, 3254, 3098, 5436}

mężczyźni to  {8769, 3423}



W zbiorze  chorzy_miesiac

kobiety to  {4544, 1234, 3098, 3476}

mężczyźni to  {3423}



W zbiorze  krzyki

kobiety to  {4544, 6532, 5436, 3254}

mężczyźni to  {8769, 1243, 3423, 2345}



W zbiorze  centrum

kobiety to  {7648, 1234, 3476, 2356, 3254}

mężczyźni to  {2345, 3987}

wszystkich kobiet jest  9

wszystkich mężczyzn jest  5


```


Wypiszmy:
 - kobiety z Krzyków, które były chore w ostatnim roku.
 - wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku.




### Program zbiory_zadanie4

Kod programu:
```python
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

# Wypiszmy:
# kobiety z Krzyków, które były chore w ostatnim roku.
print('kobiety z Krzyków, które były chore w ostatnim roku ', {e for e in krzyki.intersection(chorzy_rok) if e % 2 == 0})
# wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku.
print('wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku ',
      {e for e in centrum.difference(chorzy_rok) if e % 2 == 1})

print(f'{centrum = }')
print(f'{chorzy_rok = }')
print(f'{centrum.difference(chorzy_rok) = }')
print('to powienien byc zbior pusty ', centrum.difference(chorzy_rok).intersection(chorzy_rok))
print('to powienien byc podzbior osob z centrum ', centrum.difference(chorzy_rok).intersection(centrum))
```



Output:
```
kobiety z Krzyków, które były chore w ostatnim roku  {4544, 5436, 3254}

wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku  {2345, 3987}

centrum = {7648, 1234, 3987, 2356, 3476, 3254, 2345}

chorzy_rok = {4544, 8769, 1234, 3476, 3254, 3098, 5436, 3423}

centrum.difference(chorzy_rok) = {7648, 2345, 3987, 2356}

to powienien byc zbior pusty  set()

to powienien byc podzbior osob z centrum  {7648, 2345, 3987, 2356}


```



## Krotki



### Program krotki

Kod programu:
```python

lista = [1, 2, 3]

krotka = (1, 2, 3)

print('lista ', lista)
print('krotka ', krotka)

krotka2 = 10, 20, 30

print('krotka2 ', krotka2)

# x = lista[0]
# y = lista[1]
# z = lista[2]

x, y, z = krotka2
print('x ', x, ', y ', y, ', z ', z)

x, y, _ = krotka
print('x ', x, ', y ', y)

```



Output:
```
lista  [1, 2, 3]

krotka  (1, 2, 3)

krotka2  (10, 20, 30)

x  10 , y  20 , z  30

x  1 , y  2


```



## Dalej zdania zbiory



### Program zbiory_zadanie5

Kod programu:
```python
from functools import reduce

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345,  6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

wszystkie_zbiory = {'NFZ': NFZ, 'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}

def czy_pesel_ok(pesel: int) -> bool:
    return pesel >= 10**3 and pesel < 10**4

def przyjmuj_pesel():
    while True:
        i = input('Podaj pesel: ').strip()
        try:
            potencjalny_pesel = int(i)
            if not czy_pesel_ok(potencjalny_pesel):
                print('Pesel musi mieć 4 znaki')
                continue
            return potencjalny_pesel
        except ValueError:
            print('Proszę podać prawidłowy pesel')

zbior_wszystkich_zlych_peseli = {p for p in reduce(lambda a, b: a.union(b), wszystkie_zbiory.values()) if not czy_pesel_ok(p)}
print('zbior_wszystkich_zlych_peseli ', zbior_wszystkich_zlych_peseli)

pesel = przyjmuj_pesel()

if pesel % 2 == 0:
    print('podany pesel ', pesel, ' należy do kobiety')
else:
    print('podany pesel ', pesel, ' należy do mężczyzny')



for nazwa, zbior in wszystkie_zbiory.items():
    zbior_zlych_peseli = {p for p in zbior if not czy_pesel_ok(p)}
    if zbior_zlych_peseli:
        print('znaleziono złe pesele: ', zbior_zlych_peseli)
    if pesel in zbior:
        print('podany pesel ', pesel, ' wystepuje w zbiorze ', nazwa, ' ten zbiór to ', zbior)

```





### Program zbiory_zadanie6.py

Kod programu:
```python
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

wszystkie_zbiory = {'NFZ': NFZ, 'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}

pesel = int(input('Podaj pesel: '))

if pesel % 2 == 0:
    print('podany pesel ', pesel, ' należy do kobiety')
else:
    print('podany pesel ', pesel, ' należy do mężczyzny')


for nazwa, zbior in wszystkie_zbiory.items():
    if pesel in zbior:
        print('podany pesel ', pesel, ' wystepuje w zbiorze ', nazwa, ' ten zbiór to ', zbior)

```



Program lista rzeczy do zrobienia. Program ma oferować opcje:
 - Dodaj rzecz do zrobienia
 - Oznacz rzecz jako zrobioną
 - Pokaż rzeczy do zrobienia i zrobione
 - Usuń rzecz do zrobienia
 - Ustaw konkretną rzecz na początek
 - Wyjdź z programu




### Program zbiory_zadanie7

Kod programu:
```python
def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 6:
            return liczba
        print('To musi być liczba od 1 do 6')

lista = ['A', 'B', 'C', 'D']

del lista[2]

def petla_glowna_programu():
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            print('opcja 1')
        elif opcja == 2:
            print('opcja 2')
        elif opcja == 3:
            pass
        elif opcja == 4:
            pass
        elif opcja == 5:
            pass
        elif opcja == 6:
            return

petla_glowna_programu()
```





### Program zadanie8.py

Kod programu:
```python
from collections import defaultdict
from typing import List


def zlicz_slowa(lista_slow: List[str]):
    slownik_wystapien = defaultdict(int)
    for slowo in lista_slow:
        # if slowo not in slownik_wystapien:
        #     slownik_wystapien[slowo] = 0
        slownik_wystapien[slowo] = slownik_wystapien[slowo] + 1
    return slownik_wystapien

print(zlicz_slowa(['ala', 'ma', 'kota', 'ala']))
```



Output:
```
defaultdict(<class 'int'>, {'ala': 2, 'ma': 1, 'kota': 1})


```





### Program defultdict_przyklad

Kod programu:
```python
from collections import defaultdict

slownik = {}

# bład
# print(slownik['a'])

domyslny_slownik = defaultdict(int)
print('przed ', domyslny_slownik)
print(domyslny_slownik['a'])
print('po ', domyslny_slownik)

```



Output:
```
przed  defaultdict(<class 'int'>, {})

0

po  defaultdict(<class 'int'>, {'a': 0})


```





### Program slownik_zabezpieczenia

Kod programu:
```python
from collections import defaultdict

slownik = {}

print(slownik.get('a'))
print(slownik.get('a', 'wartosc gdy nie zjadziemy'))

domyslny_slownik = defaultdict(list)
print(domyslny_slownik['a'])

domyslny_slownik = defaultdict(lambda: 50)
print(domyslny_slownik['a'])
```



Output:
```
None

wartosc gdy nie zjadziemy

[]

50


```



## Dodatkowy materiał
Klasy na przykładzie zadania 7.



### Program zbiory_zadanie7_oop.py

Kod programu:
```python


def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 6:
            return liczba
        print('To musi być liczba od 1 do 6')

lista = ['A', 'B', 'C', 'D']

del lista[2]


def opcja_1(lista_rzeczy_do_zrobienia):
    lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))


def pokaz_rzeczy_do_zrobienia(lista_rzeczy_do_zrobienia, lista_rzeczy_zrobionych):
    print('Do zrobienia jest: ', lista_rzeczy_do_zrobienia)
    print('Zrobione jest: ', lista_rzeczy_zrobionych)


def petla_glowna_programu():
    lista_rzeczy_do_zrobienia = []
    lista_rzeczy_zrobionych = []
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            opcja_1(lista_rzeczy_do_zrobienia)
        elif opcja == 2:
            print('opcja 2')
        elif opcja == 3:
            pokaz_rzeczy_do_zrobienia(lista_rzeczy_do_zrobienia, lista_rzeczy_zrobionych)
        elif opcja == 4:
            pass
        elif opcja == 5:
            pass
        elif opcja == 6:
            return

petla_glowna_programu()
```





### Program zbiory_zadanie7_oop2.py

Kod programu:
```python


def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 6:
            return liczba
        print('To musi być liczba od 1 do 6')


class ListaRzeczyDoZrobienia:

    def __init__(self):
        self.lista_rzeczy_do_zrobienia = []
        self.lista_rzeczy_zrobionych = []

    def opcja_1(self):
        self.lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))

    def pokaz_rzeczy_do_zrobienia(self):
        print('Do zrobienia jest: ', self.lista_rzeczy_do_zrobienia)
        print('Zrobione jest: ', self.lista_rzeczy_zrobionych)

# def opcja_1(lista_rzeczy_do_zrobienia):
#     lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))
#
#
# def pokaz_rzeczy_do_zrobienia(lista_rzeczy_do_zrobienia, lista_rzeczy_zrobionych):
#     print('Do zrobienia jest: ', lista_rzeczy_do_zrobienia)
#     print('Zrobione jest: ', lista_rzeczy_zrobionych)


def petla_glowna_programu():
    # lista_rzeczy_do_zrobienia = []
    # lista_rzeczy_zrobionych = []
    instancje_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia()
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            # opcja_1(lista_rzeczy_do_zrobienia)
            instancje_rzeczy_do_zrobienia.opcja_1()
        elif opcja == 2:
            print('opcja 2')
        elif opcja == 3:
            # pokaz_rzeczy_do_zrobienia(lista_rzeczy_do_zrobienia, lista_rzeczy_zrobionych)
            instancje_rzeczy_do_zrobienia.pokaz_rzeczy_do_zrobienia()
        elif opcja == 4:
            pass
        elif opcja == 5:
            pass
        elif opcja == 6:
            return

petla_glowna_programu()
```





### Program zbiory_zadanie7_oop3.py

Kod programu:
```python


def wypisz_menu():
    print()
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 6:
            return liczba
        print('To musi być liczba od 1 do 6')


class ListaRzeczyDoZrobienia:

    def __init__(self):
        self.lista_rzeczy_do_zrobienia = []
        self.lista_rzeczy_zrobionych = []

    def dodaj_rzecz_do_zrobienia(self):
        self.lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))

    def oznacz_rzecz_jako_zrobiona(self):
        indeks_zrobionej_rzeczy = self._pobierz_indeks_rzeczy_do_zrobienia()
        self.lista_rzeczy_zrobionych.append(self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy])
        del self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]

    def pokaz_rzeczy_do_zrobienia(self):
        print()
        print('Do zrobienia jest: ')
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_do_zrobienia):
            print(f'\t\t{indeks} [ ] {rzeczy_do_zrobienia}')
        print()
        print('Zrobione jest: ')
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_zrobionych):
            print(f'\t\t{indeks} [x] {rzeczy_do_zrobienia}')

    def usun_rzecz_do_zrobienia(self):
        indeks_rzeczy_do_usuniecia = self._pobierz_indeks_rzeczy_do_zrobienia()
        del self.lista_rzeczy_do_zrobienia[indeks_rzeczy_do_usuniecia]

    def ustaw_rzecz_na_poczatek(self):
        indeks_zrobionej_rzeczy = self._pobierz_indeks_rzeczy_do_zrobienia()
        element_na_poczatek = self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]
        del self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]
        self.lista_rzeczy_do_zrobienia.insert(0, element_na_poczatek)

    def _pobierz_indeks_rzeczy_do_zrobienia(self):
        while True:
            print()
            for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_do_zrobienia):
                print(f'\t\t{indeks} [ ] {rzeczy_do_zrobienia}')
            print()
            try:
                indeks_rzeczy = int(input('Który indeks: '))
            except ValueError:
                print('to musi być liczba')
                continue
            if indeks_rzeczy >= 0 and indeks_rzeczy < len(self.lista_rzeczy_do_zrobienia):
                return indeks_rzeczy
            else:
                print('podana liczba jest spoza przedzialu')



def petla_glowna_programu():
    instancje_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia()
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            instancje_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            instancje_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            instancje_rzeczy_do_zrobienia.pokaz_rzeczy_do_zrobienia()
        elif opcja == 4:
            instancje_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            instancje_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            return

petla_glowna_programu()
```



Dodaj opcje:
 - 7. Ocznacz zrobioną rzecz jako niezrobioną



### Program zbiory_zadanie7_oop3_zadanie.py

Kod programu:
```python


def wypisz_menu():
    print()
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')
    print('7. Ocznacz zrobioną rzecz jako niezrobioną')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-7): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 7:
            return liczba
        print('To musi być liczba od 1 do 6')


class ListaRzeczyDoZrobienia:

    def __init__(self):
        self.lista_rzeczy_do_zrobienia = []
        self.lista_rzeczy_zrobionych = []

    def dodaj_rzecz_do_zrobienia(self):
        self.lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))

    def oznacz_rzecz_jako_zrobiona(self):
        indeks_zrobionej_rzeczy = self._pobierz_indeks()
        self.lista_rzeczy_zrobionych.append(self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy])
        del self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]

    def pokaz_rzeczy_do_zrobienia(self):
        print()
        print('Do zrobienia jest: ')
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_do_zrobienia):
            print(f'\t\t{indeks} [ ] {rzeczy_do_zrobienia}')
        print()
        print('Zrobione jest: ')
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_zrobionych):
            print(f'\t\t{indeks} [x] {rzeczy_do_zrobienia}')

    def usun_rzecz_do_zrobienia(self):
        indeks_rzeczy_do_usuniecia = self._pobierz_indeks()
        del self.lista_rzeczy_do_zrobienia[indeks_rzeczy_do_usuniecia]

    def ustaw_rzecz_na_poczatek(self):
        indeks_zrobionej_rzeczy = self._pobierz_indeks()
        element_na_poczatek = self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]
        del self.lista_rzeczy_do_zrobienia[indeks_zrobionej_rzeczy]
        self.lista_rzeczy_do_zrobienia.insert(0, element_na_poczatek)

    def _pobierz_indeks(self, lista=None):
        if lista is None:
            lista = self.lista_rzeczy_do_zrobienia
        while True:
            print()
            for indeks, rzeczy_do_zrobienia in enumerate(lista):
                print(f'\t\t{indeks} [ ] {rzeczy_do_zrobienia}')
            print()
            try:
                indeks_rzeczy = int(input('Który indeks: '))
            except ValueError:
                print('to musi być liczba')
                continue
            if indeks_rzeczy >= 0 and indeks_rzeczy < len(lista):
                return indeks_rzeczy
            else:
                print('podana liczba jest spoza przedzialu')

    def oznacz_rzecz_zrobiona_jako_niezrobiona(self):
        indeks_zrobionej_rzeczy = self._pobierz_indeks(self.lista_rzeczy_zrobionych)
        self.lista_rzeczy_do_zrobienia.append(self.lista_rzeczy_zrobionych[indeks_zrobionej_rzeczy])
        del self.lista_rzeczy_zrobionych[indeks_zrobionej_rzeczy]



def petla_glowna_programu():
    instancje_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia()
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            instancje_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            instancje_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            instancje_rzeczy_do_zrobienia.pokaz_rzeczy_do_zrobienia()
        elif opcja == 4:
            instancje_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            instancje_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            return
        elif opcja == 7:
            instancje_rzeczy_do_zrobienia.oznacz_rzecz_zrobiona_jako_niezrobiona()


petla_glowna_programu()
```


