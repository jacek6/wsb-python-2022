
## Definicja pętli while.

plik(`definicja_while.py`)

Zadanie 

Gra "zgadnij jaką liczbę mam na myśli"? 
 - Program losuje liczbę z przedziału <1,100>
 - Program pyta użytkownika o liczbę i mówi, czy podana liczba jest  większa, mniejsza bądź równa wylosowanej.


plik(`zgadnij_liczbe_ver_bez_losowania.py`)
plik(`zgadnij_liczbe_ver_z losowaniem.py`)

Dla chętnych opis jak na różne sposoby losować w Python:
 - https://pynative.com/python-random-randrange/

plik(`random_ranint_vs_randrange.py`)

zadanie
Co jest bardziej prawdopodobne:
 - rzut 1 kostką, gdzie sukces to 4, 5, 6
 - rzut 3 kostkami, gdzie sukces to przynajmniej 1 szóstka?
Jak policzyć, co z tych dwóch opcji ma większą szansę na 
sukces?
 - Można analitycznie… ?
 - A można napisać program, który rzuci kostkami 1000 razy, a następnie przedstawi wyniki oraz porówna wyniki?

plik(`kostki_poczatek`)
plik(`sprawdzanie_w_liscie`)
plik(`kostki_1000_rzutow`)

zadanie
Znajdź sumę oczek, która jest najbardziej prawdopodobna przy:
a)	Rzucie 2 kostkami
b)	Rzucie 3 kostkami
c)	Rzucie 11 kostkami
d)	Użytkownik decyduje iloma kośćmi rzucić



plik(`zliczanie_sukcesow`)
plik(`zliczanie_sukcesow2.py`)
plik(`sumy_kostek_a.py`)



plik(`sumy_kostek_b.py`)

Wymaga wytłumaczenia

kod:
```python
    wynik_kostki_1 = random.randint(1, 6)
    wynik_kostki_2 = random.randint(1, 6)
    wynik_kostki_3 = random.randint(1, 6)

    wyrzucona_suma = wynik_kostki_1 + wynik_kostki_2 + wynik_kostki_3

```

działą tak samo jak kod:
```python
wyrzucona_suma = 0
    wyrzucona_suma += wynik_kostki_1
    wyrzucona_suma += wynik_kostki_2
    wyrzucona_suma += wynik_kostki_3
```

i tak samo jak kod:
```python
    wyrzucona_suma = 0
    for rzut_kostka in range(3):
        wyrzucona_suma += random.randint(1, 6)
```

wtedy możemy kontrolować liczbę wyrzuconych kostek i ustawić np 11 rzutów kośćmi:
```python
    wyrzucona_suma = 0
    for rzut_kostka in range(11):
        wyrzucona_suma += random.randint(1, 6)
```

plik(`sumy_kostek_c.py`)
plik(`sumy_kostek_d.py`)

zadanie
Sprawdźmy, czy dane słowo jest anagramem.
Anagram to: axa, kajak, owo.

plik(`tekst_to_lista.py`)
plik(`zadanie_anagramy_bez_input.py`)
plik(`zadanie_anagramy_bez_input2.py`)
plik(`zadanie_anagramy_bez_input3.py`)
plik(`zadanie_anagram_rozwiazanie`)

zadanie
Napisz program, który zamienia wszystkie wykrzykniki na kropki.

plik(`zamiana_znakow1`)
plik(`zamiana_znakow2`)
plik(`zamiana_znakow3`)
plik(`zamiana_znakow4`)

zadanie
Sprawdźmy, czy dane hasło jest silne. Jeśli nie – dlaczego?

plik(`silne_haslo1`)
plik(`silne_haslo2`)
plik(`silne_haslo_po_znakach_hasla.py`)
plik(`przyklad_date_time.py`)



plik(`definicja_funkcje`)
plik(`funkcje1`)
plik(`funckje_kosci.py`)
plik(`funckje_kosci2.py`)
plik(`funckje_kosci3.py`)
plik(`funckje_kosci4.py`)
plik(`funckje_kosci5.py`)
plik(`jak_wolac_funkcje1`)
plik(`jak_wolac_funkcje2`)
plik(`funkcje_i_petle`)

zadanie
Dla podanego plików twórz jego kopię zapasową co 10 sekund.
Kopia zapasowa, ma mieć nazwę jak plik i mieć time stamp.



plik(`auto_backup1`)