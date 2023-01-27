def dekorator(funkcja):
    if 'cicha' in funkcja.__name__:
        return funkcja
    def _nowa_funkcja(*args, **kwargs):
        print(f'wywołano: {funkcja.__name__}')
        return funkcja(*args, **kwargs)
    return _nowa_funkcja

@dekorator
def funkcja_sumujaca(a, b):
    return a + b

@dekorator
def cicha_funkcja_sumujaca(a, b):
    return a + b

@dekorator
def mnozenie(a, b, c):
    return a * b * c

print(funkcja_sumujaca(1, 2))
print(cicha_funkcja_sumujaca(1, 2))
print(mnozenie(1, 2, 3))