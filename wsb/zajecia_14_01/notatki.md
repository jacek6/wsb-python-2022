

## Powtórka

Program lista rzeczy do zrobienia. Program ma oferować opcje:
 - Dodaj rzecz do zrobienia
 - Oznacz rzecz jako zrobioną
 - Pokaż rzeczy do zrobienia i zrobione
 - Usuń rzecz do zrobienia
 - Ustaw konkretną rzecz na początek
 - Wyjdź z programu

Można bazować na szkielecie programu:



### Program powrtork_szkielet.py

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
zbior_rzeczy_zrobionych = {'B'}

def dodaj_rzecz_do_zrobienia(lista, zbior_rzeczy_zrobionych):
    lista.append(input('Podaj coc chcesz zrobić: '))

def petla_glowna_programu():
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            dodaj_rzecz_do_zrobienia(lista, zbior_rzeczy_zrobionych)
        elif opcja == 2:
            oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych)
        elif opcja == 3:
            oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych)
        elif opcja == 4:
            oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych)
        elif opcja == 5:
            oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych)
        elif opcja == 6:
            return


petla_glowna_programu()
```



Działająca prosta wersja:



### Program program_bez_klasy

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


lista_czerwona = ['A', 'B', 'C', 'D']
zbior_rzeczy_zrobionych_czerwona = {'B'}

lista_niebieska = ['A', 'B', 'C', 'D']
zbior_rzeczy_zrobionych_niebieska = {'B'}

czy_lista_jest_zakazana = True
czy_lista_jest_zakazana = False

def dodaj_rzecz_do_zrobienia(lista, zbior_rzeczy_zrobionych):
    lista.append(input('Podaj coc chcesz zrobić: '))


def _kwadracik(element, lista, zbior_rzeczy_zrobionych):
    if element in zbior_rzeczy_zrobionych:
        return "[x]"
    return "[ ]"


def pokaz_liste(lista, zbior_rzeczy_zrobionych):
    for element in lista:
        print(f"{_kwadracik(element, lista, zbior_rzeczy_zrobionych)} {element}")


def oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych):
    if czy_lista_jest_zakazana:
        coss
    else:
        for i, element in enumerate(lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        zbior_rzeczy_zrobionych.add(lista[indeks_do_oznaczenia])


def usun_rzecz_do_zrobienia(lista, zbior_rzeczy_zrobionych):
    for i, element in enumerate(lista):
        print(f'{i+1}. {element}')
    indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
    del lista[indeks_do_usuniecia]


def ustaw_rzecz_na_poczatek(lista, zbior_rzeczy_zrobionych):
    for i, element in enumerate(lista):
        print(f'{i + 1}. {element}')
    indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
    element_na_poczatek = lista.pop(indeks_do_ustawienia_na_poczatek)
    lista.insert(0, element_na_poczatek)


def petla_glowna_programu():
    """
    Lista rzeczy do zorbienia Niebieska
    Lista rzeczy do zorbienia Czerwona
    :return:
    """
    while True:
        wypisz_menu()
        input('Na jakiej liscie chcesz operowac? (Niebieska, czy Czerwona): ')
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            dodaj_rzecz_do_zrobienia(lista_czerwona, zbior_rzeczy_zrobionych_czerwona)
        elif opcja == 2:
            oznacz_rzecz_jako_zrobiona(lista_niebieska, zbior_rzeczy_zrobionych_niebieska)
        elif opcja == 3:
            pokaz_liste(lista_niebieska, zbior_rzeczy_zrobionych_czerwona)
        elif opcja == 4:
            usun_rzecz_do_zrobienia(lista, zbior_rzeczy_zrobionych)
        elif opcja == 5:
            ustaw_rzecz_na_poczatek(lista, zbior_rzeczy_zrobionych)
        elif opcja == 6:
            return


petla_glowna_programu()
```



### Przerabianie na klasę
Jak wygląda zwykła funkcja:
```python
def oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych):
    for i, element in enumerate(lista):
        print(f'{i+1}. {element}')
    indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
    zbior_rzeczy_zrobionych.add(lista[indeks_do_oznaczenia])
```

Jak wygląda funkcja w klasie:
```python
    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])
```

Wersja przerobiona na używanie klasy:



### Program program_z_prosta_klasa.py

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
        self.lista = ['A', 'B', 'C', 'D']
        self.zbior_rzeczy_zrobionych = {'B'}


    def dodaj_rzecz_do_zrobienia(self):
        self.lista.append(input('Podaj co chcesz zrobić: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zrobionych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])


    def usun_rzecz_do_zrobienia(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
        del self.lista[indeks_do_usuniecia]


    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)


def petla_glowna_programu():
    lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia()
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            lista_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            lista_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            lista_rzeczy_do_zrobienia.pokaz_liste()
        elif opcja == 4:
            lista_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            lista_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            return


petla_glowna_programu()
```



Dodanie do init argumentu:



### Program program_z_prosta_klasa2

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

    def __init__(self, poczatkowa_liczba_pozycji):
        self.lista = []
        for i in range(poczatkowa_liczba_pozycji):
            self.lista.append(f'A-{i+1}')
        self.zbior_rzeczy_zrobionych = {'B'}

    def dodaj_rzecz_do_zrobienia(self):
        self.lista.append(input('Podaj co chcesz zrobić: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zrobionych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])


    def usun_rzecz_do_zrobienia(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
        del self.lista[indeks_do_usuniecia]


    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)


def petla_glowna_programu():
    lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia(poczatkowa_liczba_pozycji=6)
    # działa tak samo jak:
    # lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia(6)
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            lista_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            lista_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            lista_rzeczy_do_zrobienia.pokaz_liste()
        elif opcja == 4:
            lista_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            lista_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            return


petla_glowna_programu()
```



Dwie instacje klasy:



### Program program_z_prosta_klasa3

Kod programu:
```python
def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. zmien domyslna liste')
    print('7. Wyjdź z programu')


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

    def __init__(self, nazwa, poczatkowa_liczba_pozycji):
        self.nazwa = nazwa
        self.lista = []
        for i in range(poczatkowa_liczba_pozycji):
            self.lista.append(f'A-{i+1}')
        self.zbior_rzeczy_zrobionych = {'B'}

    def dodaj_rzecz_do_zrobienia(self):
        self.lista.append(input('Podaj co chcesz zrobić: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zrobionych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        print(f'Pokazuje zwartość listy o nazwie {self.nazwa}')
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])


    def usun_rzecz_do_zrobienia(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
        del self.lista[indeks_do_usuniecia]


    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)


def petla_glowna_programu():
    lista_rzeczy_czerwona = ListaRzeczyDoZrobienia(nazwa='Lista Czerwona', poczatkowa_liczba_pozycji=6)
    lista_rzeczy_niebieska = ListaRzeczyDoZrobienia(nazwa='Lista Niebieska', poczatkowa_liczba_pozycji=3)
    lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
    # działa tak samo jak:
    # lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia(6)
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            lista_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            lista_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            lista_rzeczy_do_zrobienia.pokaz_liste()
        elif opcja == 4:
            lista_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            lista_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            odp = input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona): ')
            if odp.startswith('C'):
                lista_rzeczy_do_zrobienia = lista_rzeczy_czerwona
            else:
                lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
        elif opcja == 7:
            return


petla_glowna_programu()
```



Zdanie:
 - po zmienie koloru listy napisz na jaki kolor lista została zmieniona
 - pozwól na pisanie czerwona lista z małej litery przy wyborze

Dwa kody które robią to samo:

```python
odp = str.lower(input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona): '))

odp = (input('Na której liście chcesz operować? ([N]iebieska, Czerwona):').lower())

```







### Program jak_jest_podawany_self

Kod programu:
```python
"""
2 notacje funkcyjne, 2 sposoby wywołania funkcji klasy:

odp = str.lower(input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona): '))

odp = (input('Na której liście chcesz operować? ([N]iebieska, Czerwona):').lower())

"""


zmienna1 = 'tesk'
zmienna2 = ['tesk']


class strNaPorzeby_kursu:

    def lower(self):
        return 'abc'

tekst = 'NORMANY Tekst'
print('lower tekst = ', tekst.lower())
print('lower tekst = ', str.lower(tekst))

tekstWlasny = strNaPorzeby_kursu()
print('lower tekstWlasny = ', tekstWlasny.lower())
print('lower tekstWlasny = ', strNaPorzeby_kursu.lower(tekstWlasny))

print('jest taka funkcja jak lower ', strNaPorzeby_kursu.lower)
```






### Program program_z_prosta_klasa4

Kod programu:
```python
def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. zmien domyslna liste')
    print('7. Wyjdź z programu')


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

    def __init__(self, nazwa, poczatkowa_liczba_pozycji):
        self.nazwa = nazwa
        self.lista = []
        for i in range(poczatkowa_liczba_pozycji):
            self.lista.append(f'A-{i+1}')
        self.zbior_rzeczy_zrobionych = {'B'}

    def dodaj_rzecz_do_zrobienia(self):
        self.lista.append(input('Podaj co chcesz zrobić: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zrobionych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        print(f'Pokazuje zwartość listy o nazwie {self.nazwa}')
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])


    def usun_rzecz_do_zrobienia(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
        del self.lista[indeks_do_usuniecia]


    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)


class ZakazaneRzeczyDoZrobienia(ListaRzeczyDoZrobienia):

    def oznacz_rzecz_jako_zrobiona(self):
        print('Nie wolno odznaczać w liście zakazanej')


def petla_glowna_programu():
    lista_rzeczy_czerwona = ListaRzeczyDoZrobienia(nazwa='Lista Czerwona', poczatkowa_liczba_pozycji=6)
    lista_rzeczy_niebieska = ListaRzeczyDoZrobienia(nazwa='Lista Niebieska', poczatkowa_liczba_pozycji=3)
    lista_zakazana = ZakazaneRzeczyDoZrobienia(nazwa='Lista Zakazana', poczatkowa_liczba_pozycji=2)
    lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
    # działa tak samo jak:
    # lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia(6)
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            lista_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            lista_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            lista_rzeczy_do_zrobienia.pokaz_liste()
        elif opcja == 4:
            lista_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            lista_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            odp = input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona, Zakazana): ')
            if odp.startswith('Z'):
                lista_rzeczy_do_zrobienia = lista_zakazana
            elif odp.startswith('C'):
                lista_rzeczy_do_zrobienia = lista_rzeczy_czerwona
            else:
                lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
        elif opcja == 7:
            return


petla_glowna_programu()
```



zadanie: 

stwórz klasę TrojkatnaListaRzeczy do zrobienia, która jest klasą dziecko naczej początkowej klasy

lista niebieska ma być instacją tej klasy

zadanie:
do klasy zakazane rzeczy do zrobienia, zmień działanie dodaj rzeczy do zrobienia, aby dodana rzeczy do zrobienia miała sufix " - ale nie wolno", wykorzystując super wywołanie




### Program program_z_prosta_klasa5

Kod programu:
```python
def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. zmien domyslna liste')
    print('7. Wyjdź z programu')


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

    def __init__(self, nazwa, poczatkowa_liczba_pozycji):
        self.nazwa = nazwa
        self.lista = []
        for i in range(poczatkowa_liczba_pozycji):
            self.lista.append(f'A-{i+1}')
        self.zbior_rzeczy_zrobionych = {'B'}

    def dodaj_rzecz_do_zrobienia(self):
        self.lista.append(input('Podaj co chcesz zrobić: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zrobionych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        print(f'Pokazuje zwartość listy o nazwie {self.nazwa}')
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])


    def usun_rzecz_do_zrobienia(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Ktory element usunac: ')) - 1
        del self.lista[indeks_do_usuniecia]


    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Ktory element usunac: ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)


class ZakazaneRzeczyDoZrobienia(ListaRzeczyDoZrobienia):

    def __init__(self, poczatkowa_liczba_pozycji):
        super(ZakazaneRzeczyDoZrobienia, self).__init__(nazwa='Lista Zakazana',
                                                        poczatkowa_liczba_pozycji=poczatkowa_liczba_pozycji)

    def oznacz_rzecz_jako_zrobiona(self):
        print('Nie wolno odznaczać w liście zakazanej')

    def _kwadracik(self, element):
        wartosc_z_klasy_rodzica = super(ZakazaneRzeczyDoZrobienia, self)._kwadracik(element)
        return f'* {wartosc_z_klasy_rodzica} *'


def petla_glowna_programu():
    lista_rzeczy_czerwona = ListaRzeczyDoZrobienia(nazwa='Lista Czerwona', poczatkowa_liczba_pozycji=6)
    lista_rzeczy_niebieska = ListaRzeczyDoZrobienia(nazwa='Lista Niebieska', poczatkowa_liczba_pozycji=3)
    lista_zakazana = ZakazaneRzeczyDoZrobienia(poczatkowa_liczba_pozycji=2)
    lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
    # działa tak samo jak:
    # lista_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia(6)
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            lista_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            lista_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobiona()
        elif opcja == 3:
            lista_rzeczy_do_zrobienia.pokaz_liste()
        elif opcja == 4:
            lista_rzeczy_do_zrobienia.usun_rzecz_do_zrobienia()
        elif opcja == 5:
            lista_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            odp = input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona, Zakazana): ')
            if odp.startswith('Z'):
                lista_rzeczy_do_zrobienia = lista_zakazana
            elif odp.startswith('C'):
                lista_rzeczy_do_zrobienia = lista_rzeczy_czerwona
            else:
                lista_rzeczy_do_zrobienia = lista_rzeczy_niebieska
        elif opcja == 7:
            return


petla_glowna_programu()
```







### Program przyklad_pygame1

Kod programu:
```python
import pygame

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255).

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image .fill(WHITE)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0, -2)
            elif event.key == pygame.K_s:
                rect.move_ip(0, 2)
            elif event.key == pygame.K_a:
                rect.move_ip(-2, 0)
            elif event.key == pygame.K_d:
                rect.move_ip(2, 0)

    screen.fill(BLACK)
    screen.blit(image, rect)
    pygame.display.update()  # Or pygame.display.flip()
```





### Program przyklad_pygame2

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

#### Create a canvas on which to display everything ####
window = (400, 400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background, (0, 255, 255), (20, 20, 40, 40))
pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
pygame.draw.rect(background, (255, 100, 255), (220, 120, 50, 50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background, (0, 0))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()

```





### Program przyklad_pygame3.py

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

#### Create a canvas on which to display everything ####
window = (400, 400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

x = 220 + 100
y = 120 + 70

def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
    pygame.draw.rect(background, (0, 255, 0), (x, y, 50, 50))

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 40
            elif event.key == pygame.K_s:
                y += 40
    paint()
#### Update the the display and wait ####

pygame.quit()

```





### Program przyklad_pygame4

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

x = 220 + 100
y = 120 + 70

krok_x = 2

def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
    pygame.draw.rect(background, (0, 255, 0), (x, y, 50, 50))

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 40
            elif event.key == pygame.K_s:
                y += 40
    paint()
    x += krok_x
    if x < 0:
        krok_x = -krok_x
    elif x > SZEROKOSC_OKNA:
        krok_x = -krok_x

pygame.quit()

```





### Program przyklad_pygame5

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

x = 220 + 100
y = 120 + 70

krok_x = 2
krok_y = 3

def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))
    pygame.draw.rect(background, (0, 255, 0), (x, y, 50, 50))

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 40
            elif event.key == pygame.K_s:
                y += 40
    paint()
    x += krok_x
    if x < 0:
        krok_x = -krok_x
        x = 0
    elif x + 50 > SZEROKOSC_OKNA:
        krok_x = -krok_x
        x = SZEROKOSC_OKNA - 50
    y += krok_y
    if y < 0:
        krok_y = -krok_y
        y = 0
    elif y + 50 > WYSOKOSC_OKNA:
        krok_y = -krok_y
        y = WYSOKOSC_OKNA - 50

pygame.quit()

```





### Program przyklad_pygame5_z_klasa

Kod programu:
```python
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

SZEROKOSC_OKNA = 400
WYSOKOSC_OKNA = 400
window = (SZEROKOSC_OKNA, WYSOKOSC_OKNA)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)


class PoruszajacySieKwadracik:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.krok_x = 2
        self.krok_y = 3

    def paint(self):
        pygame.draw.rect(background, (0, 255, 0), (self.x, self.y, 50, 50))

    def update(self):
        self.x += self.krok_x
        if self.x < 0:
            self.krok_x = -self.krok_x
            self.x = 0
        elif self.x + 50 > SZEROKOSC_OKNA:
            self.krok_x = -self.krok_x
            self.x = SZEROKOSC_OKNA - 50
        self.y += self.krok_y
        if self.y < 0:
            self.krok_y = -self.krok_y
            self.y = 0
        elif self.y + 50 > WYSOKOSC_OKNA:
            self.krok_y = -self.krok_y
            self.y = WYSOKOSC_OKNA - 50


kwadracik1 = PoruszajacySieKwadracik(120, 220)


def paint():
    pygame.draw.rect(background, (255, 255, 255), (0, 0, *window))

    pygame.draw.rect(background, (0, 255, 255), (20, 20, 30, 30))
    pygame.draw.rect(background, (255, 0, 255), (120, 120, 50, 50))

    kwadracik1.paint()

    screen.blit(background, (0, 0))
    pygame.display.flip()

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         y -= 40
        #     elif event.key == pygame.K_s:
        #         y += 40
    paint()

    kwadracik1.update()

pygame.quit()

```



