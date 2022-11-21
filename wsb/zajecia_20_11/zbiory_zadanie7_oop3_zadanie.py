

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