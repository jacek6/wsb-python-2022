lista = [-4, 56, -7, 66, 102, 9]

print(sorted(lista, key=lambda x: x * x))

funkcja_jako_zmienna = lambda x: x * x

def funkcja(a, b):
    return a + b

def funkcja2_(a, b):
    return 2 * funkcja(a, b)

funkcja2 = lambda a, b: 2 * funkcja(a, b)

print(funkcja2(2, 3))
print(funkcja2_(2, 3))


def dekorator(orginalna_funckja):
    return lambda a, b: 2 * orginalna_funckja(a, b)

@dekorator
def funkcja(a, b):
    return a + b

# funkcja = dekorator(funkcja)

print(funkcja(2, 3))

def printuj(orginalna_funckja):
    def _nowa_funkcja(a, b):
        print(f'dekortor otoczył wywołanie z {a, b}')
        return orginalna_funckja(a, b)
    return _nowa_funkcja

@printuj
def funkcja(a, b):
    return a + b

print(funkcja(2, 3))