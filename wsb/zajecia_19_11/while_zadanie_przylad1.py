
while True:
    pesel = input('Podaj PESEL: ')

    suma_cyfr = 0
    for znak_pesel in pesel:
        suma_cyfr += int(znak_pesel)
    if suma_cyfr % 3 == 0 or suma_cyfr % 4 == 0:
        print('pesel prawidłowy')
        break
    print('PESEL nie jest poprawny, proszę podać go jeszcze raz')