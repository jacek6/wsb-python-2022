
## Definicja pętli while.




### Program definicja_while.py

Kod programu:
```python
while True:  # pętla będzie się wykonywać,
    password = input('Wpisz haslo: ')  # aż do polecenia „break”
    if password == '123abc':
        print('Haslo przyjete')
        break
    else:
        print('Zle haslo, jeszcze raz')

```



## zadanie 1


Gra "zgadnij jaką liczbę mam na myśli"? 
 - Program losuje liczbę z przedziału <1,100>
 - Program pyta użytkownika o liczbę i mówi, czy podana liczba jest  większa, mniejsza bądź równa wylosowanej.





### Program zgadnij_liczbe_ver_bez_losowania.py

Kod programu:
```python
liczba_do_zgadniecia = 50

while True:
    liczba_podana = int(input('Zgadnij jaka to liczba: '))

    if liczba_podana == liczba_do_zgadniecia:
        print('zgadles to bylo ', liczba_do_zgadniecia)
        break

    if liczba_podana > liczba_do_zgadniecia:
        print('Podana przez ciebie liczba jest za duza')
    elif liczba_podana < liczba_do_zgadniecia:
        print('Podana przez ciebie liczba jest za mala')
print('koniec programu')
```





### Program zgadnij_liczbe_ver_z losowaniem.py

Kod programu:
```python
import random
liczba_do_zgadniecia = random.randint(1, 100)

while True:
    liczba_podana = int(input('Zgadnij jaka to liczba: '))

    if liczba_podana == liczba_do_zgadniecia:
        print('zgadles to bylo ', liczba_do_zgadniecia)
        break

    if liczba_podana > liczba_do_zgadniecia:
        print('Podana przez ciebie liczba jest za duza')
    elif liczba_podana < liczba_do_zgadniecia:
        print('Podana przez ciebie liczba jest za mala')
print('koniec programu')
```



Dla chętnych opis jak na różne sposoby losować w Python:
 - https://pynative.com/python-random-randrange/




### Program random_ranint_vs_randrange.py

Kod programu:
```python
import random

# randint może zwrócić 5 (podany górny zakres)
for i in range(15):
    print('randint = ', random.randint(1, 5))
print()

# randrange nigdy nie zwrócic podanego górnego zakresu
# randrange może przyjść krok locsowania = co ile losować
for i in range(15):
    # print('randrange ', random.randrange(1, 100, 20))
    print('randrange ', random.randrange(1, 5))
```



Output:
```
randint =  5
randint =  4
randint =  1
randint =  5
randint =  5
randint =  1
randint =  4
randint =  3
randint =  3
randint =  1
randint =  2
randint =  5
randint =  2
randint =  4
randint =  4

randrange  1
randrange  1
randrange  2
randrange  2
randrange  2
randrange  3
randrange  2
randrange  2
randrange  1
randrange  4
randrange  3
randrange  1
randrange  4
randrange  2
randrange  2

```



## zadanie 2

Co jest bardziej prawdopodobne:
 - rzut 1 kostką, gdzie sukces to 4, 5, 6
 - rzut 3 kostkami, gdzie sukces to przynajmniej 1 szóstka?
Jak policzyć, co z tych dwóch opcji ma większą szansę na 
sukces?
 - Można analitycznie… ?
 - A można napisać program, który rzuci kostkami 1000 razy, a następnie przedstawi wyniki oraz porówna wyniki?




### Program kostki_poczatek

Kod programu:
```python
import random

lista_kostek = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
print(lista_kostek)

if 1 in lista_kostek:
    print('jedna z kostek wyrzucila 1')
else:
    print('zadna kostka nie wyrzucila 1')
```



Output:
```
[1, 3, 4]
jedna z kostek wyrzucila 1

```





### Program sprawdzanie_w_liscie

Kod programu:
```python
uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

szukany_uzytkownik = 'marek'

if szukany_uzytkownik in uzytkownicy:
    print('znaleziono uzytkownika')
```



Output:
```
znaleziono uzytkownika

```





### Program kostki_1000_rzutow

Kod programu:
```python
import random

sukcesy_przy_rzucie_1_koscia = 0
sukcesy_przy_rzucie_3_kostkami = 0

for nr_powtorzenia_testu in range(1000):
    pierwsza_kostka = random.randint(1, 6)
    kostki = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    if pierwsza_kostka >= 4:
        # print('sukces przy rzucie 1 kostka')
        sukcesy_przy_rzucie_1_koscia += 1

    if 6 in kostki:
        # print('sukces przu rzucami wieloma kostkami')
        sukcesy_przy_rzucie_3_kostkami += 1

if sukcesy_przy_rzucie_1_koscia > sukcesy_przy_rzucie_3_kostkami:
    print('jest wiecej sukcesow przy rzucie 1 koscia')
elif sukcesy_przy_rzucie_1_koscia == sukcesy_przy_rzucie_3_kostkami:
    print('jest to tak samo prawdopodobne')
else:
    print('jest wiecej sukcesow przy rzucie 3 kostkami')

print('sukcesy_przy_rzucie_1_koscia = ', sukcesy_przy_rzucie_1_koscia)
print('sukcesu_przy_rzucie_3_kostkami = ', sukcesy_przy_rzucie_3_kostkami)


```



Output:
```
jest wiecej sukcesow przy rzucie 1 koscia
sukcesy_przy_rzucie_1_koscia =  485
sukcesu_przy_rzucie_3_kostkami =  410

```



## zadanie 3

Znajdź sumę oczek, która jest najbardziej prawdopodobna przy:
a)	Rzucie 2 kostkami
b)	Rzucie 3 kostkami
c)	Rzucie 11 kostkami
d)	Użytkownik decyduje iloma kośćmi rzucić






### Program zliczanie_sukcesow

Kod programu:
```python
zliczanie_sukcesow = [0, 0]

print('Poczatek ', zliczanie_sukcesow)

# zliczanie_sukcesow[0] += 1
zliczanie_sukcesow[1] += 1
zliczanie_sukcesow[1] += 1

print('Koniec ', zliczanie_sukcesow)

```



Output:
```
Poczatek  [0, 0]
Koniec  [0, 2]

```





### Program zliczanie_sukcesow2.py

Kod programu:
```python
zliczanie_sukcesow = [0] * 13

print('Poczatek ', zliczanie_sukcesow)

zliczanie_sukcesow[0] += 1
zliczanie_sukcesow[1] += 1
zliczanie_sukcesow[1] += 1
zliczanie_sukcesow[3] += 1
zliczanie_sukcesow[11] += 1

zliczanie_sukcesow[12] += 1


print('Koniec ', zliczanie_sukcesow)

```



Output:
```
Poczatek  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Koniec  [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]

```





### Program sumy_kostek_a.py

Kod programu:
```python
import random

sukcesy_wyrzuconych_sum = [0] * 13

for nr_powtorzenia in range(1000):
    wynik_kostki_1 = random.randint(1, 6)
    wynik_kostki_2 = random.randint(1, 6)

    wyrzucona_suma = wynik_kostki_1 + wynik_kostki_2
    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')
```



Output:
```
sukcesy_wyrzuconych_sum =  [0, 0, 23, 51, 72, 126, 120, 169, 156, 104, 83, 65, 31]
Najbardziej prawdopodobna suma to:  7  wyrzucono ja  169  razy

```








### Program sumy_kostek_b.py

Kod programu:
```python
import random

sukcesy_wyrzuconych_sum = [0] * 19

for nr_powtorzenia in range(1000):
    wynik_kostki_1 = random.randint(1, 6)
    wynik_kostki_2 = random.randint(1, 6)
    wynik_kostki_3 = random.randint(1, 6)

    wyrzucona_suma = wynik_kostki_1 + wynik_kostki_2 + wynik_kostki_3

    wyrzucona_suma = 0
    wyrzucona_suma += wynik_kostki_1
    wyrzucona_suma += wynik_kostki_2
    wyrzucona_suma += wynik_kostki_3

    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')
```



Output:
```
sukcesy_wyrzuconych_sum =  [0, 0, 0, 3, 11, 29, 47, 67, 108, 107, 106, 134, 128, 101, 70, 38, 34, 13, 4]
Najbardziej prawdopodobna suma to:  11  wyrzucono ja  134  razy

```



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




### Program sumy_kostek_c.py

Kod programu:
```python
import random

sukcesy_wyrzuconych_sum = [0] * 67

for nr_powtorzenia in range(10000):
    wyrzucona_suma = 0
    for rzut_kostka in range(11):
        wyrzucona_suma += random.randint(1, 6)

    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')
```



Output:
```
sukcesy_wyrzuconych_sum =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 5, 8, 24, 23, 51, 68, 102, 117, 168, 232, 294, 365, 439, 515, 607, 624, 666, 689, 670, 685, 604, 561, 552, 437, 340, 313, 264, 193, 132, 100, 58, 40, 27, 10, 7, 3, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0]
Najbardziej prawdopodobna suma to:  38  wyrzucono ja  689  razy

```





### Program sumy_kostek_d.py

Kod programu:
```python
import random

ile_razy_rzucic_koscia = int(input('Ile razy rzucic koscia: '))  # 11

sukcesy_wyrzuconych_sum = [0] * ile_razy_rzucic_koscia * 7

for nr_powtorzenia in range(10000):
    wyrzucona_suma = 0
    for rzut_kostka in range(ile_razy_rzucic_koscia):
        wyrzucona_suma += random.randint(1, 6)

    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')
```



## zadanie 4

Sprawdźmy, czy dane słowo jest anagramem.
Anagram to: axa, kajak, owo.




### Program tekst_to_lista.py

Kod programu:
```python
slowo = 'kajak'

lista = [45, 78, 34]

for i in lista:
    print(i)

for ch in slowo:
    print(ch)

for i, ch in enumerate(slowo):
    print('na pozycji ', i, ' znajduje sie litera ', ch)

```



Output:
```
45
78
34
k
a
j
a
k
na pozycji  0  znajduje sie litera  k
na pozycji  1  znajduje sie litera  a
na pozycji  2  znajduje sie litera  j
na pozycji  3  znajduje sie litera  a
na pozycji  4  znajduje sie litera  k

```





### Program zadanie_anagramy_bez_input.py

Kod programu:
```python
# slowo = 'kajak'
slowo = 'wrggsdvksdmvklaeipqeio wevpksd vsd'

print('dlugosc podanego slowa to ', len(slowo))

for i in range(len(slowo)):
    print('na pozycji ', i, 'znajduje sie litera', slowo[i], ' po przeciwnej stronie jest litera ', slowo[len(slowo) - 1 - i])

    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        break

```



Output:
```
dlugosc podanego slowa to  34
na pozycji  0 znajduje sie litera w  po przeciwnej stronie jest litera  d
to na pewno nie anagram

```





### Program zadanie_anagramy_bez_input2.py

Kod programu:
```python
slowo = 'kajxk'

print('dlugosc podanego slowa to ', len(slowo))

for i in range(len(slowo)):
    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        break

# if i > 0:
if i == len(slowo) - 1:
    print('Podane slowo ', slowo, 'jest anagramem')


```



Output:
```
dlugosc podanego slowa to  5
to na pewno nie anagram

```





### Program zadanie_anagramy_bez_input3.py

Kod programu:
```python
slowo = 'kajak'

print('dlugosc podanego slowa to ', len(slowo))

czy_to_anagram = True
for i in range(len(slowo)):
    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        czy_to_anagram = False
        break
if czy_to_anagram:
    print('Podane slowo ', slowo, 'jest anagramem')


```



Output:
```
dlugosc podanego slowa to  5
Podane slowo  kajak jest anagramem

```





### Program zadanie_anagram_rozwiazanie

Kod programu:
```python
slowo = input('Podaj słowo do sprawdzenia czy jest anagramem: ')

print('dlugosc podanego slowa to ', len(slowo))

czy_to_anagram = True
for i in range(len(slowo)):
    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        czy_to_anagram = False
        break
if czy_to_anagram:
    print('Podane slowo ', slowo, 'jest anagramem')


```



## zadanie 5

Napisz program, który zamienia wszystkie wykrzykniki na kropki.




### Program zamiana_znakow1

Kod programu:
```python
tekst = 'ala ma kota! oraz psa. the end'

for ch in tekst:
    print(ch, end='')
print()
print('koniec programu')
```



Output:
```
ala ma kota! oraz psa. the end
koniec programu

```





### Program zamiana_znakow2

Kod programu:
```python
tekst = 'ala ma kota! oraz psa. the end'

for ch in tekst:
    if '!' in tekst:
        print('.', end='')
    print(ch, end='')
print()
print('koniec programu')
```



Output:
```
.a.l.a. .m.a. .k.o.t.a.!. .o.r.a.z. .p.s.a... .t.h.e. .e.n.d
koniec programu

```





### Program zamiana_znakow3

Kod programu:
```python
tekst = 'ala ma kota! oraz psa. the end'
# tekst[0] = 'A'

nowy_tekst = ''
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    nowy_tekst += ch
    print('stworzylem tekst: ', nowy_tekst)
print()
print('orginalny teskst ', tekst)
print('zmieniony teskst ', nowy_tekst)
print()
print('koniec programu')
```



Output:
```
astworzylem tekst:  a
lstworzylem tekst:  al
astworzylem tekst:  ala
 stworzylem tekst:  ala 
mstworzylem tekst:  ala m
astworzylem tekst:  ala ma
 stworzylem tekst:  ala ma 
kstworzylem tekst:  ala ma k
ostworzylem tekst:  ala ma ko
tstworzylem tekst:  ala ma kot
astworzylem tekst:  ala ma kota
.stworzylem tekst:  ala ma kota.
 stworzylem tekst:  ala ma kota. 
ostworzylem tekst:  ala ma kota. o
rstworzylem tekst:  ala ma kota. or
astworzylem tekst:  ala ma kota. ora
zstworzylem tekst:  ala ma kota. oraz
 stworzylem tekst:  ala ma kota. oraz 
pstworzylem tekst:  ala ma kota. oraz p
sstworzylem tekst:  ala ma kota. oraz ps
astworzylem tekst:  ala ma kota. oraz psa
.stworzylem tekst:  ala ma kota. oraz psa.
 stworzylem tekst:  ala ma kota. oraz psa. 
tstworzylem tekst:  ala ma kota. oraz psa. t
hstworzylem tekst:  ala ma kota. oraz psa. th
estworzylem tekst:  ala ma kota. oraz psa. the
 stworzylem tekst:  ala ma kota. oraz psa. the 
estworzylem tekst:  ala ma kota. oraz psa. the e
nstworzylem tekst:  ala ma kota. oraz psa. the en
dstworzylem tekst:  ala ma kota. oraz psa. the end

orginalny teskst  ala ma kota! oraz psa. the end
zmieniony teskst  ala ma kota. oraz psa. the end

koniec programu

```





### Program zamiana_znakow4

Kod programu:
```python
tekst = 'ala ma kota! oraz psa. the end'
# tekst[0] = 'A'

znaki_nowego_tesktu = []
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    znaki_nowego_tesktu.append(ch)
print()
print('orginalny teskst ', tekst)
print('znaki_nowego_tesktu = ', znaki_nowego_tesktu)
nowy_tekst = ''.join(znaki_nowego_tesktu)  # składa tekst z listy tesktów
print('nowy_tekst ', nowy_tekst)
print()
print('koniec programu')
```



Output:
```
ala ma kota. oraz psa. the end
orginalny teskst  ala ma kota! oraz psa. the end
znaki_nowego_tesktu =  ['a', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a', '.', ' ', 'o', 'r', 'a', 'z', ' ', 'p', 's', 'a', '.', ' ', 't', 'h', 'e', ' ', 'e', 'n', 'd']
nowy_tekst  ala ma kota. oraz psa. the end

koniec programu

```



## zadanie 6

Sprawdźmy, czy dane hasło jest silne. Jeśli nie – dlaczego?




### Program silne_haslo1

Kod programu:
```python
haslo = 'abc123'

# cyfry = ['0', '1', ...]
cyfry = '1234567890'

czy_jest_cyfra = False
for cyfra in cyfry:
    if cyfra in haslo:
        czy_jest_cyfra = True
        break

if czy_jest_cyfra:
    print('haslo ma cyfre')
else:
    print('haslo musi miec cyfre')
```



Output:
```
haslo ma cyfre

```





### Program silne_haslo2

Kod programu:
```python
haslo = 'abc123!'

# cyfry = ['0', '1', ...]
cyfry = '1234567890'
znaki_specjalne = '!@#$%^&*()-+{}|:"<>?,./;[]\\'

czy_jest_cyfra = False
for cyfra in cyfry:
    if cyfra in haslo:
        czy_jest_cyfra = True
        break

czy_jest_znak_specjalny = False
for znak in znaki_specjalne:
    if znaki_specjalne in haslo:
        czy_jest_znak_specjalny = True
        break

if czy_jest_cyfra and czy_jest_znak_specjalny and len(haslo) > 6:
    print('haslo jest silne')
else:
    print('haslo jest slabe')
```



Output:
```
haslo jest slabe

```





### Program silne_haslo_po_znakach_hasla.py

Kod programu:
```python
haslo = 'aBa123!'

znaki_specjalne = '!@#$%^&*()-+{}|:"<>?,./;[]\\'

czy_jest_cyfra = False
czy_jest_znak_specjalny = False
czy_jest_litera_duza = False
czy_jest_litera_mala = False
for ch in haslo:
    if ch.isdigit():
        czy_jest_cyfra = True
    if ch.isalpha():
        if ch.isupper():
            czy_jest_litera_duza = True
        else:
            czy_jest_litera_mala = True

    if ch in znaki_specjalne:
        czy_jest_znak_specjalny = True

if czy_jest_cyfra and czy_jest_znak_specjalny and czy_jest_litera_mala and czy_jest_litera_duza\
        and len(haslo) > 6:
    print('haslo jest silne')
else:
    print('haslo jest slabe')
```



Output:
```
haslo jest silne

```





### Program przyklad_date_time.py

Kod programu:
```python
import datetime
import time

#wyciągnięcie daty
today = datetime.date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("date1 =", d1)

# tekstowo miesiac, potem dzień i rok
d2 = today.strftime("%B %d, %Y")
print("date2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("date3 =", d3)

# tekstowo skrócony miesiac, potem dzień i rok
d4 = today.strftime("%b-%d-%Y")
print("date4 =", d4)

#wyciągnięcie godziny i daty
now = datetime.datetime.now()
timer = now.strftime('%H:%M:%S')
date = now.strftime('year = %Y,    month = %m,   day = %d')
print('Time now is : ', timer)
print('Date now is :', date)


#zadanie z różnymi nazwami
file = 'report.txt'

for i in range (4):
    now = datetime.datetime.now()
    timer = now.strftime('%H%M%S')
    file_name = file[:6] + timer + file[6:]
    print(file_name)
    time.sleep(1)

```



Output:
```
date1 = 16/10/2022
date2 = October 16, 2022
date3 = 10/16/22
date4 = Oct-16-2022
Time now is :  15:05:53
Date now is : year = 2022,    month = 10,   day = 16
report150553.txt
report150554.txt
report150555.txt
report150556.txt

```








### Program definicja_funkcje

Kod programu:
```python

def funckja1():
    print('uruchomiono funkcje 1')

funckja1()
```



Output:
```
uruchomiono funkcje 1

```





### Program funkcje1

Kod programu:
```python
odp = input('Czy chcesz się przywitać? (tak/nie): ')  #tak

def przywitaj_sie():
    print('Dzień dobry, witam.')

print('decyzja co zrobić')

if odp == 'tak':
    przywitaj_sie()
```





### Program funckje_kosci.py

Kod programu:
```python
import random

def rzuc_kostka():
    return random.randint(1, 6)

print('rzucono koscia ', rzuc_kostka())
print('rzucono koscia ', rzuc_kostka())
```



Output:
```
rzucono koscia  6
rzucono koscia  4

```





### Program funckje_kosci2.py

Kod programu:
```python
import random


def rzuc_kostka():
    return random.randint(1, 6)


def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    if wynik_rzutu >= 4:
        return True
    else:
        return False

for i in range(10):
    print('wynik sytuacji1 ', sytuacja1_czy_jest_sukces())

```



Output:
```
wynik sytuacji1  False
wynik sytuacji1  False
wynik sytuacji1  True
wynik sytuacji1  True
wynik sytuacji1  True
wynik sytuacji1  False
wynik sytuacji1  False
wynik sytuacji1  False
wynik sytuacji1  False
wynik sytuacji1  True

```





### Program funckje_kosci3.py

Kod programu:
```python
import random


def rzuc_kostka():
    return random.randint(1, 6)


def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    if wynik_rzutu >= 4:
        return True
    else:
        return False

def sytuacja2_czy_jest_sukces():
    wyniki_rzutow = [rzuc_kostka(), rzuc_kostka(), rzuc_kostka()]
    if 6 in wyniki_rzutow:
        return True
    else:
        return False

for i in range(10):
    print('wynik sytuacji2 ', sytuacja2_czy_jest_sukces())

```



Output:
```
wynik sytuacji2  False
wynik sytuacji2  True
wynik sytuacji2  False
wynik sytuacji2  False
wynik sytuacji2  False
wynik sytuacji2  False
wynik sytuacji2  False
wynik sytuacji2  True
wynik sytuacji2  True
wynik sytuacji2  True

```





### Program funckje_kosci4.py

Kod programu:
```python
import random


def rzuc_kostka():
    return random.randint(1, 6)


def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    if wynik_rzutu >= 4:
        return True
    else:
        return False

def sytuacja2_czy_jest_sukces():
    wyniki_rzutow = [rzuc_kostka(), rzuc_kostka(), rzuc_kostka()]
    if 6 in wyniki_rzutow:
        return True
    else:
        return False

sukcesy_stytuacji1 = 0
sukcesy_stytuacji2 = 0

for i in range(1000):
    if sytuacja1_czy_jest_sukces():
        sukcesy_stytuacji1 += 1
    if sytuacja2_czy_jest_sukces():
        sukcesy_stytuacji2 += 1

if sukcesy_stytuacji2 > sukcesy_stytuacji1:
    print('bardziej prawdopodobna jest sytuacja 2')
else:
    print('bardziej prawdopodobna jest sytuacja 1')
print('sukcesy_stytuacji1 = ', sukcesy_stytuacji1, '    sukcesy_stytuacji2 = ', sukcesy_stytuacji2)


```



Output:
```
bardziej prawdopodobna jest sytuacja 1
sukcesy_stytuacji1 =  528     sukcesy_stytuacji2 =  413

```





### Program funckje_kosci5.py

Kod programu:
```python
import random


def rzuc_kostka():
    return random.randint(1, 6)


def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    return wynik_rzutu >= 4


def sytuacja2_czy_jest_sukces():
    wyniki_rzutow = [rzuc_kostka(), rzuc_kostka(), rzuc_kostka()]
    return 6 in wyniki_rzutow


sukcesy_stytuacji1 = 0
sukcesy_stytuacji2 = 0

for i in range(1000):
    if sytuacja1_czy_jest_sukces():
        sukcesy_stytuacji1 += 1
    if sytuacja2_czy_jest_sukces():
        sukcesy_stytuacji2 += 1

if sukcesy_stytuacji2 > sukcesy_stytuacji1:
    print('bardziej prawdopodobna jest sytuacja 2')
else:
    print('bardziej prawdopodobna jest sytuacja 1')
print('sukcesy_stytuacji1 = ', sukcesy_stytuacji1, '    sukcesy_stytuacji2 = ', sukcesy_stytuacji2)

```



Output:
```
bardziej prawdopodobna jest sytuacja 1
sukcesy_stytuacji1 =  518     sukcesy_stytuacji2 =  423

```





### Program jak_wolac_funkcje1

Kod programu:
```python
import random
def rzuc_kostka():
    return random.randint(1, 6)

def sytuacja1():
    wynik_rzutu = rzuc_kostka()
    return wynik_rzutu >= 4

sukces = 0
for i in range (10):
    if sytuacja1():
        print(sytuacja1())
        sukces += 1
print(sukces)
```



Output:
```
False
True
False
True
False
True
True
7

```





### Program jak_wolac_funkcje2

Kod programu:
```python
import random
def rzuc_kostka():
    print('RZUT')
    return random.randint(1, 6)

def sytuacja1():
    wynik_rzutu = rzuc_kostka()
    return wynik_rzutu >= 4

sukces = 0
for i in range (10):
    wynik_sytuacj1 = sytuacja1()
    if wynik_sytuacj1:
        print(wynik_sytuacj1)
        sukces += 1
print(sukces)
```



Output:
```
RZUT
RZUT
True
RZUT
RZUT
RZUT
True
RZUT
RZUT
True
RZUT
RZUT
True
RZUT
True
5

```





### Program funkcje_i_petle

Kod programu:
```python
szukany_uzytkownik = input('Podaj nazwe uzytkowanika: ') # marek

uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

def sprawdz_uzytkownika():
    print('sprawdzam czy ', szukany_uzytkownik, ' jest wśród ', len(uzytkownicy))
    for u in uzytkownicy:
        print('porownuje z uzytkownikem ', u)
        if u == szukany_uzytkownik:
            return True
    return False

if sprawdz_uzytkownika():
    print('znaleziono uzytkownika')
else:
    print('nie znaleziono uzytkownika')

```



## zadanie 7

Dla podanego plików twórz jego kopię zapasową co 10 sekund.
Kopia zapasowa, ma mieć nazwę jak plik i mieć time stamp.






### Program auto_backup1

Kod programu:
```python
import datetime
import time

scizka = 'C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10\\dane\\dane.txt'


sciezka_do_pliku = 'C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10\\dane\dane.txt'

def odczytaj_plik():
    with open(sciezka_do_pliku, 'r') as fp:
        return fp.read()

def aktualny_timestamp():
    now = datetime.datetime.now()
    timer = now.strftime('%H%M%S')
    return timer

def wykonaj_kopie_zapasowa():
    nazwa_pliku_z_kopia = sciezka_do_pliku + aktualny_timestamp() + '.txt'
    print('wykonam kopie zapasowa ', nazwa_pliku_z_kopia)
    with open(nazwa_pliku_z_kopia, 'w') as fp:
        fp.write(odczytaj_plik())
    print('kopia zapasowa gotowa')

aktualna_zawartosc_pliku = odczytaj_plik()
print('aktualna_zawartosc_pliku = ', aktualna_zawartosc_pliku)
for i in range(100):
    najnowsza_zawartosc_pliku = odczytaj_plik()
    if najnowsza_zawartosc_pliku != aktualna_zawartosc_pliku:
        print('zauwazylem ze trzeba wykonac kopie zapasowa')
        wykonaj_kopie_zapasowa()
        aktualna_zawartosc_pliku = najnowsza_zawartosc_pliku
    time.sleep(2)
```


