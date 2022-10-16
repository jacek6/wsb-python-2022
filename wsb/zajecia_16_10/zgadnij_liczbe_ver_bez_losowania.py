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