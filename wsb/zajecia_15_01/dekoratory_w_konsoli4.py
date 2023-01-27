lista_opcji = []

def dodaj_jako_opcje_programu(funckja):
    lista_opcji.append((funckja.__name__, funckja))
    return funckja

@dodaj_jako_opcje_programu
def pokaz_liste():
    print('pokazuje liste..')

@dodaj_jako_opcje_programu
def dodaj_do_listy():
    print('dodaje do listy')

for i, (nazwa, _) in enumerate(lista_opcji):
    print(f'{i+1}. {nazwa}')
odp = int(input('Co chcesz zrobić?: '))
funckcja_do_wykonania = lista_opcji[odp-1][1]
funckcja_do_wykonania()