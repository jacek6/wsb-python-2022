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