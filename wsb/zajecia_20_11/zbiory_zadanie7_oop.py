

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