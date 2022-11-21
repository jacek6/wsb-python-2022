# Zajęcia 19.11.2022
Prowadzone dla grupy 1.
## Powtórka

Dana jest lista zarobków brutto:
````
zarobki = ['5001PLN', '972EUR', '1043USD', '1897PLN', '693EUR', '790USD’]
````


Napisz program, który:
 - przeliczy zarobki na PLN,
 - obliczy należny podatek (10% powyżej 3000 zł i 20% powyżej 5000 zł),
 - zapisze w nowej liście zarobki netto w PLN,
 - wypisze odpowiednie komunikaty.




### Program powtorka.py

Kod programu:
```python

zarobki = ['5001PLN', '972EUR', '1043USD', '1897PLN', '693EUR', '790USD']

zarobki_netto = []

for z in zarobki:
    kwota = float(z[:-3])
    waluta = z[-3:]
    print(kwota, waluta)

    if waluta == 'PLN':
        kwota_w_pln = kwota
    elif waluta == 'EUR':
        kwota_w_pln = kwota * 4.71
    elif waluta == 'USD':
        kwota_w_pln = kwota * 4.55
    else:
        print(f'BŁĄD nie znana waluta: {waluta}')
    print('Zarobki brutto w PLN ', kwota_w_pln)

    podatek = 0
    if kwota_w_pln > 3000:
        podatek = kwota_w_pln * 0.1
    if kwota_w_pln > 5000:
        podatek = kwota_w_pln * 0.2
    print('podatek dla kwoty PLN ', kwota_w_pln, ' wynosi ', podatek)
    netto = kwota_w_pln - podatek

    zarobki_netto.append(netto)

print('zarobki_w_pln = ', zarobki_netto)

```



Output:
```
5001.0 PLN
Zarobki brutto w PLN  5001.0
podatek dla kwoty PLN  5001.0  wynosi  1000.2
972.0 EUR
Zarobki brutto w PLN  4578.12
podatek dla kwoty PLN  4578.12  wynosi  457.812
1043.0 USD
Zarobki brutto w PLN  4745.65
podatek dla kwoty PLN  4745.65  wynosi  474.565
1897.0 PLN
Zarobki brutto w PLN  1897.0
podatek dla kwoty PLN  1897.0  wynosi  0
693.0 EUR
Zarobki brutto w PLN  3264.03
podatek dla kwoty PLN  3264.03  wynosi  326.403
790.0 USD
Zarobki brutto w PLN  3594.5
podatek dla kwoty PLN  3594.5  wynosi  359.45000000000005
zarobki_w_pln =  [4000.8, 4120.308, 4271.085, 1897.0, 2937.6270000000004, 3235.05]

```




## Pomysły na zadania
 - słownik do przeliczania kuru walut w powtórce
 - ogólnie program z powtórki ładniej napisać z funkcjami

# Pętla while



### Program while_przyklad1

Kod programu:
```python
lista = []

while len(lista) < 3:
    lista.append('element')
# if len(lista) < 3:
#     lista.append('element')
# if len(lista) < 3:
#     lista.append('element')
# if len(lista) < 3:
#     lista.append('element')
# if len(lista) < 3:
#     lista.append('element')
# if len(lista) < 3:
#     lista.append('element')
# if len(lista) < 3:
#     lista.append('element')

print(lista)
```



Output:
```
['element', 'element', 'element']

```






### Program while_true_przyklad1

Kod programu:
```python
lista = []

while True:
    lista.append('element')
    if len(lista) >= 3:
        break

print(lista)
```



Output:
```
['element', 'element', 'element']

```



Napisz program, który przyjmuje numer PESEL i weryfikuje jego poprawność.

Program pyta tak długo, aż zostanie wprowadzony poprawny PESEL bądź użytkownik wyjdzie z programu.

Przyjmij, że:
PESEL jest czterocyfrowy, 
w poprawnym numerze PESEL suma cyfr jest podzielna przez 3 lub przez 4.





### Program while_zadanie_przylad1

Kod programu:
```python

while True:
    pesel = input('Podaj PESEL: ')

    suma_cyfr = 0
    for znak_pesel in pesel:
        suma_cyfr += int(znak_pesel)
    if suma_cyfr % 3 == 0 or suma_cyfr % 4 == 0:
        print('pesel prawidłowy')
        break
    print('PESEL nie jest poprawny, proszę podać go jeszcze raz')
```



Napisz program, który w ustalonej posortowanej liście wyszukuje indeks konkretnego elementu.

	lista = [-88, -3, 11, 23, 56, 78, 98, 154, 176, 198, 275, 375, 416, 524, 564, 627, 738, 873, 924]

Wejście:
Wartość elementu do znalezienia
Wyjście:
Indeks na którym indeksie listy jest ten element, lub jeśli go nie ma informacja o tym na jakim indeksie by się znajdował
Wymagania:
Użyj wyszukiwania binarnego z użyciem pętli while





### Program while_wyszukiwanie_binarne1

Kod programu:
```python
lista = [-88, -3, 11, 23, 56, 78, 98, 154, 176, 198, 275, 375, 416, 524, 564, 627, 738, 873, 924]

element_do_zalezienia = 0

l = 0
r = len(lista) - 1
while l + 1 < r:
    print('Szukam w liście: ', lista[l:r])

    c = (l + r) // 2

    if lista[c] == element_do_zalezienia:
        print('Znaleziono element n indeksie ', c)
        break
    if element_do_zalezienia < lista[c]:
        r = c
    else:
        l = c

if lista[c] != element_do_zalezienia:
    print("Element miałby indeks ", c)
```



Output:
```
Szukam w liście:  [-88, -3, 11, 23, 56, 78, 98, 154, 176, 198, 275, 375, 416, 524, 564, 627, 738, 873]
Szukam w liście:  [-88, -3, 11, 23, 56, 78, 98, 154, 176]
Szukam w liście:  [-88, -3, 11, 23]
Szukam w liście:  [-88, -3]
Element miałby indeks  1

```



Napisz program, który poczeka aż bęzie pełna minuta



### Program while_pelna_minuta

Kod programu:
```python
import datetime
import time

while datetime.datetime.now().second < 50:
    print('Czekam na pełną mitutę')
    time.sleep(2)

print('Pełna minuta jest zaraz...')
```



Output:
```
Czekam na pełną mitutę
Czekam na pełną mitutę
Czekam na pełną mitutę
Czekam na pełną mitutę
Czekam na pełną mitutę
Pełna minuta jest zaraz...

```




Napisz program, który poczeka aż powstanie określony plik



### Program while_zadanie_istanieje_plik

Kod programu:
```python
import os
import time

while not os.path.exists('plik.txt'):
    print('plik nie instnieje')
    time.sleep(2)

print('Plik instnieje')
```



Output:
```
Plik instnieje

```



Przykład działania while-elase



### Program while_else

Kod programu:
```python
odp = input('Podaj liczbe parzystą lub Q żeby wyjść: ')

while odp != 'Q':
    if int(odp) % 2 == 0:
        print('jest to liczba parzysta')
    else:
        print('nie jest to liczba parzysta - BŁĄD')
        break
    odp = input('Podaj liczbe parzystą lub Q żeby wyjść: ')
else:
    print('wykonuję else')
    print('prawidłowe zakończenie programu bez błędu')
```



## Funkcje



### Program funkcja_przyklad1

Kod programu:
```python

def moja_funkcja_powiekszajaca(liczba):
    print('Wykonuje funkcje powiększająca z argumnetem: ', liczba)
    return liczba + 1

print(moja_funkcja_powiekszajaca(4))

argumnet_funkcji = 1
print(moja_funkcja_powiekszajaca(argumnet_funkcji))

wynik_funkcji = moja_funkcja_powiekszajaca(8)

print('wynik_funkcji = ', wynik_funkcji)
```



Output:
```
Wykonuje funkcje powiększająca z argumnetem:  4
5
Wykonuje funkcje powiększająca z argumnetem:  1
2
Wykonuje funkcje powiększająca z argumnetem:  8
wynik_funkcji =  9

```





### Program funkcja_przyklad2

Kod programu:
```python

def oblicz_pole_trojkata(dlugosc_podstawy, wysokosc):
    return dlugosc_podstawy * wysokosc / 2

def odczytaj_liste_stringow(nazwa_pliku):
    wynik = []
    with open(nazwa_pliku, 'r') as fp:
        for linia_w_pliku in fp:
            wynik.append(linia_w_pliku)
    return wynik

print('Pole trojkta ', oblicz_pole_trojkata(4, 5))

print('Odczytanie pliku ', odczytaj_liste_stringow('plik.txt'))
print('Ładne odczytanie pliku')
for linia in odczytaj_liste_stringow('plik.txt'):
    print('Linia zwrócona z funkcji: ', linia)


with open('plik.txt', 'r') as wskaznikiem_do_pliku:
    for linia in wskaznikiem_do_pliku:
        print("Linia odczytana z pliku ", linia)

```



Output:
```
Pole trojkta  10.0
Odczytanie pliku  ['linia 1\n', 'linia 2 abc\n', 'xyz\n', 'linia 4']
Ładne odczytanie pliku
Linia zwrócona z funkcji:  linia 1

Linia zwrócona z funkcji:  linia 2 abc

Linia zwrócona z funkcji:  xyz

Linia zwrócona z funkcji:  linia 4
Linia odczytana z pliku  linia 1

Linia odczytana z pliku  linia 2 abc

Linia odczytana z pliku  xyz

Linia odczytana z pliku  linia 4

```





### Program funkcja_przyklad3

Kod programu:
```python
from typing import List


def odczytaj_liste_stringow(nazwa_pliku: str) -> List[str]:
    wynik = []
    with open(nazwa_pliku, 'r') as fp:
        for linia_w_pliku in fp:
            wynik.append(linia_w_pliku)
    return wynik

# def zapisz_do_pliku_linia_obok_lini(nazwa_pliku_do_zapisania: str, lista_lini: List[str]):
def zapisz_do_pliku_linia_obok_lini(nazwa_pliku_do_zapisania = 'plik_do_zapisania.txt', lista_lini=['domyslan linia']):
    with open(nazwa_pliku_do_zapisania, 'w') as fp:
        for lini in lista_lini:
            fp.write(lini.rstrip())
            fp.write(' ')

print('Odczytanie pliku ', odczytaj_liste_stringow('plik.txt'))
print('Ładne odczytanie pliku')
for linia in odczytaj_liste_stringow('plik.txt'):
    print('Linia zwrócona z funkcji: ', linia)

zapisz_do_pliku_linia_obok_lini('plik_wynikowy.txt', odczytaj_liste_stringow('plik.txt'))
zapisz_do_pliku_linia_obok_lini('abc.txt', ['a', 'b', 'cd'])

zapisz_do_pliku_linia_obok_lini()
```



Output:
```
Odczytanie pliku  ['linia 1\n', 'linia 2 abc\n', 'xyz\n', 'linia 4']
Ładne odczytanie pliku
Linia zwrócona z funkcji:  linia 1

Linia zwrócona z funkcji:  linia 2 abc

Linia zwrócona z funkcji:  xyz

Linia zwrócona z funkcji:  linia 4

```





### Program funkcja_przylad_wartosci_domyslne

Kod programu:
```python

def wypisz(a, b=20, c=30):
    print('podano: ', a, b, c)

# błąd:
# def wypisz2(x, a=10, b, c):
#     print('podano: ', a, b, c)


wypisz(1, 2, 3)

wypisz(1, 2)

wypisz(1)

def wypisz_smart(a, b=None):
    if b:
        print('podano ', a, b)
    else:
        print('podano ', a)

wypisz_smart(100, 200)
wypisz_smart(100)

```



Output:
```
podano:  1 2 3
podano:  1 2 30
podano:  1 20 30
podano  100 200
podano  100

```



Napisz funkcję, która przyjmuje metraż, wiek oraz typ budynku i zwraca informację, czy można w nim mieszkać.




### Program funkcje_zadanie1

Kod programu:
```python

def czy_da_sie_mieszkac(metraz: float, wiek: float, typ_budunku: str) -> bool:
    if metraz < 20:
        return False
    if wiek > 100:
        return False
    if typ_budunku == 'rudera':
        return False
    return True

def ladne_wypisanie_czy_da_sie_mieszkac(metraz: float, wiek: float, typ_budunku: str):
    if czy_da_sie_mieszkac(metraz, wiek, typ_budunku):
        print('Stwierdzono, że da się mieszkać dla, metraz ', metraz, ', wiek ', wiek, ', typ_budunku ', typ_budunku)
    else:
        print('Stwierdzono, że NIE da się mieszkać dla, metraz ', metraz, ', wiek ', wiek, ', typ_budunku ', typ_budunku)

ladne_wypisanie_czy_da_sie_mieszkac(1, 6, 'blok')
ladne_wypisanie_czy_da_sie_mieszkac(100, 6, 'blok')

ladne_wypisanie_czy_da_sie_mieszkac(metraz=120, wiek=9, typ_budunku='blok')
ladne_wypisanie_czy_da_sie_mieszkac(metraz=120, wiek=9, typ_budunku='rudera')
```



Output:
```
Stwierdzono, że NIE da się mieszkać dla, metraz  1 , wiek  6 , typ_budunku  blok
Stwierdzono, że da się mieszkać dla, metraz  100 , wiek  6 , typ_budunku  blok
Stwierdzono, że da się mieszkać dla, metraz  120 , wiek  9 , typ_budunku  blok
Stwierdzono, że NIE da się mieszkać dla, metraz  120 , wiek  9 , typ_budunku  rudera

```



Napisz funkcje, która przyjmuje dane użytkownika i zwraca informację, czy użytkownik może dalej używać programu.




### Program funkcje_zadanie2

Kod programu:
```python

def czy_mozna_uzywac_programu(nazwa_uztkownika: str, nr_licencji) -> bool:
    if not nazwa_uztkownika.endswith('@wsb.pl'):
        return False
    return nr_licencji % 3 == 0
    # if nr_licencji % 3 == 0:
    #     return True
    # else:
    #     return False

print(f"{czy_mozna_uzywac_programu('jacek@gmail.com', 3) = }")
print(f"{czy_mozna_uzywac_programu('jacek@wsb.pl', 3) = }")
print(f"{czy_mozna_uzywac_programu('jacek@wsb.pl', 31) = }")
```



Output:
```
czy_mozna_uzywac_programu('jacek@gmail.com', 3) = False
czy_mozna_uzywac_programu('jacek@wsb.pl', 3) = True
czy_mozna_uzywac_programu('jacek@wsb.pl', 31) = False

```



Napisz funkcje która oczekuje aż użytkownik poda liczbę z zadanego zakresu. Użyj tej funkcji w programie, który pyta o datę urodzenia i oblicza ile ktoś ma lat, miesięcy, dni.




### Program funkcje_zadanie3

Kod programu:
```python
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
```



Napisz funkcje która oczekuje aż użytkownik zgodzi się na warunki działania programu, jeśli odp użytkownika jest „tak” to się zgodził i program ma działać dalej. Jeśli użytkownik odp „nie” program ma się zakończyć. Każda inna odp ma powodować powtórzenie pytania. Dodaj tą funkcję do poprzedniego programu.



### Program funkcje_zadanie4

Kod programu:
```python
import sys


def wymus_zgode_na_warunki():
    while True:
        odp = input('Czy zgadzasz sie na warunki działania programu (tak/nie/q wyjśćie): ')
        if odp == 'tak':
            return
        if odp == 'nie':
            print('Zgodna na warunki jest wymagana do dalszego działania')
            continue
        print('sprawdzam czy trzeba wyjść')
        if odp == 'q':
            sys.exit(0)

wymus_zgode_na_warunki()
print('program leci dalej')
```





### Program slownik_przyklad1

Kod programu:
```python
kursy_walut_do_PLN = {'EURO' : 4.6, 'USD' : 4.5, 'BTC' : 1000000}

print(kursy_walut_do_PLN['EURO'])

x = kursy_walut_do_PLN['USD']
print('x = ', x)

suma = kursy_walut_do_PLN['EURO'] + kursy_walut_do_PLN['USD']
print('suma = ', suma)

zmienna = 'BTC'
print(kursy_walut_do_PLN[zmienna] )
```



Output:
```
4.6
x =  4.5
suma =  9.1
1000000

```





### Program slownik_przyklad2

Kod programu:
```python
kursy_walut_do_PLN = {'PLN': 1, 'EUR' : 4.6, 'USD' : 4.5, 'BTC' : 1000000}

zarobki = ['5001PLN', '972EUR', '1043USD', '1897PLN', '693EUR', '790USD']

for z in zarobki:
    kwota = float(z[:-3])
    waluta = z[-3:]
    print(kwota, waluta)

    kwota_w_pln = kwota * kursy_walut_do_PLN[waluta]

    print(z, ' -> ', kwota_w_pln)

```



Output:
```
5001.0 PLN
5001PLN  ->  5001.0
972.0 EUR
972EUR  ->  4471.2
1043.0 USD
1043USD  ->  4693.5
1897.0 PLN
1897PLN  ->  1897.0
693.0 EUR
693EUR  ->  3187.7999999999997
790.0 USD
790USD  ->  3555.0

```



PRzykład sprawdzenia czy cos jest słowniku.



### Program slownik_przyklad3

Kod programu:
```python
kursy_walut_do_PLN = {'PLN': 1, 'EUR' : 4.6, 'USD' : 4.5, 'BTC' : 1000000}

zarobki = ['5001PLN', '972EUR', '1043USD', '1897CHF', '693EUR', '790USD']

for z in zarobki:
    kwota = float(z[:-3])
    waluta = z[-3:]
    print(kwota, waluta)

    if waluta in kursy_walut_do_PLN:
        kwota_w_pln = kwota * kursy_walut_do_PLN[waluta]
    else:
        kwota_w_pln = '?'

    print(z, ' -> ', kwota_w_pln)

```



Output:
```
5001.0 PLN
5001PLN  ->  5001.0
972.0 EUR
972EUR  ->  4471.2
1043.0 USD
1043USD  ->  4693.5
1897.0 CHF
1897CHF  ->  ?
693.0 EUR
693EUR  ->  3187.7999999999997
790.0 USD
790USD  ->  3555.0

```




Program pozwala zmienić hasło użytkownika – pobiera hasło ze słownika i porównuje.



### Program slownik_zadanie1

Kod programu:
```python
hasla_uzytkownikow = {'jacek': 'abc',
                      'ania': '123'}

def zmien_haslo(uzytkownik, aktualne_haslo, nowe_haslo):
    if uzytkownik not in hasla_uzytkownikow:
        print('Nie znany użytkownik ', uzytkownik)
        return
    if hasla_uzytkownikow[uzytkownik] != aktualne_haslo:
        print('Hasło nie pasuje')
        return
    hasla_uzytkownikow[uzytkownik] = nowe_haslo

def spr_haslo(uzytkownik, haslo) -> bool:
    if uzytkownik not in hasla_uzytkownikow:
        return False
    return hasla_uzytkownikow[uzytkownik] == haslo

while True:
    print('1. zmien haslo')
    print('2. spr haslo')
    print('3. pokaż hasła')
    print('4. wyjście')

    odp = input('co chcesz zrobić (1/2)?: ')
    if odp == '1':
        zmien_haslo(input('Podaj użytkownika: '), input('Podaj aktualne hasło: '), input('Podaj nowe hasło: '))
    elif odp == '2':
        print(spr_haslo(input('Podaj użytkownika: '), input('Podaj aktualne hasło: ')))
    elif odp == '3':
        print(hasla_uzytkownikow)
    elif odp == '4':
        break

```





### Program slownik_zadanie2

Kod programu:
```python
from typing import List


def zlicz_slowa(lista_slow: List[str]):
    slownik_wystapien = {}
    for slowo in lista_slow:
        if slowo in slownik_wystapien:
            slownik_wystapien[slowo] = slownik_wystapien[slowo] + 1
        else:
            slownik_wystapien[slowo] = 1
    return slownik_wystapien

print(zlicz_slowa(['ala', 'ma', 'kota', 'ala']))
```



Output:
```
{'ala': 2, 'ma': 1, 'kota': 1}

```





### Program slownik_zadanie2_czytanie_pliku

Kod programu:
```python
from typing import List


def zlicz_slowa(lista_slow: List[str]):
    slownik_wystapien = {}
    for slowo in lista_slow:
        if slowo in slownik_wystapien:
            slownik_wystapien[slowo] = slownik_wystapien[slowo] + 1
        else:
            slownik_wystapien[slowo] = 1
    return slownik_wystapien

def wez_slowa_z_pliku(nazwa_pliku: str) ->  List[str]:
    lista_wszystkich_slow = []
    with open(nazwa_pliku, 'r', encoding='utf-8') as fp:
        for linia in fp:
            # slowa = linia.split(' ')
            # lista_wszystkich_slow += slowa
            for slowo in linia.split(' '):
                slowo = slowo.rstrip()
                if slowo:
                    lista_wszystkich_slow.append(slowo.lower())
    return lista_wszystkich_slow

print(zlicz_slowa(['ala', 'ma', 'kota', 'ala']))
wystapienia_slow = zlicz_slowa(wez_slowa_z_pliku('plik_do_liczenia_slow.txt'))
print(wystapienia_slow)

max_wartosc = 0
max_klucz = ''
for klucz, wartosc in wystapienia_slow.items():
    print('klucz ', klucz, ' ma wartosc ', wartosc)
    if wartosc > max_wartosc:
        max_wartosc = wartosc
        max_klucz = klucz
print(max_klucz, ' wystpuje ', max_wartosc, ' razy')


liste_par_klucz_wartosc = sorted(wystapienia_slow.items(), key=lambda x: x[1], reverse=True)

print(liste_par_klucz_wartosc)
print(liste_par_klucz_wartosc[0])
print(liste_par_klucz_wartosc[1])
print(liste_par_klucz_wartosc[2])

```



Output:
```
{'ala': 2, 'ma': 1, 'kota': 1}
{'opis': 2, 'konstrukcji': 1, 'ogólny': 1, 'sylwetka': 1, 'okrętów': 7, 'typu': 14, 'nagara': 3, 'sprzed': 1, 'wojennej': 2, 'przebudowy': 1, '(poniżej': 1, 'schemat': 2, 'kątów': 1, 'ostrzału': 1, 'artylerii': 1, 'i': 37, 'opancerzenia)': 1, 'kadłub': 4, 'krążowników': 4, 'miał': 3, '162,15': 1, 'm': 7, 'długości': 4, 'całkowitej,': 1, 'zaś': 8, 'na': 65, 'linii': 1, 'wodnej': 1, 'długość': 3, 'wynosiła': 5, '156,65': 1, 'm[2].': 1, 'szerokość': 1, 'jednostki': 10, '14,17': 1, 'm,': 2, 'natomiast': 4, 'jej': 1, 'zanurzenie': 1, 'wynosiło': 2, '4,85': 1, 'm[3][2].': 1, 'wyporność': 2, 'standardowa': 2, '5170': 1, 'ts,': 1, 'normalna': 1, '5690': 1, 'ts.': 1, 'w': 128, 'wyniku': 5, 'modernizacji': 1, 'z': 33, '1944': 9, 'roku': 44, 'wzrosła': 1, 'do': 26, '6050': 1, 'ts[4].': 1, 'zewnętrzny': 1, 'wykonano': 1, 'płyt': 2, 'stalowych': 1, 'o': 16, 'grubości': 6, '19': 1, '25,4': 2, 'mm,': 6, 'a': 11, 'płyty': 2, 'stanowiące': 1, 'wewnętrzne': 1, 'elementy': 1, 'kadłuba': 4, 'miały': 7, 'grubość': 2, 'od': 15, '6,4': 1, '12,7': 1, 'mm[5].': 1, 'grubsze': 1, 'znajdowały': 6, 'się': 28, 'kluczowych': 1, 'dla': 10, 'żywotności': 1, 'okrętu': 7, 'miejscach[5].': 1, 'okręty': 12, 'trzy': 3, 'pokłady:': 1, 'pokład': 7, 'główny,': 1, 'ciągnący': 1, 'przez': 11, 'całą': 1, 'jednostki,': 1, 'drugi': 3, '–': 4, 'znajdujący': 1, 'przed': 4, 'przedziałem': 2, 'kotłowni': 5, 'części': 5, 'dziobowej': 3, 'oraz': 35, 'za': 9, 'maszynowni': 1, 'rufowej[5].': 1, 'poniżej': 1, 'znajdował': 5, 'ostatni': 2, 'pełniący': 1, 'funkcję': 6, 'ładowni[5].': 1, 'śródokręcie': 1, 'jednostek': 2, 'było': 6, 'podwyższone': 1, 'przykryte': 1, 'pokładem': 4, 'łodziowym[5].': 1, 'śródokręciu': 2, 'ulokowano': 5, 'kabiny': 2, 'załogi,': 1, 'kambuz,': 1, 'instalacje': 1, 'sanitariatu': 1, 'magazyny.': 1, 'nadbudówce': 2, 'rufowej': 1, 'oficerów,': 1, 'umywalnie': 1, 'dalsze': 1, 'pomieszczenia': 4, 'magazynowe[5].': 1, 'załogi': 1, 'pokładzie': 2, 'głównym': 1, 'kotłowniami': 1, 'śródokręciu,': 2, 'pod': 9, 'łodziowym.': 1, 'podoficerowie': 1, 'zajmowali': 1, 'miejsca': 1, 'kabinami': 1, 'oficerskimi[6].': 1, 'znajdowała': 3, 'także': 2, 'wysoka': 1, 'dziobówka.': 1, 'składała': 1, 'czterech': 3, 'poziomów,': 1, 'gdzie': 6, 'pierwszym': 1, 'nich': 1, 'kabinę': 2, 'radiową,': 1, 'nad': 1, 'którą': 2, 'znajdowało': 2, 'pomieszczenie': 3, 'nakresowe': 1, 'operacyjne[7].': 1, 'wyżej': 1, 'kompasowy,': 1, 'którym': 1, 'oprócz': 3, 'kompasów': 1, 'dalmierze,': 1, 'lornety': 2, 'dalocelownik[7].': 1, 'nadbudówki,': 1, 'tuż': 1, 'kompasowym': 1, 'stanowisko': 3, 'dowodzenia[7].': 1, 'początkowo': 2, 'hangar': 1, 'wodnosamolotu,': 1, 'jednak': 2, 'podczas': 12, 'modernizacji,': 1, 'która': 1, 'zależności': 1, 'odbyła': 1, 'latach': 8, '1931–1934,': 2, 'został': 9, 'on': 2, 'zlikwidowany': 1, 'jego': 2, 'miejsce': 5, 'utworzono': 1, 'łączności,': 1, 'sztabu': 1, 'dowództwa': 1, 'flotylli': 2, 'powiększono': 1, 'centrum': 1, 'bojowe[6].': 1, 'załoga': 2, 'liczyła': 1, 'bazowo': 1, '450': 1, 'osób,': 2, 'tym': 6, '37': 1, 'oficerów.': 1, 'przypadku': 3, 'jeśli': 1, 'okręt': 39, 'pełnił': 5, 'flagowego,': 1, 'zaokrętowanych': 1, 'nim': 1, 'dodatkowych': 1, '27': 3, '5': 3, 'oficerów[6].': 1, 'opancerzenie': 2, 'zastosowany': 1, 'układ': 3, 'opancerzenia': 1, 'był': 4, 'praktycznie': 2, 'taki': 1, 'sam': 1, 'jak': 2, 'projektu': 1, 'kuma[2].': 1, 'pas': 2, 'pancerny': 1, '63,5': 1, 'łączący': 1, 'górnym,': 1, '73,17': 1, 'wysokości': 1, '4,87': 1, 'czego': 1, '0,84': 1, 'wodą[2].': 1, 'rozwiązanie': 1, 'to': 5, 'zapewniało': 1, 'ochronę': 1, 'ostrzałem': 2, 'dział': 8, 'kalibru': 8, '102': 1, 'mm.': 3, 'ten': 2, 'po': 13, 'obu': 1, 'stronach': 1, 'burt': 1, 'chronił': 1, 'maszynowni.': 1, 'wykonany': 1, 'ze': 2, 'stali': 1, 'wysokiej': 1, 'odporności': 1, 'rozciąganie': 1, 'składał': 1, 'dwóch': 5, 'warstw': 1, 'pancernych:': 1, 'warstwy': 1, 'zewnętrznej': 1, 'liczącej': 1, '38,1': 1, 'mm': 18, 'wewnętrznej,': 1, 'której': 2, 'mm[2].': 4, 'główny': 1, 'pokryto': 1, 'płytami': 2, 'pancernymi': 2, '28,5': 1, 'zamontowane': 3, 'wcześniej': 2, 'główne': 1, 'działa': 7, 'kal.': 16, '140': 4, 'osłonięto': 1, 'maskami': 1, '10': 5, 'komory': 1, 'amunicyjne': 1, 'głównych': 3, 'zostały': 2, 'opancerzone': 1, '32': 1, 'podajników': 1, 'amunicyjnych': 1, '16': 5, 'napędowy': 2, 'napędzane': 2, 'były': 9, 'pośrednictwem': 4, 'zespołów': 1, 'turbin': 2, 'parowych': 1, 'parsonsa,': 1, 'których': 1, 'skład': 2, 'wchodziła': 1, 'turbina': 2, 'wysokociśnieniowa': 1, 'gihon': 1, 'reakcyjna': 1, 'niskociśnieniowa': 1, 'mitsubishi-parsons[5].': 1, 'każdy': 1, 'zespół': 2, 'własnej': 1, 'przekładni': 1, 'redukcyjnej': 1, 'napędzał': 1, 'swoją': 2, 'linię': 1, 'wału': 1, 'napędowego,': 1, 'zakończoną': 1, 'pojedynczą,': 1, 'trójpłatową': 1, 'śrubą': 1, 'napędową[5].': 1, 'turbiny': 1, 'zasilane': 1, 'dwunastu': 1, 'kotłów': 1, 'opalanych': 1, 'paliwem': 4, 'płynnym[a]': 1, 'węglem[5].': 1, 'cztery': 4, 'kotłowni,': 1, 'pierwszej': 1, 'strony': 1, 'dziobu': 1, 'dwa': 12, 'małe': 1, 'kotły': 5, 'opalane': 4, 'olejowym': 1, 'węglem,': 1, 'drugiej': 1, 'ropą[5].': 1, 'trzeciej': 2, 'zajmowane': 1, 'ropę,': 1, 'ostatniej,': 1, 'czwartej': 1, 'również': 1, 'ciekłym[5].': 1, 'generowały': 2, 'one': 3, 'parę': 1, 'ciśnieniu': 1, 'wynoszącym': 1, '18,3': 1, 'kgf/cm²[5].': 1, 'zabierały': 2, 'zapas': 5, 'paliwa': 1, 'płynnego': 1, 'masie': 3, '1284': 1, 'ton': 2, '350': 1, 'węgla[5].': 1, 'węglem': 1, 'zmodernizowane': 1, 'tego': 5, 'czasu': 1, 'opalano': 1, 'je': 3, 'wyłącznie': 1, 'płynnym.': 1, 'modernizację': 2, 'siłowni': 1, 'poszczególnych': 1, 'okrętach': 2, 'przeprowadzono': 1, '1934–1938[6].': 1, 'spaliny': 1, 'odprowadzane': 1, 'trzech': 2, 'kominów': 1, 'śródokręciu[7].': 1, 'generował': 1, 'maksymalną': 3, 'moc': 1, 'wynoszącą': 2, '90': 1, '000': 2, 'km,': 1, 'co': 2, 'pozwalało': 1, 'osiągnąć': 1, 'krążownikom': 1, 'prędkość': 1, 'prawie': 1, '36': 1, 'węzłów[7].': 1, 'zasięg': 2, 'wynosił': 5, '8500': 1, 'przy': 4, 'prędkości': 4, 'węzłów,': 1, '6000': 1, '14': 4, 'węzłach': 1, '1000': 1, 'wynoszącej': 4, '23': 2, 'węzły[7].': 1, 'energię': 1, 'elektryczną': 1, 'zapewniały': 2, 'spalinowe': 1, 'generatory': 1, 'prądu': 1, 'stałego': 1, 'mocy': 2, 'odpowiednio': 1, '66': 1, '88': 1, 'kw.': 1, 'napięcie': 1, '110': 1, 'v.': 1, 'zainstalowano': 1, 'przedziale': 1, 'maszynowni[7].': 1, 'wyposażenie': 1, 'krążownik': 14, '„kinu”': 5, 'widoczną': 2, 'dziobową': 2, 'platformą': 2, 'startową': 3, 'wodnosamolotów': 2, '(1931': 1, 'rok)': 2, '„abukuma”': 4, 'obrotową': 2, 'rufie': 2, 'wodnosamolotem': 1, '(1941': 1, 'wyposażono': 2, 'dalocelowniki,': 1, 'kompasy.': 1, 'większość': 2, 'wyposażenia': 1, 'kompasowym[8].': 1, 'maszty[8].': 1, 'jeden': 3, 'dziobówką,': 1, 'okolicach': 3, 'rufy[8].': 1, 'dziobowym': 1, 'maszcie': 3, 'dalocelownik': 1, '13': 3, 'służący': 1, 'kierowania': 1, 'ogniem': 1, 'artyleryjskim,': 1, 'dowodzenia': 1, 'artylerią': 1, 'reflektory[8].': 1, '1924–1925': 1, 'prac': 1, 'prowadzonych': 1, 'krążownikach': 3, 'typu,': 1, 'zyskał': 1, 'dodatkową': 1, 'platformę': 2, 'obserwacyjną': 1, 'określania': 1, 'celów[8].': 1, 'rufowym': 1, 'reflektor[8].': 1, 'okręty,': 1, 'zatopionej': 2, '1942': 10, '„yury”,': 1, 'otrzymały': 1, 'radar': 3, 'ostrzegania': 2, 'powietrznego': 2, '21': 3, 'nawodnego': 1, '22.': 1, 'płaską,': 1, 'kwadratową': 1, 'antenę,': 1, 'zamontowano': 5, 'trójnożnym': 1, 'dachu': 1, 'pomostu': 1, 'kompasowego.': 1, 'wypadku': 1, 'krążownika': 1, '„isuzu”,': 4, 'przebudowie': 3, 'przeciwlotniczy': 3, 'dodatkowo': 6, '13.': 1, 'dysponował': 1, 'więc': 1, 'trzema': 2, 'stacjami': 1, 'radiolokacyjnymi[9].': 1, 'wyposażone': 1, 'metrów': 1, 'samolotu': 1, 'myśliwskiego': 1, 'mitsubishi': 1, '1mf.': 1, 'platforma': 1, 'ta': 2, 'została': 7, 'usunięta': 1, '„nagarze”,': 2, '„yurze”': 2, 'pozostałych': 2, '„natori”': 1, '„abukumie”': 1, '1934–1935[6].': 2, 'pomiędzy': 3, '1932': 2, '1934': 2, 'rokiem': 1, 'zyskały': 2, 'katapultę': 1, 'kure': 1, 'typ': 5, '2': 3, 'model': 1, '3': 3, 'wodnosamolotu': 1, 'nakajima': 2, 'e4n.': 1, 'katapulta': 1, 'była': 5, 'stanie': 2, 'przyjąć': 1, 'wodnosamolot': 1, 'maksymalnej': 3, 'startowej': 1, 'tony[6].': 1, 'krążowniki': 7, 'eksploatowały': 1, 'typy': 1, 'dwumiejscowe': 1, 'e8n': 1, 'lub': 2, 'trzymiejscowe': 1, 'kawanishi': 1, 'e7k.': 1, 'maszyn': 1, 'używany': 1, 'był,': 1, 'gdy': 1, 'rolę': 1, 'flagowej': 3, 'floty[10].': 1, 'uzbrojenie': 6, 'armata': 1, 'uniwersalna': 1, '89': 3, '127': 3, 'zamontowana': 1, 'rufowych': 1, 'armat': 3, 'pierwotnie': 1, 'armaty': 5, 'przeciwlotnicze': 3, '76,2': 3, 'służby': 9, 'tę': 1, 'samą': 1, 'konfigurację': 1, 'uzbrojenia[11].': 1, 'momencie': 2, 'wejścia': 2, 'linii,': 1, 'uzbrojono': 1, 'siedem': 1, 'okrętowych': 1, 'l/50': 1, 'mm[11].': 1, 'każde': 1, 'działo': 3, 'umiejscowiono': 3, 'pojedynczym': 1, 'stanowisku': 1, 'ogniowym,': 1, 'osłonięte': 1, 'maski': 1, 'przeciwodłamkowe.': 1, 'umiejscowione': 1, 'dziobie,': 1, 'układzie': 2, 'tandemu,': 1, 'lufy': 2, 'skierowane': 1, 'inne': 1, 'strony.': 1, 'lufa': 1, 'numer': 3, 'skierowana': 1, 'kierunku': 1, 'dziobu,': 1, 'lufę': 1, 'skierowano': 3, 'nadbudówkę[11].': 1, 'bokach': 2, 'nadbudówki': 1, 'jednym': 1, 'dziale': 1, '(jedno': 1, 'każdą': 1, 'burtę)[11].': 1, 'pozostałe': 4, 'wzdłuż': 1, 'płaszczyzny': 1, 'symetrii': 1, 'stanowiska': 1, 'ostatnim': 1, 'kominem': 1, 'ostatnie': 1, 'ulokowane': 1, 'rufie.': 1, 'te': 4, 'szybkostrzelność': 2, '6': 3, 'strzałów': 2, 'minutę': 1, 'donośność': 1, '17': 3, '500': 1, 'm[11].': 1, 'maksymalny': 2, 'kąt': 1, 'podniesienia': 1, '25°[11].': 1, 'pięciu': 1, 'przewidziano': 1, 'pocisków': 1, 'wynoszący': 1, '120': 1, 'sztuk,': 2, 'bocznych': 1, '105': 1, 'sztuk[11].': 1, 'pociski': 1, 'ważyły': 1, '38': 2, 'kg': 1, 'wystrzeliwano': 1, 'pomocą': 1, 'ładunków': 1, 'miotających[11].': 1, 'dysponowały': 3, 'dwiema': 3, 'armatami': 2, 'salutacyjnymi.': 1, '„nagara”': 2, '„yura”': 4, '47': 1, 'kalibrze': 1, '57': 1, 'mm[12].': 1, 'wielokrotnie': 6, 'przezbrajane.': 1, 'składało': 2, 'ono': 1, 'pojedynczych': 2, 'przeciwlotniczych': 1, 'pierwszego': 1, 'komina.': 1, 'amunicji': 1, 'każdej': 1, '240': 1, 'ona': 1, 'rozdzielnego': 1, 'ładowania[12].': 1, 'zwalczać': 1, 'cele': 1, 'odległości': 1, '6500': 1, 'osiągać': 1, 'między': 3, '18': 2, 'minutę[12].': 1, 'uzupełniały': 1, 'karabiny': 3, 'maszynowe': 1, '6,5': 2, 'drugim': 1, 'trzecim': 1, 'kominem.': 1, 'toku': 1, 'dalszej': 1, 'eksploatacji': 1, 'dynamicznego': 1, 'rozwoju': 1, 'lotnictwa': 2, 'szybko': 1, 'okazało': 1, 'być': 1, 'niewystarczające[12].': 1, '1931–1934': 1, 'poczwórnych': 1, 'wielkokalibrowych': 1, 'karabinów': 3, 'maszynowych': 2, 'hotchkiss': 1, '13,2': 4, 'platformie': 1, 'dziobówką[12].': 1, 'natori”': 1, 'poczwórny': 1, 'hotchkissa': 1, 'dwie': 2, 'plot.': 1, 'zastąpiono': 4, 'dwoma': 3, 'podwójnymi': 2, 'stanowiskami': 2, '93': 1, 'które': 2, 'kolei': 1, 'późniejszym': 2, 'czasie': 3, '25': 6, 'mm[6].': 2, 'karabinami': 1, 'maszynowymi': 1, 'lewis': 1, '7,7': 1, 'artyleryjskie': 2, 'stanowiło': 1, 'jedno': 1, 'podwójne': 2, 'uniwersalne': 1, '89,': 1, '8': 5, 'wkm': 1, '22': 2, '96': 1, '×': 3, 'iii,': 1, 'ii': 3, 'i[4].': 1, 'uniwersalnych': 1, 'łącznie': 2, '50': 1, 'różnej': 1, 'konfiguracji[4].': 1, 'czterema': 1, 'wyrzutniami': 1, 'torped': 4, '610': 2, 'mm[13].': 1, 'wyrzutnie': 2, 'poruszane': 1, 'zakresie': 1, '360°': 1, 'silnik': 1, 'elektryczny': 1, 'km[13].': 1, 'pojedynczej': 1, 'wyrzutni': 1, '8,8': 1, 'ważyła': 1, '8,45': 1, 'tony.': 1, 'używano': 1, 'wówczas': 1, '8,42': 1, 'głowicy': 1, 'bojowej': 1, '346': 1, 'kg[13].': 1, 'czterocylindrowym': 1, 'silnikiem': 1, 'spalinowym,': 1, 'który': 2, 'pozwalał': 1, 'osiągnięcie': 1, 'torpedom': 1, 'węzłów[13].': 2, 'ich': 1, '20': 3, 'poczwórnymi': 1, '92': 1, '93.': 1, 'torped.': 1, 'zrzutnie': 1, 'bomb': 1, 'głębinowych[9]': 1, 'tory': 1, 'minowe': 1, '48': 1, 'min': 1, 'morskich[8].': 1, 'przebieg': 1, 'osobny': 6, 'artykuł:': 6, '(1921).': 2, 'stępkę': 4, 'położono': 4, '9': 1, 'września': 6, '1920': 3, 'stoczni': 7, 'sasebo,': 1, 'zwodowano': 3, 'kwietnia': 4, '1921': 5, 'roku.': 9, 'wcielenie': 1, 'miało': 3, '1922': 7, 'brał': 5, 'udział': 6, 'wojnie': 4, 'chińsko-japońskiej,': 2, 'następnie': 1, 'walkach': 1, 'wojny': 2, 'światowej': 1, 'pacyfiku,': 1, 'bitwie': 4, 'midway': 1, 'bitwach': 1, 'guadalcanalem.': 1, 'flagowego.': 2, 'okresie': 7, 'międzywojennym': 5, 'operował': 8, 'głownie': 1, 'wodach': 5, 'morza': 1, 'południowochińskiego.': 1, 'odbywał': 1, 'wiele': 1, 'rejsów': 1, 'ćwiczebnych,': 1, 'będąc': 1, 'kilkukrotnie': 4, 'kierowany': 1, 'rezerwy': 2, 'modernizowany.': 3, 'lipca': 1, '1937': 2, 'konfliktu': 1, 'chińsko-japońskiego': 1, 'wraz': 10, 'grupą': 2, 'niszczycieli': 3, 'patrolował': 2, 'morzu': 2, 'południowochińskim': 1, 'wspierał': 3, 'desant': 5, 'miasta': 1, 'kanton[14].': 1, 'listopadzie': 3, '1939': 1, 'powrócił': 1, 'portu': 1, 'sasebo.': 2, 'kwietniu': 3, '1940': 2, 'przekierowany': 1, 'maizuru[14].': 1, 'czerwca': 1, '1941': 8, 'jednostka': 6, 'operowała': 1, 'składzie': 2, 'sentai': 2, '15[14].': 1, 'listopada': 4, 'bazował': 3, 'palau,': 1, 'wydzielony': 1, 'grupy': 2, 'mającej': 1, 'zaatakować': 1, 'filipiny.': 1, 'grudnia': 5, 'wyruszył': 2, 'grupie': 1, 'składającej': 1, 'siedmiu': 1, 'statków': 1, 'transportowych[14].': 1, 'dniach': 1, '12–13': 1, 'osłaniał': 7, 'pancerniki': 2, '„hiei”': 1, '„kirishima”': 1, 'bitwy': 2, 'guadalcanalem[4].': 1, 'nocnego': 1, 'starcia': 1, 'krążownikiem': 1, 'uss': 3, '„san': 1, 'francisco”': 1, '(ca-38)': 1, 'japoński': 1, 'doznał': 1, 'lekkich': 1, 'uszkodzeń[4].': 1, 'guadalcanalem,': 1, 'niszczycielami': 3, 'walczył': 1, 'pancerników': 1, 'kadm.': 1, 'willisa': 1, 'augustusa': 1, 'lee[4].': 1, '1943': 7, 'u': 3, 'wybrzeży': 3, 'nowej': 1, 'irlandii,': 1, 'uszkodzony.': 1, 'zatopiony': 4, 'amerykański': 2, 'podwodny': 2, '7': 3, 'sierpnia': 4, 'roku[15].': 1, 'isuzu': 2, '„isuzu”': 5, '(1944)': 1, 'uraga': 2, 'dock': 2, 'co.,': 1, '29': 2, 'października': 7, 'wprowadzenie': 1, '15': 4, '1923': 3, 'innymi': 2, 'chin,': 1, 'funkcje': 1, 'flagowego': 1, 'szkolnego.': 1, '1931–1935': 1, 'przechodził': 1, 'kilka': 1, 'modernizacji.': 1, 'grudniu': 1, 'styczniu': 4, 'stacjonował': 1, 'hongkongu[15].': 1, 'prowadził': 1, 'patrole': 1, 'jawajskim[15].': 1, 'atolu': 1, 'truk.': 1, 'siedmioma': 1, '„kongō”': 1, '„haruna”,': 1, 'bombardowanie': 1, 'lotniska': 1, 'henderson': 2, 'field': 2, 'guadalcanalu': 2, 'ciężkie': 1, '„maya”': 1, '„myōkō”[15].': 1, 'wziął': 1, 'koło': 1, 'wysp': 2, 'santa': 1, 'cruz[16].': 1, 'pierwszą': 1, 'połowę': 1, 'przeszedł': 3, 'pierwszą,': 1, 'głębszą': 1, 'początku': 1, 'wojny,': 1, 'polegającej': 1, 'm.in.': 1, 'montażu': 1, 'podwójnej': 1, 'wzmocnieniu': 1, 'obrony': 1, 'przeciwlotniczej.': 1, 'majem': 1, 'wrześniem': 1, 'roku,': 6, 'przebudowany': 1, 'przeciwlotniczy.': 1, 'ataku': 6, 'torpedowego': 2, 'amerykańskich': 1, 'podwodnych': 1, '1945': 1, 'wyspy': 4, 'sumbawy[17].': 1, 'natori': 2, '(1922).': 2, 'położenie': 1, 'stępki': 1, 'odbyło': 1, 'mitsubishi-nagasaki.': 2, 'wszedł': 5, 'dai-nippon': 3, 'teikoku': 3, 'kaigun': 3, 'resztę': 1, 'okresu': 2, 'międzywojennego': 2, 'pełniła': 2, 'odbywała': 2, 'rejsy': 2, 'chińskich.': 2, 'modernizowana.': 1, 'czerwcu': 1, 'rejonie': 3, 'szanghaju.': 1, 'samego': 2, 'hangzhou[17].': 1, 'lutym': 1, 'sajgonie': 1, '(obecnym': 1, 'ho': 1, 'chi': 1, 'minh).': 1, 'siłami': 1, '5.': 2, 'fn': 2, 'floty': 1, 'bazującej': 1, 'tajwanie[17].': 1, 'lipcu': 1, 'sierpniu': 1, 'uczestniczył': 1, 'zajęciu': 1, 'indochin': 1, 'francuskich[17].': 1, 'nocy': 1, '1': 3, 'marca': 5, 'eskortujący': 1, 'inwazyjne': 1, 'stoczył': 1, 'walkę': 1, 'alianckimi': 1, 'krążownikami': 2, '„houston”': 1, '(ca-30)': 1, 'hmas': 1, '„perth”[18].': 1, 'zaatakowany': 1, '„tautog”': 1, '(ss-199).': 1, 'wystrzelone': 1, 'torpedy': 1, 'trafiły': 1, 'rufę': 1, 'krążownika.': 1, 'eksplozja': 1, 'spowodowała': 1, 'oderwanie': 1, 'reszty': 1, '20-metrowej': 1, 'rufy[18].': 1, 'krytycznie': 1, 'uszkodzona': 1, 'trudem': 1, 'dotarła': 1, 'zatoki': 2, 'ambon[18].': 1, 'przełomie': 2, 'głęboką': 1, 'modernizację.': 1, 'amerykańskiego': 2, 'podwodnego': 1, 'pobliżu': 3, 'ujścia': 1, 'cieśniny': 1, 'san': 1, 'bernardino[18].': 1, 'yura': 2, 'maja': 6, 'wodowany': 1, 'lutego': 3, 'incydentu': 1, 'szanghajskiego,': 1, 'artyleryjskim': 1, 'działania': 1, 'lądzie[18].': 1, 'japońsko-chińskiej': 1, 'rejon': 1, 'qingdao[18].': 1, 'okrętem': 1, 'flagowym': 1, 'podwodnych,': 1, 'operując': 1, 'karolinów,': 1, 'marshalla': 1, 'marianów': 1, 'miesiącach': 1, 'września[18].': 1, 'ciężkimi': 1, '„kumano”': 1, '„suzuya”': 1, 'lądowanie': 2, 'endau[19].': 1, 'październiku': 2, 'wsparcia': 1, 'walk': 1, 'lotnisko': 1, '24': 2, 'uderzeniowej': 1, 'opuścił': 1, 'shortland[20].': 1, 'grupa': 1, 'zaatakowana': 1, 'bombowce': 1, 'horyzontalne': 1, 'nurkujące.': 1, 'trafiona': 2, 'bombami': 1, 'okolice': 1, 'rufy[19].': 1, 'około': 1, 'godziny': 1, '15:00': 1, 'nastąpił': 1, 'atak,': 1, 'którego': 1, 'kolejnymi': 1, 'bombami,': 1, 'spowodowało': 1, 'liczne': 1, 'pożary[19].': 1, 'opuściła': 1, 'przeszła': 1, 'niszczyciela': 1, '„murasame”,': 1, 'niszczyciele:': 1, '„yūdachi”': 1, '„harusame”': 1, 'dobiły': 1, 'opuszczony': 1, 'krążownik[19].': 1, 'kinu': 1, 'kinu.': 1, 'stycznia': 1, 'zwodowany': 2, 'głównie': 2, 'chińskich,': 2, 'chińsko-japońskiej.': 1, 'malaje.': 1, 'wspierała': 1, 'miri': 1, 'sarawaku,': 1, 'kuching[21].': 1, 'we': 1, 'wrześniu': 1, 'bliźniaczym': 1, 'statki': 2, 'desantem': 1, 'salomona.': 1, 'wysadził': 1, 'wyspie': 1, 'shortland,': 1, 'moluków[21].': 1, 'głęboką,': 1, 'wojenną': 1, 'modernizacje': 1, 'podobnie': 1, 'serii,': 1, '„yury”.': 1, 'zatoce': 2, 'leyte.': 1, '26': 4, 'ormoc[21].': 1, 'abukuma': 2, '(1923).': 1, 'stępka': 1, 'budowę': 1, 'położona': 1, 'co.': 1, 'cesarskiej': 1, 'marynarce': 1, '1925': 1, 'budowa': 1, 'uległa': 1, 'opóźnieniu': 1, 'powodu': 2, 'zniszczeń': 1, 'trzęsienia': 1, 'ziemi,': 1, 'ostatecznie': 1, 'budowano': 1, '3,5': 1, 'roku[19].': 1, 'japońsko-chińskiej.': 1, 'tamtym': 1, 'modernizowano': 1, 'flotyllą': 1, 'niszczycieli,': 1, 'wyszedł': 1, 'flotą': 1, 'admirała': 1, 'nagumo': 1, 'pearl': 1, 'harbor[19].': 1, 'inwazji': 1, 'jawę': 1, 'ośmioma': 1, 'przechwytywał': 1, 'płynące': 1, 'jawą': 1, 'australią[19].': 1, 'połowie': 1, 'włączono': 1, '1.': 1, 'zespołu': 1, 'regionu': 1, 'północnego,': 1, 'zadanie': 1, 'przejąć': 1, 'aleuty[22].': 1, 'jako': 1, 'część': 1, 'eskorty': 1, 'adak.': 1, 'trakcie': 1, 'rejsu': 1, 'odwołano': 1, 'operację': 1, 'niepowodzenia': 1, 'midway.': 1, 'attu,': 1, 'wylądowała': 1, 'czerwca.': 1, 'pozostawały': 1, 'rejonie,': 1, 'patrolując': 1, 'go': 1, 'połowy': 1, 'czerwca[23].': 1, 'kiska.': 1, 'jednostkę': 1, 'zmodernizowano': 1, 'wzór': 1, 'nagara.': 1, 'uczestniczyła': 1, 'leyte,': 1, 'zatopiona[23].': 1}
klucz  opis  ma wartosc  2
klucz  konstrukcji  ma wartosc  1
klucz  ogólny  ma wartosc  1
klucz  sylwetka  ma wartosc  1
klucz  okrętów  ma wartosc  7
klucz  typu  ma wartosc  14
klucz  nagara  ma wartosc  3
klucz  sprzed  ma wartosc  1
klucz  wojennej  ma wartosc  2
klucz  przebudowy  ma wartosc  1
klucz  (poniżej  ma wartosc  1
klucz  schemat  ma wartosc  2
klucz  kątów  ma wartosc  1
klucz  ostrzału  ma wartosc  1
klucz  artylerii  ma wartosc  1
klucz  i  ma wartosc  37
klucz  opancerzenia)  ma wartosc  1
klucz  kadłub  ma wartosc  4
klucz  krążowników  ma wartosc  4
klucz  miał  ma wartosc  3
klucz  162,15  ma wartosc  1
klucz  m  ma wartosc  7
klucz  długości  ma wartosc  4
klucz  całkowitej,  ma wartosc  1
klucz  zaś  ma wartosc  8
klucz  na  ma wartosc  65
klucz  linii  ma wartosc  1
klucz  wodnej  ma wartosc  1
klucz  długość  ma wartosc  3
klucz  wynosiła  ma wartosc  5
klucz  156,65  ma wartosc  1
klucz  m[2].  ma wartosc  1
klucz  szerokość  ma wartosc  1
klucz  jednostki  ma wartosc  10
klucz  14,17  ma wartosc  1
klucz  m,  ma wartosc  2
klucz  natomiast  ma wartosc  4
klucz  jej  ma wartosc  1
klucz  zanurzenie  ma wartosc  1
klucz  wynosiło  ma wartosc  2
klucz  4,85  ma wartosc  1
klucz  m[3][2].  ma wartosc  1
klucz  wyporność  ma wartosc  2
klucz  standardowa  ma wartosc  2
klucz  5170  ma wartosc  1
klucz  ts,  ma wartosc  1
klucz  normalna  ma wartosc  1
klucz  5690  ma wartosc  1
klucz  ts.  ma wartosc  1
klucz  w  ma wartosc  128
klucz  wyniku  ma wartosc  5
klucz  modernizacji  ma wartosc  1
klucz  z  ma wartosc  33
klucz  1944  ma wartosc  9
klucz  roku  ma wartosc  44
klucz  wzrosła  ma wartosc  1
klucz  do  ma wartosc  26
klucz  6050  ma wartosc  1
klucz  ts[4].  ma wartosc  1
klucz  zewnętrzny  ma wartosc  1
klucz  wykonano  ma wartosc  1
klucz  płyt  ma wartosc  2
klucz  stalowych  ma wartosc  1
klucz  o  ma wartosc  16
klucz  grubości  ma wartosc  6
klucz  19  ma wartosc  1
klucz  25,4  ma wartosc  2
klucz  mm,  ma wartosc  6
klucz  a  ma wartosc  11
klucz  płyty  ma wartosc  2
klucz  stanowiące  ma wartosc  1
klucz  wewnętrzne  ma wartosc  1
klucz  elementy  ma wartosc  1
klucz  kadłuba  ma wartosc  4
klucz  miały  ma wartosc  7
klucz  grubość  ma wartosc  2
klucz  od  ma wartosc  15
klucz  6,4  ma wartosc  1
klucz  12,7  ma wartosc  1
klucz  mm[5].  ma wartosc  1
klucz  grubsze  ma wartosc  1
klucz  znajdowały  ma wartosc  6
klucz  się  ma wartosc  28
klucz  kluczowych  ma wartosc  1
klucz  dla  ma wartosc  10
klucz  żywotności  ma wartosc  1
klucz  okrętu  ma wartosc  7
klucz  miejscach[5].  ma wartosc  1
klucz  okręty  ma wartosc  12
klucz  trzy  ma wartosc  3
klucz  pokłady:  ma wartosc  1
klucz  pokład  ma wartosc  7
klucz  główny,  ma wartosc  1
klucz  ciągnący  ma wartosc  1
klucz  przez  ma wartosc  11
klucz  całą  ma wartosc  1
klucz  jednostki,  ma wartosc  1
klucz  drugi  ma wartosc  3
klucz  –  ma wartosc  4
klucz  znajdujący  ma wartosc  1
klucz  przed  ma wartosc  4
klucz  przedziałem  ma wartosc  2
klucz  kotłowni  ma wartosc  5
klucz  części  ma wartosc  5
klucz  dziobowej  ma wartosc  3
klucz  oraz  ma wartosc  35
klucz  za  ma wartosc  9
klucz  maszynowni  ma wartosc  1
klucz  rufowej[5].  ma wartosc  1
klucz  poniżej  ma wartosc  1
klucz  znajdował  ma wartosc  5
klucz  ostatni  ma wartosc  2
klucz  pełniący  ma wartosc  1
klucz  funkcję  ma wartosc  6
klucz  ładowni[5].  ma wartosc  1
klucz  śródokręcie  ma wartosc  1
klucz  jednostek  ma wartosc  2
klucz  było  ma wartosc  6
klucz  podwyższone  ma wartosc  1
klucz  przykryte  ma wartosc  1
klucz  pokładem  ma wartosc  4
klucz  łodziowym[5].  ma wartosc  1
klucz  śródokręciu  ma wartosc  2
klucz  ulokowano  ma wartosc  5
klucz  kabiny  ma wartosc  2
klucz  załogi,  ma wartosc  1
klucz  kambuz,  ma wartosc  1
klucz  instalacje  ma wartosc  1
klucz  sanitariatu  ma wartosc  1
klucz  magazyny.  ma wartosc  1
klucz  nadbudówce  ma wartosc  2
klucz  rufowej  ma wartosc  1
klucz  oficerów,  ma wartosc  1
klucz  umywalnie  ma wartosc  1
klucz  dalsze  ma wartosc  1
klucz  pomieszczenia  ma wartosc  4
klucz  magazynowe[5].  ma wartosc  1
klucz  załogi  ma wartosc  1
klucz  pokładzie  ma wartosc  2
klucz  głównym  ma wartosc  1
klucz  kotłowniami  ma wartosc  1
klucz  śródokręciu,  ma wartosc  2
klucz  pod  ma wartosc  9
klucz  łodziowym.  ma wartosc  1
klucz  podoficerowie  ma wartosc  1
klucz  zajmowali  ma wartosc  1
klucz  miejsca  ma wartosc  1
klucz  kabinami  ma wartosc  1
klucz  oficerskimi[6].  ma wartosc  1
klucz  znajdowała  ma wartosc  3
klucz  także  ma wartosc  2
klucz  wysoka  ma wartosc  1
klucz  dziobówka.  ma wartosc  1
klucz  składała  ma wartosc  1
klucz  czterech  ma wartosc  3
klucz  poziomów,  ma wartosc  1
klucz  gdzie  ma wartosc  6
klucz  pierwszym  ma wartosc  1
klucz  nich  ma wartosc  1
klucz  kabinę  ma wartosc  2
klucz  radiową,  ma wartosc  1
klucz  nad  ma wartosc  1
klucz  którą  ma wartosc  2
klucz  znajdowało  ma wartosc  2
klucz  pomieszczenie  ma wartosc  3
klucz  nakresowe  ma wartosc  1
klucz  operacyjne[7].  ma wartosc  1
klucz  wyżej  ma wartosc  1
klucz  kompasowy,  ma wartosc  1
klucz  którym  ma wartosc  1
klucz  oprócz  ma wartosc  3
klucz  kompasów  ma wartosc  1
klucz  dalmierze,  ma wartosc  1
klucz  lornety  ma wartosc  2
klucz  dalocelownik[7].  ma wartosc  1
klucz  nadbudówki,  ma wartosc  1
klucz  tuż  ma wartosc  1
klucz  kompasowym  ma wartosc  1
klucz  stanowisko  ma wartosc  3
klucz  dowodzenia[7].  ma wartosc  1
klucz  początkowo  ma wartosc  2
klucz  hangar  ma wartosc  1
klucz  wodnosamolotu,  ma wartosc  1
klucz  jednak  ma wartosc  2
klucz  podczas  ma wartosc  12
klucz  modernizacji,  ma wartosc  1
klucz  która  ma wartosc  1
klucz  zależności  ma wartosc  1
klucz  odbyła  ma wartosc  1
klucz  latach  ma wartosc  8
klucz  1931–1934,  ma wartosc  2
klucz  został  ma wartosc  9
klucz  on  ma wartosc  2
klucz  zlikwidowany  ma wartosc  1
klucz  jego  ma wartosc  2
klucz  miejsce  ma wartosc  5
klucz  utworzono  ma wartosc  1
klucz  łączności,  ma wartosc  1
klucz  sztabu  ma wartosc  1
klucz  dowództwa  ma wartosc  1
klucz  flotylli  ma wartosc  2
klucz  powiększono  ma wartosc  1
klucz  centrum  ma wartosc  1
klucz  bojowe[6].  ma wartosc  1
klucz  załoga  ma wartosc  2
klucz  liczyła  ma wartosc  1
klucz  bazowo  ma wartosc  1
klucz  450  ma wartosc  1
klucz  osób,  ma wartosc  2
klucz  tym  ma wartosc  6
klucz  37  ma wartosc  1
klucz  oficerów.  ma wartosc  1
klucz  przypadku  ma wartosc  3
klucz  jeśli  ma wartosc  1
klucz  okręt  ma wartosc  39
klucz  pełnił  ma wartosc  5
klucz  flagowego,  ma wartosc  1
klucz  zaokrętowanych  ma wartosc  1
klucz  nim  ma wartosc  1
klucz  dodatkowych  ma wartosc  1
klucz  27  ma wartosc  3
klucz  5  ma wartosc  3
klucz  oficerów[6].  ma wartosc  1
klucz  opancerzenie  ma wartosc  2
klucz  zastosowany  ma wartosc  1
klucz  układ  ma wartosc  3
klucz  opancerzenia  ma wartosc  1
klucz  był  ma wartosc  4
klucz  praktycznie  ma wartosc  2
klucz  taki  ma wartosc  1
klucz  sam  ma wartosc  1
klucz  jak  ma wartosc  2
klucz  projektu  ma wartosc  1
klucz  kuma[2].  ma wartosc  1
klucz  pas  ma wartosc  2
klucz  pancerny  ma wartosc  1
klucz  63,5  ma wartosc  1
klucz  łączący  ma wartosc  1
klucz  górnym,  ma wartosc  1
klucz  73,17  ma wartosc  1
klucz  wysokości  ma wartosc  1
klucz  4,87  ma wartosc  1
klucz  czego  ma wartosc  1
klucz  0,84  ma wartosc  1
klucz  wodą[2].  ma wartosc  1
klucz  rozwiązanie  ma wartosc  1
klucz  to  ma wartosc  5
klucz  zapewniało  ma wartosc  1
klucz  ochronę  ma wartosc  1
klucz  ostrzałem  ma wartosc  2
klucz  dział  ma wartosc  8
klucz  kalibru  ma wartosc  8
klucz  102  ma wartosc  1
klucz  mm.  ma wartosc  3
klucz  ten  ma wartosc  2
klucz  po  ma wartosc  13
klucz  obu  ma wartosc  1
klucz  stronach  ma wartosc  1
klucz  burt  ma wartosc  1
klucz  chronił  ma wartosc  1
klucz  maszynowni.  ma wartosc  1
klucz  wykonany  ma wartosc  1
klucz  ze  ma wartosc  2
klucz  stali  ma wartosc  1
klucz  wysokiej  ma wartosc  1
klucz  odporności  ma wartosc  1
klucz  rozciąganie  ma wartosc  1
klucz  składał  ma wartosc  1
klucz  dwóch  ma wartosc  5
klucz  warstw  ma wartosc  1
klucz  pancernych:  ma wartosc  1
klucz  warstwy  ma wartosc  1
klucz  zewnętrznej  ma wartosc  1
klucz  liczącej  ma wartosc  1
klucz  38,1  ma wartosc  1
klucz  mm  ma wartosc  18
klucz  wewnętrznej,  ma wartosc  1
klucz  której  ma wartosc  2
klucz  mm[2].  ma wartosc  4
klucz  główny  ma wartosc  1
klucz  pokryto  ma wartosc  1
klucz  płytami  ma wartosc  2
klucz  pancernymi  ma wartosc  2
klucz  28,5  ma wartosc  1
klucz  zamontowane  ma wartosc  3
klucz  wcześniej  ma wartosc  2
klucz  główne  ma wartosc  1
klucz  działa  ma wartosc  7
klucz  kal.  ma wartosc  16
klucz  140  ma wartosc  4
klucz  osłonięto  ma wartosc  1
klucz  maskami  ma wartosc  1
klucz  10  ma wartosc  5
klucz  komory  ma wartosc  1
klucz  amunicyjne  ma wartosc  1
klucz  głównych  ma wartosc  3
klucz  zostały  ma wartosc  2
klucz  opancerzone  ma wartosc  1
klucz  32  ma wartosc  1
klucz  podajników  ma wartosc  1
klucz  amunicyjnych  ma wartosc  1
klucz  16  ma wartosc  5
klucz  napędowy  ma wartosc  2
klucz  napędzane  ma wartosc  2
klucz  były  ma wartosc  9
klucz  pośrednictwem  ma wartosc  4
klucz  zespołów  ma wartosc  1
klucz  turbin  ma wartosc  2
klucz  parowych  ma wartosc  1
klucz  parsonsa,  ma wartosc  1
klucz  których  ma wartosc  1
klucz  skład  ma wartosc  2
klucz  wchodziła  ma wartosc  1
klucz  turbina  ma wartosc  2
klucz  wysokociśnieniowa  ma wartosc  1
klucz  gihon  ma wartosc  1
klucz  reakcyjna  ma wartosc  1
klucz  niskociśnieniowa  ma wartosc  1
klucz  mitsubishi-parsons[5].  ma wartosc  1
klucz  każdy  ma wartosc  1
klucz  zespół  ma wartosc  2
klucz  własnej  ma wartosc  1
klucz  przekładni  ma wartosc  1
klucz  redukcyjnej  ma wartosc  1
klucz  napędzał  ma wartosc  1
klucz  swoją  ma wartosc  2
klucz  linię  ma wartosc  1
klucz  wału  ma wartosc  1
klucz  napędowego,  ma wartosc  1
klucz  zakończoną  ma wartosc  1
klucz  pojedynczą,  ma wartosc  1
klucz  trójpłatową  ma wartosc  1
klucz  śrubą  ma wartosc  1
klucz  napędową[5].  ma wartosc  1
klucz  turbiny  ma wartosc  1
klucz  zasilane  ma wartosc  1
klucz  dwunastu  ma wartosc  1
klucz  kotłów  ma wartosc  1
klucz  opalanych  ma wartosc  1
klucz  paliwem  ma wartosc  4
klucz  płynnym[a]  ma wartosc  1
klucz  węglem[5].  ma wartosc  1
klucz  cztery  ma wartosc  4
klucz  kotłowni,  ma wartosc  1
klucz  pierwszej  ma wartosc  1
klucz  strony  ma wartosc  1
klucz  dziobu  ma wartosc  1
klucz  dwa  ma wartosc  12
klucz  małe  ma wartosc  1
klucz  kotły  ma wartosc  5
klucz  opalane  ma wartosc  4
klucz  olejowym  ma wartosc  1
klucz  węglem,  ma wartosc  1
klucz  drugiej  ma wartosc  1
klucz  ropą[5].  ma wartosc  1
klucz  trzeciej  ma wartosc  2
klucz  zajmowane  ma wartosc  1
klucz  ropę,  ma wartosc  1
klucz  ostatniej,  ma wartosc  1
klucz  czwartej  ma wartosc  1
klucz  również  ma wartosc  1
klucz  ciekłym[5].  ma wartosc  1
klucz  generowały  ma wartosc  2
klucz  one  ma wartosc  3
klucz  parę  ma wartosc  1
klucz  ciśnieniu  ma wartosc  1
klucz  wynoszącym  ma wartosc  1
klucz  18,3  ma wartosc  1
klucz  kgf/cm²[5].  ma wartosc  1
klucz  zabierały  ma wartosc  2
klucz  zapas  ma wartosc  5
klucz  paliwa  ma wartosc  1
klucz  płynnego  ma wartosc  1
klucz  masie  ma wartosc  3
klucz  1284  ma wartosc  1
klucz  ton  ma wartosc  2
klucz  350  ma wartosc  1
klucz  węgla[5].  ma wartosc  1
klucz  węglem  ma wartosc  1
klucz  zmodernizowane  ma wartosc  1
klucz  tego  ma wartosc  5
klucz  czasu  ma wartosc  1
klucz  opalano  ma wartosc  1
klucz  je  ma wartosc  3
klucz  wyłącznie  ma wartosc  1
klucz  płynnym.  ma wartosc  1
klucz  modernizację  ma wartosc  2
klucz  siłowni  ma wartosc  1
klucz  poszczególnych  ma wartosc  1
klucz  okrętach  ma wartosc  2
klucz  przeprowadzono  ma wartosc  1
klucz  1934–1938[6].  ma wartosc  1
klucz  spaliny  ma wartosc  1
klucz  odprowadzane  ma wartosc  1
klucz  trzech  ma wartosc  2
klucz  kominów  ma wartosc  1
klucz  śródokręciu[7].  ma wartosc  1
klucz  generował  ma wartosc  1
klucz  maksymalną  ma wartosc  3
klucz  moc  ma wartosc  1
klucz  wynoszącą  ma wartosc  2
klucz  90  ma wartosc  1
klucz  000  ma wartosc  2
klucz  km,  ma wartosc  1
klucz  co  ma wartosc  2
klucz  pozwalało  ma wartosc  1
klucz  osiągnąć  ma wartosc  1
klucz  krążownikom  ma wartosc  1
klucz  prędkość  ma wartosc  1
klucz  prawie  ma wartosc  1
klucz  36  ma wartosc  1
klucz  węzłów[7].  ma wartosc  1
klucz  zasięg  ma wartosc  2
klucz  wynosił  ma wartosc  5
klucz  8500  ma wartosc  1
klucz  przy  ma wartosc  4
klucz  prędkości  ma wartosc  4
klucz  węzłów,  ma wartosc  1
klucz  6000  ma wartosc  1
klucz  14  ma wartosc  4
klucz  węzłach  ma wartosc  1
klucz  1000  ma wartosc  1
klucz  wynoszącej  ma wartosc  4
klucz  23  ma wartosc  2
klucz  węzły[7].  ma wartosc  1
klucz  energię  ma wartosc  1
klucz  elektryczną  ma wartosc  1
klucz  zapewniały  ma wartosc  2
klucz  spalinowe  ma wartosc  1
klucz  generatory  ma wartosc  1
klucz  prądu  ma wartosc  1
klucz  stałego  ma wartosc  1
klucz  mocy  ma wartosc  2
klucz  odpowiednio  ma wartosc  1
klucz  66  ma wartosc  1
klucz  88  ma wartosc  1
klucz  kw.  ma wartosc  1
klucz  napięcie  ma wartosc  1
klucz  110  ma wartosc  1
klucz  v.  ma wartosc  1
klucz  zainstalowano  ma wartosc  1
klucz  przedziale  ma wartosc  1
klucz  maszynowni[7].  ma wartosc  1
klucz  wyposażenie  ma wartosc  1
klucz  krążownik  ma wartosc  14
klucz  „kinu”  ma wartosc  5
klucz  widoczną  ma wartosc  2
klucz  dziobową  ma wartosc  2
klucz  platformą  ma wartosc  2
klucz  startową  ma wartosc  3
klucz  wodnosamolotów  ma wartosc  2
klucz  (1931  ma wartosc  1
klucz  rok)  ma wartosc  2
klucz  „abukuma”  ma wartosc  4
klucz  obrotową  ma wartosc  2
klucz  rufie  ma wartosc  2
klucz  wodnosamolotem  ma wartosc  1
klucz  (1941  ma wartosc  1
klucz  wyposażono  ma wartosc  2
klucz  dalocelowniki,  ma wartosc  1
klucz  kompasy.  ma wartosc  1
klucz  większość  ma wartosc  2
klucz  wyposażenia  ma wartosc  1
klucz  kompasowym[8].  ma wartosc  1
klucz  maszty[8].  ma wartosc  1
klucz  jeden  ma wartosc  3
klucz  dziobówką,  ma wartosc  1
klucz  okolicach  ma wartosc  3
klucz  rufy[8].  ma wartosc  1
klucz  dziobowym  ma wartosc  1
klucz  maszcie  ma wartosc  3
klucz  dalocelownik  ma wartosc  1
klucz  13  ma wartosc  3
klucz  służący  ma wartosc  1
klucz  kierowania  ma wartosc  1
klucz  ogniem  ma wartosc  1
klucz  artyleryjskim,  ma wartosc  1
klucz  dowodzenia  ma wartosc  1
klucz  artylerią  ma wartosc  1
klucz  reflektory[8].  ma wartosc  1
klucz  1924–1925  ma wartosc  1
klucz  prac  ma wartosc  1
klucz  prowadzonych  ma wartosc  1
klucz  krążownikach  ma wartosc  3
klucz  typu,  ma wartosc  1
klucz  zyskał  ma wartosc  1
klucz  dodatkową  ma wartosc  1
klucz  platformę  ma wartosc  2
klucz  obserwacyjną  ma wartosc  1
klucz  określania  ma wartosc  1
klucz  celów[8].  ma wartosc  1
klucz  rufowym  ma wartosc  1
klucz  reflektor[8].  ma wartosc  1
klucz  okręty,  ma wartosc  1
klucz  zatopionej  ma wartosc  2
klucz  1942  ma wartosc  10
klucz  „yury”,  ma wartosc  1
klucz  otrzymały  ma wartosc  1
klucz  radar  ma wartosc  3
klucz  ostrzegania  ma wartosc  2
klucz  powietrznego  ma wartosc  2
klucz  21  ma wartosc  3
klucz  nawodnego  ma wartosc  1
klucz  22.  ma wartosc  1
klucz  płaską,  ma wartosc  1
klucz  kwadratową  ma wartosc  1
klucz  antenę,  ma wartosc  1
klucz  zamontowano  ma wartosc  5
klucz  trójnożnym  ma wartosc  1
klucz  dachu  ma wartosc  1
klucz  pomostu  ma wartosc  1
klucz  kompasowego.  ma wartosc  1
klucz  wypadku  ma wartosc  1
klucz  krążownika  ma wartosc  1
klucz  „isuzu”,  ma wartosc  4
klucz  przebudowie  ma wartosc  3
klucz  przeciwlotniczy  ma wartosc  3
klucz  dodatkowo  ma wartosc  6
klucz  13.  ma wartosc  1
klucz  dysponował  ma wartosc  1
klucz  więc  ma wartosc  1
klucz  trzema  ma wartosc  2
klucz  stacjami  ma wartosc  1
klucz  radiolokacyjnymi[9].  ma wartosc  1
klucz  wyposażone  ma wartosc  1
klucz  metrów  ma wartosc  1
klucz  samolotu  ma wartosc  1
klucz  myśliwskiego  ma wartosc  1
klucz  mitsubishi  ma wartosc  1
klucz  1mf.  ma wartosc  1
klucz  platforma  ma wartosc  1
klucz  ta  ma wartosc  2
klucz  została  ma wartosc  7
klucz  usunięta  ma wartosc  1
klucz  „nagarze”,  ma wartosc  2
klucz  „yurze”  ma wartosc  2
klucz  pozostałych  ma wartosc  2
klucz  „natori”  ma wartosc  1
klucz  „abukumie”  ma wartosc  1
klucz  1934–1935[6].  ma wartosc  2
klucz  pomiędzy  ma wartosc  3
klucz  1932  ma wartosc  2
klucz  1934  ma wartosc  2
klucz  rokiem  ma wartosc  1
klucz  zyskały  ma wartosc  2
klucz  katapultę  ma wartosc  1
klucz  kure  ma wartosc  1
klucz  typ  ma wartosc  5
klucz  2  ma wartosc  3
klucz  model  ma wartosc  1
klucz  3  ma wartosc  3
klucz  wodnosamolotu  ma wartosc  1
klucz  nakajima  ma wartosc  2
klucz  e4n.  ma wartosc  1
klucz  katapulta  ma wartosc  1
klucz  była  ma wartosc  5
klucz  stanie  ma wartosc  2
klucz  przyjąć  ma wartosc  1
klucz  wodnosamolot  ma wartosc  1
klucz  maksymalnej  ma wartosc  3
klucz  startowej  ma wartosc  1
klucz  tony[6].  ma wartosc  1
klucz  krążowniki  ma wartosc  7
klucz  eksploatowały  ma wartosc  1
klucz  typy  ma wartosc  1
klucz  dwumiejscowe  ma wartosc  1
klucz  e8n  ma wartosc  1
klucz  lub  ma wartosc  2
klucz  trzymiejscowe  ma wartosc  1
klucz  kawanishi  ma wartosc  1
klucz  e7k.  ma wartosc  1
klucz  maszyn  ma wartosc  1
klucz  używany  ma wartosc  1
klucz  był,  ma wartosc  1
klucz  gdy  ma wartosc  1
klucz  rolę  ma wartosc  1
klucz  flagowej  ma wartosc  3
klucz  floty[10].  ma wartosc  1
klucz  uzbrojenie  ma wartosc  6
klucz  armata  ma wartosc  1
klucz  uniwersalna  ma wartosc  1
klucz  89  ma wartosc  3
klucz  127  ma wartosc  3
klucz  zamontowana  ma wartosc  1
klucz  rufowych  ma wartosc  1
klucz  armat  ma wartosc  3
klucz  pierwotnie  ma wartosc  1
klucz  armaty  ma wartosc  5
klucz  przeciwlotnicze  ma wartosc  3
klucz  76,2  ma wartosc  3
klucz  służby  ma wartosc  9
klucz  tę  ma wartosc  1
klucz  samą  ma wartosc  1
klucz  konfigurację  ma wartosc  1
klucz  uzbrojenia[11].  ma wartosc  1
klucz  momencie  ma wartosc  2
klucz  wejścia  ma wartosc  2
klucz  linii,  ma wartosc  1
klucz  uzbrojono  ma wartosc  1
klucz  siedem  ma wartosc  1
klucz  okrętowych  ma wartosc  1
klucz  l/50  ma wartosc  1
klucz  mm[11].  ma wartosc  1
klucz  każde  ma wartosc  1
klucz  działo  ma wartosc  3
klucz  umiejscowiono  ma wartosc  3
klucz  pojedynczym  ma wartosc  1
klucz  stanowisku  ma wartosc  1
klucz  ogniowym,  ma wartosc  1
klucz  osłonięte  ma wartosc  1
klucz  maski  ma wartosc  1
klucz  przeciwodłamkowe.  ma wartosc  1
klucz  umiejscowione  ma wartosc  1
klucz  dziobie,  ma wartosc  1
klucz  układzie  ma wartosc  2
klucz  tandemu,  ma wartosc  1
klucz  lufy  ma wartosc  2
klucz  skierowane  ma wartosc  1
klucz  inne  ma wartosc  1
klucz  strony.  ma wartosc  1
klucz  lufa  ma wartosc  1
klucz  numer  ma wartosc  3
klucz  skierowana  ma wartosc  1
klucz  kierunku  ma wartosc  1
klucz  dziobu,  ma wartosc  1
klucz  lufę  ma wartosc  1
klucz  skierowano  ma wartosc  3
klucz  nadbudówkę[11].  ma wartosc  1
klucz  bokach  ma wartosc  2
klucz  nadbudówki  ma wartosc  1
klucz  jednym  ma wartosc  1
klucz  dziale  ma wartosc  1
klucz  (jedno  ma wartosc  1
klucz  każdą  ma wartosc  1
klucz  burtę)[11].  ma wartosc  1
klucz  pozostałe  ma wartosc  4
klucz  wzdłuż  ma wartosc  1
klucz  płaszczyzny  ma wartosc  1
klucz  symetrii  ma wartosc  1
klucz  stanowiska  ma wartosc  1
klucz  ostatnim  ma wartosc  1
klucz  kominem  ma wartosc  1
klucz  ostatnie  ma wartosc  1
klucz  ulokowane  ma wartosc  1
klucz  rufie.  ma wartosc  1
klucz  te  ma wartosc  4
klucz  szybkostrzelność  ma wartosc  2
klucz  6  ma wartosc  3
klucz  strzałów  ma wartosc  2
klucz  minutę  ma wartosc  1
klucz  donośność  ma wartosc  1
klucz  17  ma wartosc  3
klucz  500  ma wartosc  1
klucz  m[11].  ma wartosc  1
klucz  maksymalny  ma wartosc  2
klucz  kąt  ma wartosc  1
klucz  podniesienia  ma wartosc  1
klucz  25°[11].  ma wartosc  1
klucz  pięciu  ma wartosc  1
klucz  przewidziano  ma wartosc  1
klucz  pocisków  ma wartosc  1
klucz  wynoszący  ma wartosc  1
klucz  120  ma wartosc  1
klucz  sztuk,  ma wartosc  2
klucz  bocznych  ma wartosc  1
klucz  105  ma wartosc  1
klucz  sztuk[11].  ma wartosc  1
klucz  pociski  ma wartosc  1
klucz  ważyły  ma wartosc  1
klucz  38  ma wartosc  2
klucz  kg  ma wartosc  1
klucz  wystrzeliwano  ma wartosc  1
klucz  pomocą  ma wartosc  1
klucz  ładunków  ma wartosc  1
klucz  miotających[11].  ma wartosc  1
klucz  dysponowały  ma wartosc  3
klucz  dwiema  ma wartosc  3
klucz  armatami  ma wartosc  2
klucz  salutacyjnymi.  ma wartosc  1
klucz  „nagara”  ma wartosc  2
klucz  „yura”  ma wartosc  4
klucz  47  ma wartosc  1
klucz  kalibrze  ma wartosc  1
klucz  57  ma wartosc  1
klucz  mm[12].  ma wartosc  1
klucz  wielokrotnie  ma wartosc  6
klucz  przezbrajane.  ma wartosc  1
klucz  składało  ma wartosc  2
klucz  ono  ma wartosc  1
klucz  pojedynczych  ma wartosc  2
klucz  przeciwlotniczych  ma wartosc  1
klucz  pierwszego  ma wartosc  1
klucz  komina.  ma wartosc  1
klucz  amunicji  ma wartosc  1
klucz  każdej  ma wartosc  1
klucz  240  ma wartosc  1
klucz  ona  ma wartosc  1
klucz  rozdzielnego  ma wartosc  1
klucz  ładowania[12].  ma wartosc  1
klucz  zwalczać  ma wartosc  1
klucz  cele  ma wartosc  1
klucz  odległości  ma wartosc  1
klucz  6500  ma wartosc  1
klucz  osiągać  ma wartosc  1
klucz  między  ma wartosc  3
klucz  18  ma wartosc  2
klucz  minutę[12].  ma wartosc  1
klucz  uzupełniały  ma wartosc  1
klucz  karabiny  ma wartosc  3
klucz  maszynowe  ma wartosc  1
klucz  6,5  ma wartosc  2
klucz  drugim  ma wartosc  1
klucz  trzecim  ma wartosc  1
klucz  kominem.  ma wartosc  1
klucz  toku  ma wartosc  1
klucz  dalszej  ma wartosc  1
klucz  eksploatacji  ma wartosc  1
klucz  dynamicznego  ma wartosc  1
klucz  rozwoju  ma wartosc  1
klucz  lotnictwa  ma wartosc  2
klucz  szybko  ma wartosc  1
klucz  okazało  ma wartosc  1
klucz  być  ma wartosc  1
klucz  niewystarczające[12].  ma wartosc  1
klucz  1931–1934  ma wartosc  1
klucz  poczwórnych  ma wartosc  1
klucz  wielkokalibrowych  ma wartosc  1
klucz  karabinów  ma wartosc  3
klucz  maszynowych  ma wartosc  2
klucz  hotchkiss  ma wartosc  1
klucz  13,2  ma wartosc  4
klucz  platformie  ma wartosc  1
klucz  dziobówką[12].  ma wartosc  1
klucz  natori”  ma wartosc  1
klucz  poczwórny  ma wartosc  1
klucz  hotchkissa  ma wartosc  1
klucz  dwie  ma wartosc  2
klucz  plot.  ma wartosc  1
klucz  zastąpiono  ma wartosc  4
klucz  dwoma  ma wartosc  3
klucz  podwójnymi  ma wartosc  2
klucz  stanowiskami  ma wartosc  2
klucz  93  ma wartosc  1
klucz  które  ma wartosc  2
klucz  kolei  ma wartosc  1
klucz  późniejszym  ma wartosc  2
klucz  czasie  ma wartosc  3
klucz  25  ma wartosc  6
klucz  mm[6].  ma wartosc  2
klucz  karabinami  ma wartosc  1
klucz  maszynowymi  ma wartosc  1
klucz  lewis  ma wartosc  1
klucz  7,7  ma wartosc  1
klucz  artyleryjskie  ma wartosc  2
klucz  stanowiło  ma wartosc  1
klucz  jedno  ma wartosc  1
klucz  podwójne  ma wartosc  2
klucz  uniwersalne  ma wartosc  1
klucz  89,  ma wartosc  1
klucz  8  ma wartosc  5
klucz  wkm  ma wartosc  1
klucz  22  ma wartosc  2
klucz  96  ma wartosc  1
klucz  ×  ma wartosc  3
klucz  iii,  ma wartosc  1
klucz  ii  ma wartosc  3
klucz  i[4].  ma wartosc  1
klucz  uniwersalnych  ma wartosc  1
klucz  łącznie  ma wartosc  2
klucz  50  ma wartosc  1
klucz  różnej  ma wartosc  1
klucz  konfiguracji[4].  ma wartosc  1
klucz  czterema  ma wartosc  1
klucz  wyrzutniami  ma wartosc  1
klucz  torped  ma wartosc  4
klucz  610  ma wartosc  2
klucz  mm[13].  ma wartosc  1
klucz  wyrzutnie  ma wartosc  2
klucz  poruszane  ma wartosc  1
klucz  zakresie  ma wartosc  1
klucz  360°  ma wartosc  1
klucz  silnik  ma wartosc  1
klucz  elektryczny  ma wartosc  1
klucz  km[13].  ma wartosc  1
klucz  pojedynczej  ma wartosc  1
klucz  wyrzutni  ma wartosc  1
klucz  8,8  ma wartosc  1
klucz  ważyła  ma wartosc  1
klucz  8,45  ma wartosc  1
klucz  tony.  ma wartosc  1
klucz  używano  ma wartosc  1
klucz  wówczas  ma wartosc  1
klucz  8,42  ma wartosc  1
klucz  głowicy  ma wartosc  1
klucz  bojowej  ma wartosc  1
klucz  346  ma wartosc  1
klucz  kg[13].  ma wartosc  1
klucz  czterocylindrowym  ma wartosc  1
klucz  silnikiem  ma wartosc  1
klucz  spalinowym,  ma wartosc  1
klucz  który  ma wartosc  2
klucz  pozwalał  ma wartosc  1
klucz  osiągnięcie  ma wartosc  1
klucz  torpedom  ma wartosc  1
klucz  węzłów[13].  ma wartosc  2
klucz  ich  ma wartosc  1
klucz  20  ma wartosc  3
klucz  poczwórnymi  ma wartosc  1
klucz  92  ma wartosc  1
klucz  93.  ma wartosc  1
klucz  torped.  ma wartosc  1
klucz  zrzutnie  ma wartosc  1
klucz  bomb  ma wartosc  1
klucz  głębinowych[9]  ma wartosc  1
klucz  tory  ma wartosc  1
klucz  minowe  ma wartosc  1
klucz  48  ma wartosc  1
klucz  min  ma wartosc  1
klucz  morskich[8].  ma wartosc  1
klucz  przebieg  ma wartosc  1
klucz  osobny  ma wartosc  6
klucz  artykuł:  ma wartosc  6
klucz  (1921).  ma wartosc  2
klucz  stępkę  ma wartosc  4
klucz  położono  ma wartosc  4
klucz  9  ma wartosc  1
klucz  września  ma wartosc  6
klucz  1920  ma wartosc  3
klucz  stoczni  ma wartosc  7
klucz  sasebo,  ma wartosc  1
klucz  zwodowano  ma wartosc  3
klucz  kwietnia  ma wartosc  4
klucz  1921  ma wartosc  5
klucz  roku.  ma wartosc  9
klucz  wcielenie  ma wartosc  1
klucz  miało  ma wartosc  3
klucz  1922  ma wartosc  7
klucz  brał  ma wartosc  5
klucz  udział  ma wartosc  6
klucz  wojnie  ma wartosc  4
klucz  chińsko-japońskiej,  ma wartosc  2
klucz  następnie  ma wartosc  1
klucz  walkach  ma wartosc  1
klucz  wojny  ma wartosc  2
klucz  światowej  ma wartosc  1
klucz  pacyfiku,  ma wartosc  1
klucz  bitwie  ma wartosc  4
klucz  midway  ma wartosc  1
klucz  bitwach  ma wartosc  1
klucz  guadalcanalem.  ma wartosc  1
klucz  flagowego.  ma wartosc  2
klucz  okresie  ma wartosc  7
klucz  międzywojennym  ma wartosc  5
klucz  operował  ma wartosc  8
klucz  głownie  ma wartosc  1
klucz  wodach  ma wartosc  5
klucz  morza  ma wartosc  1
klucz  południowochińskiego.  ma wartosc  1
klucz  odbywał  ma wartosc  1
klucz  wiele  ma wartosc  1
klucz  rejsów  ma wartosc  1
klucz  ćwiczebnych,  ma wartosc  1
klucz  będąc  ma wartosc  1
klucz  kilkukrotnie  ma wartosc  4
klucz  kierowany  ma wartosc  1
klucz  rezerwy  ma wartosc  2
klucz  modernizowany.  ma wartosc  3
klucz  lipca  ma wartosc  1
klucz  1937  ma wartosc  2
klucz  konfliktu  ma wartosc  1
klucz  chińsko-japońskiego  ma wartosc  1
klucz  wraz  ma wartosc  10
klucz  grupą  ma wartosc  2
klucz  niszczycieli  ma wartosc  3
klucz  patrolował  ma wartosc  2
klucz  morzu  ma wartosc  2
klucz  południowochińskim  ma wartosc  1
klucz  wspierał  ma wartosc  3
klucz  desant  ma wartosc  5
klucz  miasta  ma wartosc  1
klucz  kanton[14].  ma wartosc  1
klucz  listopadzie  ma wartosc  3
klucz  1939  ma wartosc  1
klucz  powrócił  ma wartosc  1
klucz  portu  ma wartosc  1
klucz  sasebo.  ma wartosc  2
klucz  kwietniu  ma wartosc  3
klucz  1940  ma wartosc  2
klucz  przekierowany  ma wartosc  1
klucz  maizuru[14].  ma wartosc  1
klucz  czerwca  ma wartosc  1
klucz  1941  ma wartosc  8
klucz  jednostka  ma wartosc  6
klucz  operowała  ma wartosc  1
klucz  składzie  ma wartosc  2
klucz  sentai  ma wartosc  2
klucz  15[14].  ma wartosc  1
klucz  listopada  ma wartosc  4
klucz  bazował  ma wartosc  3
klucz  palau,  ma wartosc  1
klucz  wydzielony  ma wartosc  1
klucz  grupy  ma wartosc  2
klucz  mającej  ma wartosc  1
klucz  zaatakować  ma wartosc  1
klucz  filipiny.  ma wartosc  1
klucz  grudnia  ma wartosc  5
klucz  wyruszył  ma wartosc  2
klucz  grupie  ma wartosc  1
klucz  składającej  ma wartosc  1
klucz  siedmiu  ma wartosc  1
klucz  statków  ma wartosc  1
klucz  transportowych[14].  ma wartosc  1
klucz  dniach  ma wartosc  1
klucz  12–13  ma wartosc  1
klucz  osłaniał  ma wartosc  7
klucz  pancerniki  ma wartosc  2
klucz  „hiei”  ma wartosc  1
klucz  „kirishima”  ma wartosc  1
klucz  bitwy  ma wartosc  2
klucz  guadalcanalem[4].  ma wartosc  1
klucz  nocnego  ma wartosc  1
klucz  starcia  ma wartosc  1
klucz  krążownikiem  ma wartosc  1
klucz  uss  ma wartosc  3
klucz  „san  ma wartosc  1
klucz  francisco”  ma wartosc  1
klucz  (ca-38)  ma wartosc  1
klucz  japoński  ma wartosc  1
klucz  doznał  ma wartosc  1
klucz  lekkich  ma wartosc  1
klucz  uszkodzeń[4].  ma wartosc  1
klucz  guadalcanalem,  ma wartosc  1
klucz  niszczycielami  ma wartosc  3
klucz  walczył  ma wartosc  1
klucz  pancerników  ma wartosc  1
klucz  kadm.  ma wartosc  1
klucz  willisa  ma wartosc  1
klucz  augustusa  ma wartosc  1
klucz  lee[4].  ma wartosc  1
klucz  1943  ma wartosc  7
klucz  u  ma wartosc  3
klucz  wybrzeży  ma wartosc  3
klucz  nowej  ma wartosc  1
klucz  irlandii,  ma wartosc  1
klucz  uszkodzony.  ma wartosc  1
klucz  zatopiony  ma wartosc  4
klucz  amerykański  ma wartosc  2
klucz  podwodny  ma wartosc  2
klucz  7  ma wartosc  3
klucz  sierpnia  ma wartosc  4
klucz  roku[15].  ma wartosc  1
klucz  isuzu  ma wartosc  2
klucz  „isuzu”  ma wartosc  5
klucz  (1944)  ma wartosc  1
klucz  uraga  ma wartosc  2
klucz  dock  ma wartosc  2
klucz  co.,  ma wartosc  1
klucz  29  ma wartosc  2
klucz  października  ma wartosc  7
klucz  wprowadzenie  ma wartosc  1
klucz  15  ma wartosc  4
klucz  1923  ma wartosc  3
klucz  innymi  ma wartosc  2
klucz  chin,  ma wartosc  1
klucz  funkcje  ma wartosc  1
klucz  flagowego  ma wartosc  1
klucz  szkolnego.  ma wartosc  1
klucz  1931–1935  ma wartosc  1
klucz  przechodził  ma wartosc  1
klucz  kilka  ma wartosc  1
klucz  modernizacji.  ma wartosc  1
klucz  grudniu  ma wartosc  1
klucz  styczniu  ma wartosc  4
klucz  stacjonował  ma wartosc  1
klucz  hongkongu[15].  ma wartosc  1
klucz  prowadził  ma wartosc  1
klucz  patrole  ma wartosc  1
klucz  jawajskim[15].  ma wartosc  1
klucz  atolu  ma wartosc  1
klucz  truk.  ma wartosc  1
klucz  siedmioma  ma wartosc  1
klucz  „kongō”  ma wartosc  1
klucz  „haruna”,  ma wartosc  1
klucz  bombardowanie  ma wartosc  1
klucz  lotniska  ma wartosc  1
klucz  henderson  ma wartosc  2
klucz  field  ma wartosc  2
klucz  guadalcanalu  ma wartosc  2
klucz  ciężkie  ma wartosc  1
klucz  „maya”  ma wartosc  1
klucz  „myōkō”[15].  ma wartosc  1
klucz  wziął  ma wartosc  1
klucz  koło  ma wartosc  1
klucz  wysp  ma wartosc  2
klucz  santa  ma wartosc  1
klucz  cruz[16].  ma wartosc  1
klucz  pierwszą  ma wartosc  1
klucz  połowę  ma wartosc  1
klucz  przeszedł  ma wartosc  3
klucz  pierwszą,  ma wartosc  1
klucz  głębszą  ma wartosc  1
klucz  początku  ma wartosc  1
klucz  wojny,  ma wartosc  1
klucz  polegającej  ma wartosc  1
klucz  m.in.  ma wartosc  1
klucz  montażu  ma wartosc  1
klucz  podwójnej  ma wartosc  1
klucz  wzmocnieniu  ma wartosc  1
klucz  obrony  ma wartosc  1
klucz  przeciwlotniczej.  ma wartosc  1
klucz  majem  ma wartosc  1
klucz  wrześniem  ma wartosc  1
klucz  roku,  ma wartosc  6
klucz  przebudowany  ma wartosc  1
klucz  przeciwlotniczy.  ma wartosc  1
klucz  ataku  ma wartosc  6
klucz  torpedowego  ma wartosc  2
klucz  amerykańskich  ma wartosc  1
klucz  podwodnych  ma wartosc  1
klucz  1945  ma wartosc  1
klucz  wyspy  ma wartosc  4
klucz  sumbawy[17].  ma wartosc  1
klucz  natori  ma wartosc  2
klucz  (1922).  ma wartosc  2
klucz  położenie  ma wartosc  1
klucz  stępki  ma wartosc  1
klucz  odbyło  ma wartosc  1
klucz  mitsubishi-nagasaki.  ma wartosc  2
klucz  wszedł  ma wartosc  5
klucz  dai-nippon  ma wartosc  3
klucz  teikoku  ma wartosc  3
klucz  kaigun  ma wartosc  3
klucz  resztę  ma wartosc  1
klucz  okresu  ma wartosc  2
klucz  międzywojennego  ma wartosc  2
klucz  pełniła  ma wartosc  2
klucz  odbywała  ma wartosc  2
klucz  rejsy  ma wartosc  2
klucz  chińskich.  ma wartosc  2
klucz  modernizowana.  ma wartosc  1
klucz  czerwcu  ma wartosc  1
klucz  rejonie  ma wartosc  3
klucz  szanghaju.  ma wartosc  1
klucz  samego  ma wartosc  2
klucz  hangzhou[17].  ma wartosc  1
klucz  lutym  ma wartosc  1
klucz  sajgonie  ma wartosc  1
klucz  (obecnym  ma wartosc  1
klucz  ho  ma wartosc  1
klucz  chi  ma wartosc  1
klucz  minh).  ma wartosc  1
klucz  siłami  ma wartosc  1
klucz  5.  ma wartosc  2
klucz  fn  ma wartosc  2
klucz  floty  ma wartosc  1
klucz  bazującej  ma wartosc  1
klucz  tajwanie[17].  ma wartosc  1
klucz  lipcu  ma wartosc  1
klucz  sierpniu  ma wartosc  1
klucz  uczestniczył  ma wartosc  1
klucz  zajęciu  ma wartosc  1
klucz  indochin  ma wartosc  1
klucz  francuskich[17].  ma wartosc  1
klucz  nocy  ma wartosc  1
klucz  1  ma wartosc  3
klucz  marca  ma wartosc  5
klucz  eskortujący  ma wartosc  1
klucz  inwazyjne  ma wartosc  1
klucz  stoczył  ma wartosc  1
klucz  walkę  ma wartosc  1
klucz  alianckimi  ma wartosc  1
klucz  krążownikami  ma wartosc  2
klucz  „houston”  ma wartosc  1
klucz  (ca-30)  ma wartosc  1
klucz  hmas  ma wartosc  1
klucz  „perth”[18].  ma wartosc  1
klucz  zaatakowany  ma wartosc  1
klucz  „tautog”  ma wartosc  1
klucz  (ss-199).  ma wartosc  1
klucz  wystrzelone  ma wartosc  1
klucz  torpedy  ma wartosc  1
klucz  trafiły  ma wartosc  1
klucz  rufę  ma wartosc  1
klucz  krążownika.  ma wartosc  1
klucz  eksplozja  ma wartosc  1
klucz  spowodowała  ma wartosc  1
klucz  oderwanie  ma wartosc  1
klucz  reszty  ma wartosc  1
klucz  20-metrowej  ma wartosc  1
klucz  rufy[18].  ma wartosc  1
klucz  krytycznie  ma wartosc  1
klucz  uszkodzona  ma wartosc  1
klucz  trudem  ma wartosc  1
klucz  dotarła  ma wartosc  1
klucz  zatoki  ma wartosc  2
klucz  ambon[18].  ma wartosc  1
klucz  przełomie  ma wartosc  2
klucz  głęboką  ma wartosc  1
klucz  modernizację.  ma wartosc  1
klucz  amerykańskiego  ma wartosc  2
klucz  podwodnego  ma wartosc  1
klucz  pobliżu  ma wartosc  3
klucz  ujścia  ma wartosc  1
klucz  cieśniny  ma wartosc  1
klucz  san  ma wartosc  1
klucz  bernardino[18].  ma wartosc  1
klucz  yura  ma wartosc  2
klucz  maja  ma wartosc  6
klucz  wodowany  ma wartosc  1
klucz  lutego  ma wartosc  3
klucz  incydentu  ma wartosc  1
klucz  szanghajskiego,  ma wartosc  1
klucz  artyleryjskim  ma wartosc  1
klucz  działania  ma wartosc  1
klucz  lądzie[18].  ma wartosc  1
klucz  japońsko-chińskiej  ma wartosc  1
klucz  rejon  ma wartosc  1
klucz  qingdao[18].  ma wartosc  1
klucz  okrętem  ma wartosc  1
klucz  flagowym  ma wartosc  1
klucz  podwodnych,  ma wartosc  1
klucz  operując  ma wartosc  1
klucz  karolinów,  ma wartosc  1
klucz  marshalla  ma wartosc  1
klucz  marianów  ma wartosc  1
klucz  miesiącach  ma wartosc  1
klucz  września[18].  ma wartosc  1
klucz  ciężkimi  ma wartosc  1
klucz  „kumano”  ma wartosc  1
klucz  „suzuya”  ma wartosc  1
klucz  lądowanie  ma wartosc  2
klucz  endau[19].  ma wartosc  1
klucz  październiku  ma wartosc  2
klucz  wsparcia  ma wartosc  1
klucz  walk  ma wartosc  1
klucz  lotnisko  ma wartosc  1
klucz  24  ma wartosc  2
klucz  uderzeniowej  ma wartosc  1
klucz  opuścił  ma wartosc  1
klucz  shortland[20].  ma wartosc  1
klucz  grupa  ma wartosc  1
klucz  zaatakowana  ma wartosc  1
klucz  bombowce  ma wartosc  1
klucz  horyzontalne  ma wartosc  1
klucz  nurkujące.  ma wartosc  1
klucz  trafiona  ma wartosc  2
klucz  bombami  ma wartosc  1
klucz  okolice  ma wartosc  1
klucz  rufy[19].  ma wartosc  1
klucz  około  ma wartosc  1
klucz  godziny  ma wartosc  1
klucz  15:00  ma wartosc  1
klucz  nastąpił  ma wartosc  1
klucz  atak,  ma wartosc  1
klucz  którego  ma wartosc  1
klucz  kolejnymi  ma wartosc  1
klucz  bombami,  ma wartosc  1
klucz  spowodowało  ma wartosc  1
klucz  liczne  ma wartosc  1
klucz  pożary[19].  ma wartosc  1
klucz  opuściła  ma wartosc  1
klucz  przeszła  ma wartosc  1
klucz  niszczyciela  ma wartosc  1
klucz  „murasame”,  ma wartosc  1
klucz  niszczyciele:  ma wartosc  1
klucz  „yūdachi”  ma wartosc  1
klucz  „harusame”  ma wartosc  1
klucz  dobiły  ma wartosc  1
klucz  opuszczony  ma wartosc  1
klucz  krążownik[19].  ma wartosc  1
klucz  kinu  ma wartosc  1
klucz  kinu.  ma wartosc  1
klucz  stycznia  ma wartosc  1
klucz  zwodowany  ma wartosc  2
klucz  głównie  ma wartosc  2
klucz  chińskich,  ma wartosc  2
klucz  chińsko-japońskiej.  ma wartosc  1
klucz  malaje.  ma wartosc  1
klucz  wspierała  ma wartosc  1
klucz  miri  ma wartosc  1
klucz  sarawaku,  ma wartosc  1
klucz  kuching[21].  ma wartosc  1
klucz  we  ma wartosc  1
klucz  wrześniu  ma wartosc  1
klucz  bliźniaczym  ma wartosc  1
klucz  statki  ma wartosc  2
klucz  desantem  ma wartosc  1
klucz  salomona.  ma wartosc  1
klucz  wysadził  ma wartosc  1
klucz  wyspie  ma wartosc  1
klucz  shortland,  ma wartosc  1
klucz  moluków[21].  ma wartosc  1
klucz  głęboką,  ma wartosc  1
klucz  wojenną  ma wartosc  1
klucz  modernizacje  ma wartosc  1
klucz  podobnie  ma wartosc  1
klucz  serii,  ma wartosc  1
klucz  „yury”.  ma wartosc  1
klucz  zatoce  ma wartosc  2
klucz  leyte.  ma wartosc  1
klucz  26  ma wartosc  4
klucz  ormoc[21].  ma wartosc  1
klucz  abukuma  ma wartosc  2
klucz  (1923).  ma wartosc  1
klucz  stępka  ma wartosc  1
klucz  budowę  ma wartosc  1
klucz  położona  ma wartosc  1
klucz  co.  ma wartosc  1
klucz  cesarskiej  ma wartosc  1
klucz  marynarce  ma wartosc  1
klucz  1925  ma wartosc  1
klucz  budowa  ma wartosc  1
klucz  uległa  ma wartosc  1
klucz  opóźnieniu  ma wartosc  1
klucz  powodu  ma wartosc  2
klucz  zniszczeń  ma wartosc  1
klucz  trzęsienia  ma wartosc  1
klucz  ziemi,  ma wartosc  1
klucz  ostatecznie  ma wartosc  1
klucz  budowano  ma wartosc  1
klucz  3,5  ma wartosc  1
klucz  roku[19].  ma wartosc  1
klucz  japońsko-chińskiej.  ma wartosc  1
klucz  tamtym  ma wartosc  1
klucz  modernizowano  ma wartosc  1
klucz  flotyllą  ma wartosc  1
klucz  niszczycieli,  ma wartosc  1
klucz  wyszedł  ma wartosc  1
klucz  flotą  ma wartosc  1
klucz  admirała  ma wartosc  1
klucz  nagumo  ma wartosc  1
klucz  pearl  ma wartosc  1
klucz  harbor[19].  ma wartosc  1
klucz  inwazji  ma wartosc  1
klucz  jawę  ma wartosc  1
klucz  ośmioma  ma wartosc  1
klucz  przechwytywał  ma wartosc  1
klucz  płynące  ma wartosc  1
klucz  jawą  ma wartosc  1
klucz  australią[19].  ma wartosc  1
klucz  połowie  ma wartosc  1
klucz  włączono  ma wartosc  1
klucz  1.  ma wartosc  1
klucz  zespołu  ma wartosc  1
klucz  regionu  ma wartosc  1
klucz  północnego,  ma wartosc  1
klucz  zadanie  ma wartosc  1
klucz  przejąć  ma wartosc  1
klucz  aleuty[22].  ma wartosc  1
klucz  jako  ma wartosc  1
klucz  część  ma wartosc  1
klucz  eskorty  ma wartosc  1
klucz  adak.  ma wartosc  1
klucz  trakcie  ma wartosc  1
klucz  rejsu  ma wartosc  1
klucz  odwołano  ma wartosc  1
klucz  operację  ma wartosc  1
klucz  niepowodzenia  ma wartosc  1
klucz  midway.  ma wartosc  1
klucz  attu,  ma wartosc  1
klucz  wylądowała  ma wartosc  1
klucz  czerwca.  ma wartosc  1
klucz  pozostawały  ma wartosc  1
klucz  rejonie,  ma wartosc  1
klucz  patrolując  ma wartosc  1
klucz  go  ma wartosc  1
klucz  połowy  ma wartosc  1
klucz  czerwca[23].  ma wartosc  1
klucz  kiska.  ma wartosc  1
klucz  jednostkę  ma wartosc  1
klucz  zmodernizowano  ma wartosc  1
klucz  wzór  ma wartosc  1
klucz  nagara.  ma wartosc  1
klucz  uczestniczyła  ma wartosc  1
klucz  leyte,  ma wartosc  1
klucz  zatopiona[23].  ma wartosc  1
w  wystpuje  128  razy
[('w', 128), ('na', 65), ('roku', 44), ('okręt', 39), ('i', 37), ('oraz', 35), ('z', 33), ('się', 28), ('do', 26), ('mm', 18), ('o', 16), ('kal.', 16), ('od', 15), ('typu', 14), ('krążownik', 14), ('po', 13), ('okręty', 12), ('podczas', 12), ('dwa', 12), ('a', 11), ('przez', 11), ('jednostki', 10), ('dla', 10), ('1942', 10), ('wraz', 10), ('1944', 9), ('za', 9), ('pod', 9), ('został', 9), ('były', 9), ('służby', 9), ('roku.', 9), ('zaś', 8), ('latach', 8), ('dział', 8), ('kalibru', 8), ('operował', 8), ('1941', 8), ('okrętów', 7), ('m', 7), ('miały', 7), ('okrętu', 7), ('pokład', 7), ('działa', 7), ('została', 7), ('krążowniki', 7), ('stoczni', 7), ('1922', 7), ('okresie', 7), ('osłaniał', 7), ('1943', 7), ('października', 7), ('grubości', 6), ('mm,', 6), ('znajdowały', 6), ('funkcję', 6), ('było', 6), ('gdzie', 6), ('tym', 6), ('dodatkowo', 6), ('uzbrojenie', 6), ('wielokrotnie', 6), ('25', 6), ('osobny', 6), ('artykuł:', 6), ('września', 6), ('udział', 6), ('jednostka', 6), ('roku,', 6), ('ataku', 6), ('maja', 6), ('wynosiła', 5), ('wyniku', 5), ('kotłowni', 5), ('części', 5), ('znajdował', 5), ('ulokowano', 5), ('miejsce', 5), ('pełnił', 5), ('to', 5), ('dwóch', 5), ('10', 5), ('16', 5), ('kotły', 5), ('zapas', 5), ('tego', 5), ('wynosił', 5), ('„kinu”', 5), ('zamontowano', 5), ('typ', 5), ('była', 5), ('armaty', 5), ('8', 5), ('1921', 5), ('brał', 5), ('międzywojennym', 5), ('wodach', 5), ('desant', 5), ('grudnia', 5), ('„isuzu”', 5), ('wszedł', 5), ('marca', 5), ('kadłub', 4), ('krążowników', 4), ('długości', 4), ('natomiast', 4), ('kadłuba', 4), ('–', 4), ('przed', 4), ('pokładem', 4), ('pomieszczenia', 4), ('był', 4), ('mm[2].', 4), ('140', 4), ('pośrednictwem', 4), ('paliwem', 4), ('cztery', 4), ('opalane', 4), ('przy', 4), ('prędkości', 4), ('14', 4), ('wynoszącej', 4), ('„abukuma”', 4), ('„isuzu”,', 4), ('pozostałe', 4), ('te', 4), ('„yura”', 4), ('13,2', 4), ('zastąpiono', 4), ('torped', 4), ('stępkę', 4), ('położono', 4), ('kwietnia', 4), ('wojnie', 4), ('bitwie', 4), ('kilkukrotnie', 4), ('listopada', 4), ('zatopiony', 4), ('sierpnia', 4), ('15', 4), ('styczniu', 4), ('wyspy', 4), ('26', 4), ('nagara', 3), ('miał', 3), ('długość', 3), ('trzy', 3), ('drugi', 3), ('dziobowej', 3), ('znajdowała', 3), ('czterech', 3), ('pomieszczenie', 3), ('oprócz', 3), ('stanowisko', 3), ('przypadku', 3), ('27', 3), ('5', 3), ('układ', 3), ('mm.', 3), ('zamontowane', 3), ('głównych', 3), ('one', 3), ('masie', 3), ('je', 3), ('maksymalną', 3), ('startową', 3), ('jeden', 3), ('okolicach', 3), ('maszcie', 3), ('13', 3), ('krążownikach', 3), ('radar', 3), ('21', 3), ('przebudowie', 3), ('przeciwlotniczy', 3), ('pomiędzy', 3), ('2', 3), ('3', 3), ('maksymalnej', 3), ('flagowej', 3), ('89', 3), ('127', 3), ('armat', 3), ('przeciwlotnicze', 3), ('76,2', 3), ('działo', 3), ('umiejscowiono', 3), ('numer', 3), ('skierowano', 3), ('6', 3), ('17', 3), ('dysponowały', 3), ('dwiema', 3), ('między', 3), ('karabiny', 3), ('karabinów', 3), ('dwoma', 3), ('czasie', 3), ('×', 3), ('ii', 3), ('20', 3), ('1920', 3), ('zwodowano', 3), ('miało', 3), ('modernizowany.', 3), ('niszczycieli', 3), ('wspierał', 3), ('listopadzie', 3), ('kwietniu', 3), ('bazował', 3), ('uss', 3), ('niszczycielami', 3), ('u', 3), ('wybrzeży', 3), ('7', 3), ('1923', 3), ('przeszedł', 3), ('dai-nippon', 3), ('teikoku', 3), ('kaigun', 3), ('rejonie', 3), ('1', 3), ('pobliżu', 3), ('lutego', 3), ('opis', 2), ('wojennej', 2), ('schemat', 2), ('m,', 2), ('wynosiło', 2), ('wyporność', 2), ('standardowa', 2), ('płyt', 2), ('25,4', 2), ('płyty', 2), ('grubość', 2), ('przedziałem', 2), ('ostatni', 2), ('jednostek', 2), ('śródokręciu', 2), ('kabiny', 2), ('nadbudówce', 2), ('pokładzie', 2), ('śródokręciu,', 2), ('także', 2), ('kabinę', 2), ('którą', 2), ('znajdowało', 2), ('lornety', 2), ('początkowo', 2), ('jednak', 2), ('1931–1934,', 2), ('on', 2), ('jego', 2), ('flotylli', 2), ('załoga', 2), ('osób,', 2), ('opancerzenie', 2), ('praktycznie', 2), ('jak', 2), ('pas', 2), ('ostrzałem', 2), ('ten', 2), ('ze', 2), ('której', 2), ('płytami', 2), ('pancernymi', 2), ('wcześniej', 2), ('zostały', 2), ('napędowy', 2), ('napędzane', 2), ('turbin', 2), ('skład', 2), ('turbina', 2), ('zespół', 2), ('swoją', 2), ('trzeciej', 2), ('generowały', 2), ('zabierały', 2), ('ton', 2), ('modernizację', 2), ('okrętach', 2), ('trzech', 2), ('wynoszącą', 2), ('000', 2), ('co', 2), ('zasięg', 2), ('23', 2), ('zapewniały', 2), ('mocy', 2), ('widoczną', 2), ('dziobową', 2), ('platformą', 2), ('wodnosamolotów', 2), ('rok)', 2), ('obrotową', 2), ('rufie', 2), ('wyposażono', 2), ('większość', 2), ('platformę', 2), ('zatopionej', 2), ('ostrzegania', 2), ('powietrznego', 2), ('trzema', 2), ('ta', 2), ('„nagarze”,', 2), ('„yurze”', 2), ('pozostałych', 2), ('1934–1935[6].', 2), ('1932', 2), ('1934', 2), ('zyskały', 2), ('nakajima', 2), ('stanie', 2), ('lub', 2), ('momencie', 2), ('wejścia', 2), ('układzie', 2), ('lufy', 2), ('bokach', 2), ('szybkostrzelność', 2), ('strzałów', 2), ('maksymalny', 2), ('sztuk,', 2), ('38', 2), ('armatami', 2), ('„nagara”', 2), ('składało', 2), ('pojedynczych', 2), ('18', 2), ('6,5', 2), ('lotnictwa', 2), ('maszynowych', 2), ('dwie', 2), ('podwójnymi', 2), ('stanowiskami', 2), ('które', 2), ('późniejszym', 2), ('mm[6].', 2), ('artyleryjskie', 2), ('podwójne', 2), ('22', 2), ('łącznie', 2), ('610', 2), ('wyrzutnie', 2), ('który', 2), ('węzłów[13].', 2), ('(1921).', 2), ('chińsko-japońskiej,', 2), ('wojny', 2), ('flagowego.', 2), ('rezerwy', 2), ('1937', 2), ('grupą', 2), ('patrolował', 2), ('morzu', 2), ('sasebo.', 2), ('1940', 2), ('składzie', 2), ('sentai', 2), ('grupy', 2), ('wyruszył', 2), ('pancerniki', 2), ('bitwy', 2), ('amerykański', 2), ('podwodny', 2), ('isuzu', 2), ('uraga', 2), ('dock', 2), ('29', 2), ('innymi', 2), ('henderson', 2), ('field', 2), ('guadalcanalu', 2), ('wysp', 2), ('torpedowego', 2), ('natori', 2), ('(1922).', 2), ('mitsubishi-nagasaki.', 2), ('okresu', 2), ('międzywojennego', 2), ('pełniła', 2), ('odbywała', 2), ('rejsy', 2), ('chińskich.', 2), ('samego', 2), ('5.', 2), ('fn', 2), ('krążownikami', 2), ('zatoki', 2), ('przełomie', 2), ('amerykańskiego', 2), ('yura', 2), ('lądowanie', 2), ('październiku', 2), ('24', 2), ('trafiona', 2), ('zwodowany', 2), ('głównie', 2), ('chińskich,', 2), ('statki', 2), ('zatoce', 2), ('abukuma', 2), ('powodu', 2), ('konstrukcji', 1), ('ogólny', 1), ('sylwetka', 1), ('sprzed', 1), ('przebudowy', 1), ('(poniżej', 1), ('kątów', 1), ('ostrzału', 1), ('artylerii', 1), ('opancerzenia)', 1), ('162,15', 1), ('całkowitej,', 1), ('linii', 1), ('wodnej', 1), ('156,65', 1), ('m[2].', 1), ('szerokość', 1), ('14,17', 1), ('jej', 1), ('zanurzenie', 1), ('4,85', 1), ('m[3][2].', 1), ('5170', 1), ('ts,', 1), ('normalna', 1), ('5690', 1), ('ts.', 1), ('modernizacji', 1), ('wzrosła', 1), ('6050', 1), ('ts[4].', 1), ('zewnętrzny', 1), ('wykonano', 1), ('stalowych', 1), ('19', 1), ('stanowiące', 1), ('wewnętrzne', 1), ('elementy', 1), ('6,4', 1), ('12,7', 1), ('mm[5].', 1), ('grubsze', 1), ('kluczowych', 1), ('żywotności', 1), ('miejscach[5].', 1), ('pokłady:', 1), ('główny,', 1), ('ciągnący', 1), ('całą', 1), ('jednostki,', 1), ('znajdujący', 1), ('maszynowni', 1), ('rufowej[5].', 1), ('poniżej', 1), ('pełniący', 1), ('ładowni[5].', 1), ('śródokręcie', 1), ('podwyższone', 1), ('przykryte', 1), ('łodziowym[5].', 1), ('załogi,', 1), ('kambuz,', 1), ('instalacje', 1), ('sanitariatu', 1), ('magazyny.', 1), ('rufowej', 1), ('oficerów,', 1), ('umywalnie', 1), ('dalsze', 1), ('magazynowe[5].', 1), ('załogi', 1), ('głównym', 1), ('kotłowniami', 1), ('łodziowym.', 1), ('podoficerowie', 1), ('zajmowali', 1), ('miejsca', 1), ('kabinami', 1), ('oficerskimi[6].', 1), ('wysoka', 1), ('dziobówka.', 1), ('składała', 1), ('poziomów,', 1), ('pierwszym', 1), ('nich', 1), ('radiową,', 1), ('nad', 1), ('nakresowe', 1), ('operacyjne[7].', 1), ('wyżej', 1), ('kompasowy,', 1), ('którym', 1), ('kompasów', 1), ('dalmierze,', 1), ('dalocelownik[7].', 1), ('nadbudówki,', 1), ('tuż', 1), ('kompasowym', 1), ('dowodzenia[7].', 1), ('hangar', 1), ('wodnosamolotu,', 1), ('modernizacji,', 1), ('która', 1), ('zależności', 1), ('odbyła', 1), ('zlikwidowany', 1), ('utworzono', 1), ('łączności,', 1), ('sztabu', 1), ('dowództwa', 1), ('powiększono', 1), ('centrum', 1), ('bojowe[6].', 1), ('liczyła', 1), ('bazowo', 1), ('450', 1), ('37', 1), ('oficerów.', 1), ('jeśli', 1), ('flagowego,', 1), ('zaokrętowanych', 1), ('nim', 1), ('dodatkowych', 1), ('oficerów[6].', 1), ('zastosowany', 1), ('opancerzenia', 1), ('taki', 1), ('sam', 1), ('projektu', 1), ('kuma[2].', 1), ('pancerny', 1), ('63,5', 1), ('łączący', 1), ('górnym,', 1), ('73,17', 1), ('wysokości', 1), ('4,87', 1), ('czego', 1), ('0,84', 1), ('wodą[2].', 1), ('rozwiązanie', 1), ('zapewniało', 1), ('ochronę', 1), ('102', 1), ('obu', 1), ('stronach', 1), ('burt', 1), ('chronił', 1), ('maszynowni.', 1), ('wykonany', 1), ('stali', 1), ('wysokiej', 1), ('odporności', 1), ('rozciąganie', 1), ('składał', 1), ('warstw', 1), ('pancernych:', 1), ('warstwy', 1), ('zewnętrznej', 1), ('liczącej', 1), ('38,1', 1), ('wewnętrznej,', 1), ('główny', 1), ('pokryto', 1), ('28,5', 1), ('główne', 1), ('osłonięto', 1), ('maskami', 1), ('komory', 1), ('amunicyjne', 1), ('opancerzone', 1), ('32', 1), ('podajników', 1), ('amunicyjnych', 1), ('zespołów', 1), ('parowych', 1), ('parsonsa,', 1), ('których', 1), ('wchodziła', 1), ('wysokociśnieniowa', 1), ('gihon', 1), ('reakcyjna', 1), ('niskociśnieniowa', 1), ('mitsubishi-parsons[5].', 1), ('każdy', 1), ('własnej', 1), ('przekładni', 1), ('redukcyjnej', 1), ('napędzał', 1), ('linię', 1), ('wału', 1), ('napędowego,', 1), ('zakończoną', 1), ('pojedynczą,', 1), ('trójpłatową', 1), ('śrubą', 1), ('napędową[5].', 1), ('turbiny', 1), ('zasilane', 1), ('dwunastu', 1), ('kotłów', 1), ('opalanych', 1), ('płynnym[a]', 1), ('węglem[5].', 1), ('kotłowni,', 1), ('pierwszej', 1), ('strony', 1), ('dziobu', 1), ('małe', 1), ('olejowym', 1), ('węglem,', 1), ('drugiej', 1), ('ropą[5].', 1), ('zajmowane', 1), ('ropę,', 1), ('ostatniej,', 1), ('czwartej', 1), ('również', 1), ('ciekłym[5].', 1), ('parę', 1), ('ciśnieniu', 1), ('wynoszącym', 1), ('18,3', 1), ('kgf/cm²[5].', 1), ('paliwa', 1), ('płynnego', 1), ('1284', 1), ('350', 1), ('węgla[5].', 1), ('węglem', 1), ('zmodernizowane', 1), ('czasu', 1), ('opalano', 1), ('wyłącznie', 1), ('płynnym.', 1), ('siłowni', 1), ('poszczególnych', 1), ('przeprowadzono', 1), ('1934–1938[6].', 1), ('spaliny', 1), ('odprowadzane', 1), ('kominów', 1), ('śródokręciu[7].', 1), ('generował', 1), ('moc', 1), ('90', 1), ('km,', 1), ('pozwalało', 1), ('osiągnąć', 1), ('krążownikom', 1), ('prędkość', 1), ('prawie', 1), ('36', 1), ('węzłów[7].', 1), ('8500', 1), ('węzłów,', 1), ('6000', 1), ('węzłach', 1), ('1000', 1), ('węzły[7].', 1), ('energię', 1), ('elektryczną', 1), ('spalinowe', 1), ('generatory', 1), ('prądu', 1), ('stałego', 1), ('odpowiednio', 1), ('66', 1), ('88', 1), ('kw.', 1), ('napięcie', 1), ('110', 1), ('v.', 1), ('zainstalowano', 1), ('przedziale', 1), ('maszynowni[7].', 1), ('wyposażenie', 1), ('(1931', 1), ('wodnosamolotem', 1), ('(1941', 1), ('dalocelowniki,', 1), ('kompasy.', 1), ('wyposażenia', 1), ('kompasowym[8].', 1), ('maszty[8].', 1), ('dziobówką,', 1), ('rufy[8].', 1), ('dziobowym', 1), ('dalocelownik', 1), ('służący', 1), ('kierowania', 1), ('ogniem', 1), ('artyleryjskim,', 1), ('dowodzenia', 1), ('artylerią', 1), ('reflektory[8].', 1), ('1924–1925', 1), ('prac', 1), ('prowadzonych', 1), ('typu,', 1), ('zyskał', 1), ('dodatkową', 1), ('obserwacyjną', 1), ('określania', 1), ('celów[8].', 1), ('rufowym', 1), ('reflektor[8].', 1), ('okręty,', 1), ('„yury”,', 1), ('otrzymały', 1), ('nawodnego', 1), ('22.', 1), ('płaską,', 1), ('kwadratową', 1), ('antenę,', 1), ('trójnożnym', 1), ('dachu', 1), ('pomostu', 1), ('kompasowego.', 1), ('wypadku', 1), ('krążownika', 1), ('13.', 1), ('dysponował', 1), ('więc', 1), ('stacjami', 1), ('radiolokacyjnymi[9].', 1), ('wyposażone', 1), ('metrów', 1), ('samolotu', 1), ('myśliwskiego', 1), ('mitsubishi', 1), ('1mf.', 1), ('platforma', 1), ('usunięta', 1), ('„natori”', 1), ('„abukumie”', 1), ('rokiem', 1), ('katapultę', 1), ('kure', 1), ('model', 1), ('wodnosamolotu', 1), ('e4n.', 1), ('katapulta', 1), ('przyjąć', 1), ('wodnosamolot', 1), ('startowej', 1), ('tony[6].', 1), ('eksploatowały', 1), ('typy', 1), ('dwumiejscowe', 1), ('e8n', 1), ('trzymiejscowe', 1), ('kawanishi', 1), ('e7k.', 1), ('maszyn', 1), ('używany', 1), ('był,', 1), ('gdy', 1), ('rolę', 1), ('floty[10].', 1), ('armata', 1), ('uniwersalna', 1), ('zamontowana', 1), ('rufowych', 1), ('pierwotnie', 1), ('tę', 1), ('samą', 1), ('konfigurację', 1), ('uzbrojenia[11].', 1), ('linii,', 1), ('uzbrojono', 1), ('siedem', 1), ('okrętowych', 1), ('l/50', 1), ('mm[11].', 1), ('każde', 1), ('pojedynczym', 1), ('stanowisku', 1), ('ogniowym,', 1), ('osłonięte', 1), ('maski', 1), ('przeciwodłamkowe.', 1), ('umiejscowione', 1), ('dziobie,', 1), ('tandemu,', 1), ('skierowane', 1), ('inne', 1), ('strony.', 1), ('lufa', 1), ('skierowana', 1), ('kierunku', 1), ('dziobu,', 1), ('lufę', 1), ('nadbudówkę[11].', 1), ('nadbudówki', 1), ('jednym', 1), ('dziale', 1), ('(jedno', 1), ('każdą', 1), ('burtę)[11].', 1), ('wzdłuż', 1), ('płaszczyzny', 1), ('symetrii', 1), ('stanowiska', 1), ('ostatnim', 1), ('kominem', 1), ('ostatnie', 1), ('ulokowane', 1), ('rufie.', 1), ('minutę', 1), ('donośność', 1), ('500', 1), ('m[11].', 1), ('kąt', 1), ('podniesienia', 1), ('25°[11].', 1), ('pięciu', 1), ('przewidziano', 1), ('pocisków', 1), ('wynoszący', 1), ('120', 1), ('bocznych', 1), ('105', 1), ('sztuk[11].', 1), ('pociski', 1), ('ważyły', 1), ('kg', 1), ('wystrzeliwano', 1), ('pomocą', 1), ('ładunków', 1), ('miotających[11].', 1), ('salutacyjnymi.', 1), ('47', 1), ('kalibrze', 1), ('57', 1), ('mm[12].', 1), ('przezbrajane.', 1), ('ono', 1), ('przeciwlotniczych', 1), ('pierwszego', 1), ('komina.', 1), ('amunicji', 1), ('każdej', 1), ('240', 1), ('ona', 1), ('rozdzielnego', 1), ('ładowania[12].', 1), ('zwalczać', 1), ('cele', 1), ('odległości', 1), ('6500', 1), ('osiągać', 1), ('minutę[12].', 1), ('uzupełniały', 1), ('maszynowe', 1), ('drugim', 1), ('trzecim', 1), ('kominem.', 1), ('toku', 1), ('dalszej', 1), ('eksploatacji', 1), ('dynamicznego', 1), ('rozwoju', 1), ('szybko', 1), ('okazało', 1), ('być', 1), ('niewystarczające[12].', 1), ('1931–1934', 1), ('poczwórnych', 1), ('wielkokalibrowych', 1), ('hotchkiss', 1), ('platformie', 1), ('dziobówką[12].', 1), ('natori”', 1), ('poczwórny', 1), ('hotchkissa', 1), ('plot.', 1), ('93', 1), ('kolei', 1), ('karabinami', 1), ('maszynowymi', 1), ('lewis', 1), ('7,7', 1), ('stanowiło', 1), ('jedno', 1), ('uniwersalne', 1), ('89,', 1), ('wkm', 1), ('96', 1), ('iii,', 1), ('i[4].', 1), ('uniwersalnych', 1), ('50', 1), ('różnej', 1), ('konfiguracji[4].', 1), ('czterema', 1), ('wyrzutniami', 1), ('mm[13].', 1), ('poruszane', 1), ('zakresie', 1), ('360°', 1), ('silnik', 1), ('elektryczny', 1), ('km[13].', 1), ('pojedynczej', 1), ('wyrzutni', 1), ('8,8', 1), ('ważyła', 1), ('8,45', 1), ('tony.', 1), ('używano', 1), ('wówczas', 1), ('8,42', 1), ('głowicy', 1), ('bojowej', 1), ('346', 1), ('kg[13].', 1), ('czterocylindrowym', 1), ('silnikiem', 1), ('spalinowym,', 1), ('pozwalał', 1), ('osiągnięcie', 1), ('torpedom', 1), ('ich', 1), ('poczwórnymi', 1), ('92', 1), ('93.', 1), ('torped.', 1), ('zrzutnie', 1), ('bomb', 1), ('głębinowych[9]', 1), ('tory', 1), ('minowe', 1), ('48', 1), ('min', 1), ('morskich[8].', 1), ('przebieg', 1), ('9', 1), ('sasebo,', 1), ('wcielenie', 1), ('następnie', 1), ('walkach', 1), ('światowej', 1), ('pacyfiku,', 1), ('midway', 1), ('bitwach', 1), ('guadalcanalem.', 1), ('głownie', 1), ('morza', 1), ('południowochińskiego.', 1), ('odbywał', 1), ('wiele', 1), ('rejsów', 1), ('ćwiczebnych,', 1), ('będąc', 1), ('kierowany', 1), ('lipca', 1), ('konfliktu', 1), ('chińsko-japońskiego', 1), ('południowochińskim', 1), ('miasta', 1), ('kanton[14].', 1), ('1939', 1), ('powrócił', 1), ('portu', 1), ('przekierowany', 1), ('maizuru[14].', 1), ('czerwca', 1), ('operowała', 1), ('15[14].', 1), ('palau,', 1), ('wydzielony', 1), ('mającej', 1), ('zaatakować', 1), ('filipiny.', 1), ('grupie', 1), ('składającej', 1), ('siedmiu', 1), ('statków', 1), ('transportowych[14].', 1), ('dniach', 1), ('12–13', 1), ('„hiei”', 1), ('„kirishima”', 1), ('guadalcanalem[4].', 1), ('nocnego', 1), ('starcia', 1), ('krążownikiem', 1), ('„san', 1), ('francisco”', 1), ('(ca-38)', 1), ('japoński', 1), ('doznał', 1), ('lekkich', 1), ('uszkodzeń[4].', 1), ('guadalcanalem,', 1), ('walczył', 1), ('pancerników', 1), ('kadm.', 1), ('willisa', 1), ('augustusa', 1), ('lee[4].', 1), ('nowej', 1), ('irlandii,', 1), ('uszkodzony.', 1), ('roku[15].', 1), ('(1944)', 1), ('co.,', 1), ('wprowadzenie', 1), ('chin,', 1), ('funkcje', 1), ('flagowego', 1), ('szkolnego.', 1), ('1931–1935', 1), ('przechodził', 1), ('kilka', 1), ('modernizacji.', 1), ('grudniu', 1), ('stacjonował', 1), ('hongkongu[15].', 1), ('prowadził', 1), ('patrole', 1), ('jawajskim[15].', 1), ('atolu', 1), ('truk.', 1), ('siedmioma', 1), ('„kongō”', 1), ('„haruna”,', 1), ('bombardowanie', 1), ('lotniska', 1), ('ciężkie', 1), ('„maya”', 1), ('„myōkō”[15].', 1), ('wziął', 1), ('koło', 1), ('santa', 1), ('cruz[16].', 1), ('pierwszą', 1), ('połowę', 1), ('pierwszą,', 1), ('głębszą', 1), ('początku', 1), ('wojny,', 1), ('polegającej', 1), ('m.in.', 1), ('montażu', 1), ('podwójnej', 1), ('wzmocnieniu', 1), ('obrony', 1), ('przeciwlotniczej.', 1), ('majem', 1), ('wrześniem', 1), ('przebudowany', 1), ('przeciwlotniczy.', 1), ('amerykańskich', 1), ('podwodnych', 1), ('1945', 1), ('sumbawy[17].', 1), ('położenie', 1), ('stępki', 1), ('odbyło', 1), ('resztę', 1), ('modernizowana.', 1), ('czerwcu', 1), ('szanghaju.', 1), ('hangzhou[17].', 1), ('lutym', 1), ('sajgonie', 1), ('(obecnym', 1), ('ho', 1), ('chi', 1), ('minh).', 1), ('siłami', 1), ('floty', 1), ('bazującej', 1), ('tajwanie[17].', 1), ('lipcu', 1), ('sierpniu', 1), ('uczestniczył', 1), ('zajęciu', 1), ('indochin', 1), ('francuskich[17].', 1), ('nocy', 1), ('eskortujący', 1), ('inwazyjne', 1), ('stoczył', 1), ('walkę', 1), ('alianckimi', 1), ('„houston”', 1), ('(ca-30)', 1), ('hmas', 1), ('„perth”[18].', 1), ('zaatakowany', 1), ('„tautog”', 1), ('(ss-199).', 1), ('wystrzelone', 1), ('torpedy', 1), ('trafiły', 1), ('rufę', 1), ('krążownika.', 1), ('eksplozja', 1), ('spowodowała', 1), ('oderwanie', 1), ('reszty', 1), ('20-metrowej', 1), ('rufy[18].', 1), ('krytycznie', 1), ('uszkodzona', 1), ('trudem', 1), ('dotarła', 1), ('ambon[18].', 1), ('głęboką', 1), ('modernizację.', 1), ('podwodnego', 1), ('ujścia', 1), ('cieśniny', 1), ('san', 1), ('bernardino[18].', 1), ('wodowany', 1), ('incydentu', 1), ('szanghajskiego,', 1), ('artyleryjskim', 1), ('działania', 1), ('lądzie[18].', 1), ('japońsko-chińskiej', 1), ('rejon', 1), ('qingdao[18].', 1), ('okrętem', 1), ('flagowym', 1), ('podwodnych,', 1), ('operując', 1), ('karolinów,', 1), ('marshalla', 1), ('marianów', 1), ('miesiącach', 1), ('września[18].', 1), ('ciężkimi', 1), ('„kumano”', 1), ('„suzuya”', 1), ('endau[19].', 1), ('wsparcia', 1), ('walk', 1), ('lotnisko', 1), ('uderzeniowej', 1), ('opuścił', 1), ('shortland[20].', 1), ('grupa', 1), ('zaatakowana', 1), ('bombowce', 1), ('horyzontalne', 1), ('nurkujące.', 1), ('bombami', 1), ('okolice', 1), ('rufy[19].', 1), ('około', 1), ('godziny', 1), ('15:00', 1), ('nastąpił', 1), ('atak,', 1), ('którego', 1), ('kolejnymi', 1), ('bombami,', 1), ('spowodowało', 1), ('liczne', 1), ('pożary[19].', 1), ('opuściła', 1), ('przeszła', 1), ('niszczyciela', 1), ('„murasame”,', 1), ('niszczyciele:', 1), ('„yūdachi”', 1), ('„harusame”', 1), ('dobiły', 1), ('opuszczony', 1), ('krążownik[19].', 1), ('kinu', 1), ('kinu.', 1), ('stycznia', 1), ('chińsko-japońskiej.', 1), ('malaje.', 1), ('wspierała', 1), ('miri', 1), ('sarawaku,', 1), ('kuching[21].', 1), ('we', 1), ('wrześniu', 1), ('bliźniaczym', 1), ('desantem', 1), ('salomona.', 1), ('wysadził', 1), ('wyspie', 1), ('shortland,', 1), ('moluków[21].', 1), ('głęboką,', 1), ('wojenną', 1), ('modernizacje', 1), ('podobnie', 1), ('serii,', 1), ('„yury”.', 1), ('leyte.', 1), ('ormoc[21].', 1), ('(1923).', 1), ('stępka', 1), ('budowę', 1), ('położona', 1), ('co.', 1), ('cesarskiej', 1), ('marynarce', 1), ('1925', 1), ('budowa', 1), ('uległa', 1), ('opóźnieniu', 1), ('zniszczeń', 1), ('trzęsienia', 1), ('ziemi,', 1), ('ostatecznie', 1), ('budowano', 1), ('3,5', 1), ('roku[19].', 1), ('japońsko-chińskiej.', 1), ('tamtym', 1), ('modernizowano', 1), ('flotyllą', 1), ('niszczycieli,', 1), ('wyszedł', 1), ('flotą', 1), ('admirała', 1), ('nagumo', 1), ('pearl', 1), ('harbor[19].', 1), ('inwazji', 1), ('jawę', 1), ('ośmioma', 1), ('przechwytywał', 1), ('płynące', 1), ('jawą', 1), ('australią[19].', 1), ('połowie', 1), ('włączono', 1), ('1.', 1), ('zespołu', 1), ('regionu', 1), ('północnego,', 1), ('zadanie', 1), ('przejąć', 1), ('aleuty[22].', 1), ('jako', 1), ('część', 1), ('eskorty', 1), ('adak.', 1), ('trakcie', 1), ('rejsu', 1), ('odwołano', 1), ('operację', 1), ('niepowodzenia', 1), ('midway.', 1), ('attu,', 1), ('wylądowała', 1), ('czerwca.', 1), ('pozostawały', 1), ('rejonie,', 1), ('patrolując', 1), ('go', 1), ('połowy', 1), ('czerwca[23].', 1), ('kiska.', 1), ('jednostkę', 1), ('zmodernizowano', 1), ('wzór', 1), ('nagara.', 1), ('uczestniczyła', 1), ('leyte,', 1), ('zatopiona[23].', 1)]
('w', 128)
('na', 65)
('roku', 44)

```





### Program przyklad_args_kwargs

Kod programu:
```python

def wypisz(a, b=None, c=None, d=None):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
    if d:
        print(d)
    print()

wypisz(1)
wypisz(1, 2, 3, 4)

def wypisz2(*args):
    print('Podano args: ', args)
    for arg in args:
        print(arg)

wypisz2(1)
wypisz2(1, 2, 3, 4)
wypisz2(1, 2, 3, 4, 5, 6, 7, 344, 34, 23, 'b', 'mm')

lista = [1, 31]
wypisz2(*lista)
```



Output:
```
1

1
2
3
4

Podano args:  (1,)
1
Podano args:  (1, 2, 3, 4)
1
2
3
4
Podano args:  (1, 2, 3, 4, 5, 6, 7, 344, 34, 23, 'b', 'mm')
1
2
3
4
5
6
7
344
34
23
b
mm
Podano args:  (1, 31)
1
31

```





### Program przyklad_args_kwargs2

Kod programu:
```python

def wypisz(a, b, c):
    print('a ', a, ', b ', b, ', c', c)

wypisz(a='A', b='B', c='C')
wypisz(b='B', a='A', c='C')
wypisz(c='C', b='B', a='A')


wypisz('A', b='B', c='C')
wypisz('A', c='C', b='B')

def wypisz2(*args, **kwargs):
    print('args ', args)
    print('kwargs ', kwargs)

wypisz2('A', c='C', b='B')
```



Output:
```
a  A , b  B , c C
a  A , b  B , c C
a  A , b  B , c C
a  A , b  B , c C
a  A , b  B , c C
args  ('A',)
kwargs  {'c': 'C', 'b': 'B'}

```





### Program przyklad_args_kwargs3

Kod programu:
```python
import datetime
def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)


def podaj_date(**kwargs) -> datetime.date:
    print('podano kwargs: ', kwargs)

    if 'dzien' not in kwargs:
        print('Podaj dzien urodzenia')
        kwargs['dzien'] = podaj_liczbe_z_zakresu(1, 31)

    if 'miesiac' not in kwargs:
        print('Podaj miesiac urodzenia')
        kwargs['miesiac'] = podaj_liczbe_z_zakresu(1, 12)

    if 'rok' not in kwargs:
        kwargs['rok'] = int(input('Podaj rok urodzenia: '))

    print('pełny słownik: ', kwargs)
    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')
```



Zdefiniuj funkcje podaj_date,


Funkcja ma powiedzieć, co już wie i spytać się o to czego brakuje

Przykładowe użycia:
```
data = podaj_date(dzien=19, miesiac=11)


Mam podany dzień: 19
Mam podany miesiąc: 11
Proszę podać rok: ...

data = podaj_date(rok=2022)
Podaj dzień...
Podaj miesiesiąc: ...
Mam podany rok: 2022
```



### Program funkcja_odczytaj_date

Kod programu:
```python
"""

Zdefiniuj funkcje podaj_date,


Funkcja ma powiedzieć, co już wie i spytać się o to czego brakuje

Przykładowe użycia:
data = podaj_date(dzien=19, miesiac=11)

Mam podany dzień: 19
Mam podany miesiąc: 11
Proszę podać rok: ...

data = podaj_date(rok=2022)
Podaj dzień...
Podaj miesiesiąc: ...
MAm podany rok: 2022
"""

import datetime
def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)


def podaj_date(**kwargs) -> datetime.date:

    if 'dzien' in kwargs:
        print('Mam podany dzien ', kwargs['dzien'])
    else:
        print('Podaj dzien urodzenia')
        kwargs['dzien'] = podaj_liczbe_z_zakresu(1, 31)

    if 'miesiac' in kwargs:
        print('Mam podany miesiac ', kwargs['miesiac'])
    else:
        print('Podaj miesiac urodzenia')
        kwargs['miesiac'] = podaj_liczbe_z_zakresu(1, 12)

    if 'rok' in kwargs:
        print('Mam podany rok ', kwargs['rok'])
        print(f'Mam podany rok {kwargs["rok"]} ')
    else:
        kwargs['rok'] = int(input('Podaj rok urodzenia: '))

    print('pełny słownik: ', kwargs)
    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')
```





### Program str_definicja.py

Kod programu:
```python
zmienna = 'teskt'
zmienna = "acasc "
# błąd:
# zmienna = "ac " asc "

x = ' defninujemy cos slownik[\'miesiac\']   '
x = " defninujemy cos slownik['miesiac']   "
x = ' defninujemy cos slownik["miesiac"]   '
```



Output:
```

```





### Program funkcja_odczytaj_date2.py

Kod programu:
```python
"""

Zdefiniuj funkcje podaj_date,


Funkcja ma powiedzieć, co już wie i spytać się o to czego brakuje

Przykładowe użycia:
data = podaj_date(dzien=19, miesiac=11)

Mam podany dzień: 19
Mam podany miesiąc: 11
Proszę podać rok: ...

data = podaj_date(rok=2022)
Podaj dzień...
Podaj miesiesiąc: ...
MAm podany rok: 2022
"""

import datetime
def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)

pola_daty = {'dzien': [1, 31], 'miesiac': [1, 12], 'rok': [1000, 2022]}

def podaj_date(**kwargs) -> datetime.date:
    for nazwa_pola in pola_daty.keys():
        if nazwa_pola in kwargs:
            print(f'Podano z góry {nazwa_pola}: {kwargs[nazwa_pola]}')
    for nazwa_pola, zakres_pola in pola_daty.items():
        if nazwa_pola not in kwargs:
            print(f'proszę podać {nazwa_pola}:')
            kwargs[nazwa_pola] = podaj_liczbe_z_zakresu(*zakres_pola)
    return stworz_date(**kwargs)


data = podaj_date(dzien=19, miesiac=11)
print(data)

data = podaj_date(rok=2022)
print(data)
# podaj_date(dzien=19, miesiac_nazwa='listopad')
```





### Program funkcja_odczytaj_date3.py

Kod programu:
```python
"""

Zdefiniuj funkcje podaj_date,


Funkcja ma powiedzieć, co już wie i spytać się o to czego brakuje

Przykładowe użycia:
data = podaj_date(dzien=19, miesiac=11)

Mam podany dzień: 19
Mam podany miesiąc: 11
Proszę podać rok: ...

data = podaj_date(rok=2022)
Podaj dzień...
Podaj miesiesiąc: ...
MAm podany rok: 2022
"""

import datetime
def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b}: ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba

def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)

pola_daty = {'dzien': [1, 31], 'miesiac': [1, 12], 'rok': [1000, 2022]}

lista_miesiecy = ['styczen', 'luty', 'marzec', 'kwiecen', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrze',
                  'paz', 'listopad', 'grudzien']

def str_do_int_miesiac(nazwa_miesiaca):
    return lista_miesiecy.index(nazwa_miesiaca) + 1


def podaj_date(**kwargs) -> datetime.date:
    if 'miesiac_nazwa' in kwargs:
        kwargs['miesiac'] = str_do_int_miesiac(kwargs['miesiac_nazwa'])
        del kwargs['miesiac_nazwa']
    for nazwa_pola in pola_daty.keys():
        if nazwa_pola in kwargs:
            print(f'Podano z góry {nazwa_pola}: {kwargs[nazwa_pola]}')
    for nazwa_pola, zakres_pola in pola_daty.items():
        if nazwa_pola not in kwargs:
            print(f'proszę podać {nazwa_pola}:')
            kwargs[nazwa_pola] = podaj_liczbe_z_zakresu(*zakres_pola)

    return stworz_date(**kwargs)

data = podaj_date(dzien=19, miesiac_nazwa='listopad')
print(data)

```




Do przerobienia:
 - with open context manager