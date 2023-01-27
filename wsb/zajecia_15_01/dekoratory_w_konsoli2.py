def printuj(orginalna_funckja):
    def _nowa_funkcja(*args, **kwargs):
        print(f'dekortor otoczył wywołanie z {args, kwargs}')
        return orginalna_funckja(*args, **kwargs)
    return _nowa_funkcja

@printuj
def funkcja(a, b, c):
    return a + b + c

def dekorator_dodaj_wszystko(orginalna_funckja):
    def _nowa_funkcja(*args):
        suma = sum(args)
        return orginalna_funckja(suma)
    return _nowa_funkcja

print(funkcja(2, 3, 9))

@printuj
@dekorator_dodaj_wszystko
@printuj
def wypisz_jedna_liczbe(x):
    print(f'x = {x}')

wypisz_jedna_liczbe(88)
wypisz_jedna_liczbe(88, 12)