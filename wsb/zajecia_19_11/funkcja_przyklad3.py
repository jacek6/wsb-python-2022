from typing import List


def odczytaj_liste_stringow(nazwa_pliku: str) -> List[str]:
    wynik = []
    with open(nazwa_pliku, 'r') as fp:
        for linia_w_pliku in fp:
            wynik.append(linia_w_pliku)
    return wynik

# def zapisz_do_pliku_linia_obok_lini(nazwa_pliku_do_zapisania: str, lista_lini: List[str]):
def zapisz_do_pliku_linia_obok_lini(nazwa_pliku_do_zapisania = 'plik_do_zapisania.txt', lista_lini=['domyslan linia']):
    with open(nazwa_pliku_do_zapisania, 'w') as fp:
        for lini in lista_lini:
            fp.write(lini.rstrip())
            fp.write(' ')

print('Odczytanie pliku ', odczytaj_liste_stringow('plik.txt'))
print('Ładne odczytanie pliku')
for linia in odczytaj_liste_stringow('plik.txt'):
    print('Linia zwrócona z funkcji: ', linia)

zapisz_do_pliku_linia_obok_lini('plik_wynikowy.txt', odczytaj_liste_stringow('plik.txt'))
zapisz_do_pliku_linia_obok_lini('abc.txt', ['a', 'b', 'cd'])

zapisz_do_pliku_linia_obok_lini()