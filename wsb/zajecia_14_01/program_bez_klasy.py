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