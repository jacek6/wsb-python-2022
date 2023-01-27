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