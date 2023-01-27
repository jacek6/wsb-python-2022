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