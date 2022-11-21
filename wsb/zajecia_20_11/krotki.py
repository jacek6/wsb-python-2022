
lista = [1, 2, 3]

krotka = (1, 2, 3)

print('lista ', lista)
print('krotka ', krotka)

krotka2 = 10, 20, 30

print('krotka2 ', krotka2)

# x = lista[0]
# y = lista[1]
# z = lista[2]

x, y, z = krotka2
print('x ', x, ', y ', y, ', z ', z)

x, y, _ = krotka
print('x ', x, ', y ', y)
