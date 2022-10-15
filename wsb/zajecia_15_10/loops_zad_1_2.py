lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]

for i in range ( len(lista) ):
    if lista[i] % 2 == 0 or lista[i] > 10:
        print('wykonanie petli nr ', i, ' wartosc listy = ', lista[i])
