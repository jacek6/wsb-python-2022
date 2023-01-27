lista = [8, 2, 5, 1, 78, 2, -90, -3, -1]

print(sorted(lista))
# print(sorted(lista, reverse=True))


def mysl_o_innej_wartosci(wartosc_z_listy):
    return wartosc_z_listy * wartosc_z_listy

print(sorted(lista, key=mysl_o_innej_wartosci))

print(sorted(lista, key=lambda wartosc_z_listy: wartosc_z_listy * wartosc_z_listy))
print(sorted(lista, key=lambda x: x * x))

# funkcja jako wartość zmiennej
mysl_o_innej_wartosci2 = lambda wartosc_z_listy: wartosc_z_listy * wartosc_z_listy

print(mysl_o_innej_wartosci(-2))
print(mysl_o_innej_wartosci2(-2))

funckja_mnozaca_w_jendej_lini = lambda a, b, c: a * b * c
print(funckja_mnozaca_w_jendej_lini(2, 3, 4))

def funckja_mnozaca_normna(a, b, c):
    return a * b * c