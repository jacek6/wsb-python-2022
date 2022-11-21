
def oblicz_pole_trojkata(dlugosc_podstawy, wysokosc):
    return dlugosc_podstawy * wysokosc / 2

def odczytaj_liste_stringow(nazwa_pliku):
    wynik = []
    with open(nazwa_pliku, 'r') as fp:
        for linia_w_pliku in fp:
            wynik.append(linia_w_pliku)
    return wynik

print('Pole trojkta ', oblicz_pole_trojkata(4, 5))

print('Odczytanie pliku ', odczytaj_liste_stringow('plik.txt'))
print('Ładne odczytanie pliku')
for linia in odczytaj_liste_stringow('plik.txt'):
    print('Linia zwrócona z funkcji: ', linia)


with open('plik.txt', 'r') as wskaznikiem_do_pliku:
    for linia in wskaznikiem_do_pliku:
        print("Linia odczytana z pliku ", linia)
