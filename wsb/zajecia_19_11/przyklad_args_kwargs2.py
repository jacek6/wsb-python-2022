
def wypisz(a, b, c):
    print('a ', a, ', b ', b, ', c', c)

wypisz(a='A', b='B', c='C')
wypisz(b='B', a='A', c='C')
wypisz(c='C', b='B', a='A')


wypisz('A', b='B', c='C')
wypisz('A', c='C', b='B')

def wypisz2(*args, **kwargs):
    print('args ', args)
    print('kwargs ', kwargs)

wypisz2('A', c='C', b='B')