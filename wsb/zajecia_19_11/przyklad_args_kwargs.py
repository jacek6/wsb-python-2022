
def wypisz(a, b=None, c=None, d=None):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
    if d:
        print(d)
    print()

wypisz(1)
wypisz(1, 2, 3, 4)

def wypisz2(*args):
    print('Podano args: ', args)
    for arg in args:
        print(arg)

wypisz2(1)
wypisz2(1, 2, 3, 4)
wypisz2(1, 2, 3, 4, 5, 6, 7, 344, 34, 23, 'b', 'mm')

lista = [1, 31]
wypisz2(*lista)