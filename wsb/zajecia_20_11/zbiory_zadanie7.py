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

def petla_glowna_programu():
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            print('opcja 1')
        elif opcja == 2:
            print('opcja 2')
        elif opcja == 3:
            pass
        elif opcja == 4:
            pass
        elif opcja == 5:
            pass
        elif opcja == 6:
            return

petla_glowna_programu()