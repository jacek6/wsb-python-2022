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

plik(`powtorka.py`)


## Pomysły na zadania
 - słownik do przeliczania kuru walut w powtórce
 - ogólnie program z powtórki ładniej napisać z funkcjami

# Pętla while
plik(`while_przyklad1`)

plik(`while_true_przyklad1`)

Napisz program, który przyjmuje numer PESEL i weryfikuje jego poprawność.

Program pyta tak długo, aż zostanie wprowadzony poprawny PESEL bądź użytkownik wyjdzie z programu.

Przyjmij, że:
PESEL jest czterocyfrowy, 
w poprawnym numerze PESEL suma cyfr jest podzielna przez 3 lub przez 4.


plik(`while_zadanie_przylad1`)

Napisz program, który w ustalonej posortowanej liście wyszukuje indeks konkretnego elementu.

	lista = [-88, -3, 11, 23, 56, 78, 98, 154, 176, 198, 275, 375, 416, 524, 564, 627, 738, 873, 924]

Wejście:
Wartość elementu do znalezienia
Wyjście:
Indeks na którym indeksie listy jest ten element, lub jeśli go nie ma informacja o tym na jakim indeksie by się znajdował
Wymagania:
Użyj wyszukiwania binarnego z użyciem pętli while


plik(`while_wyszukiwanie_binarne1`)

Napisz program, który poczeka aż bęzie pełna minuta
plik(`while_pelna_minuta`)


Napisz program, który poczeka aż powstanie określony plik
plik(`while_zadanie_istanieje_plik`)

Przykład działania while-elase
plik(`while_else`)

## Funkcje
plik(`funkcja_przyklad1`)
plik(`funkcja_przyklad2`)
plik(`funkcja_przyklad3`)
plik(`funkcja_przylad_wartosci_domyslne`)

Napisz funkcję, która przyjmuje metraż, wiek oraz typ budynku i zwraca informację, czy można w nim mieszkać.

plik(`funkcje_zadanie1`)

Napisz funkcje, która przyjmuje dane użytkownika i zwraca informację, czy użytkownik może dalej używać programu.

plik(`funkcje_zadanie2`)

Napisz funkcje która oczekuje aż użytkownik poda liczbę z zadanego zakresu. Użyj tej funkcji w programie, który pyta o datę urodzenia i oblicza ile ktoś ma lat, miesięcy, dni.

plik(`funkcje_zadanie3`)

Napisz funkcje która oczekuje aż użytkownik zgodzi się na warunki działania programu, jeśli odp użytkownika jest „tak” to się zgodził i program ma działać dalej. Jeśli użytkownik odp „nie” program ma się zakończyć. Każda inna odp ma powodować powtórzenie pytania. Dodaj tą funkcję do poprzedniego programu.
plik(`funkcje_zadanie4`)
plik(`slownik_przyklad1`)
plik(`slownik_przyklad2`)

PRzykład sprawdzenia czy cos jest słowniku.
plik(`slownik_przyklad3`)


Program pozwala zmienić hasło użytkownika – pobiera hasło ze słownika i porównuje.
plik(`slownik_zadanie1`)
plik(`slownik_zadanie2`)
plik(`slownik_zadanie2_czytanie_pliku`)
plik(`przyklad_args_kwargs`)
plik(`przyklad_args_kwargs2`)
plik(`przyklad_args_kwargs3`)

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
plik(`funkcja_odczytaj_date`)
plik(`str_definicja.py`)
plik(`funkcja_odczytaj_date2.py`)
plik(`funkcja_odczytaj_date3.py`)


Do przerobienia:
 - with open context manager