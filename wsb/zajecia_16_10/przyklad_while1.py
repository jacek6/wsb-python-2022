licznik = 0
while True:
    licznik += 1
    print('Licznik ma teraz wartość ', licznik)
    if licznik > 5:
        print('Licznik jest za duży, przerywamy')
        break
print('Koniec programu')