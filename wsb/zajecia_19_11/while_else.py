odp = input('Podaj liczbe parzystą lub Q żeby wyjść: ')

while odp != 'Q':
    if int(odp) % 2 == 0:
        print('jest to liczba parzysta')
    else:
        print('nie jest to liczba parzysta - BŁĄD')
        break
    odp = input('Podaj liczbe parzystą lub Q żeby wyjść: ')
else:
    print('wykonuję else')
    print('prawidłowe zakończenie programu bez błędu')