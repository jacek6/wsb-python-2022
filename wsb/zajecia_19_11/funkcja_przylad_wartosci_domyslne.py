
def wypisz(a, b=20, c=30):
    print('podano: ', a, b, c)

# błąd:
# def wypisz2(x, a=10, b, c):
#     print('podano: ', a, b, c)


wypisz(1, 2, 3)

wypisz(1, 2)

wypisz(1)

def wypisz_smart(a, b=None):
    if b:
        print('podano ', a, b)
    else:
        print('podano ', a)

wypisz_smart(100, 200)
wypisz_smart(100)
