lista = [-88, -3, 11, 23, 56, 78, 98, 154, 176, 198, 275, 375, 416, 524, 564, 627, 738, 873, 924]

element_do_zalezienia = 0

l = 0
r = len(lista) - 1
while l + 1 < r:
    print('Szukam w liście: ', lista[l:r])

    c = (l + r) // 2

    if lista[c] == element_do_zalezienia:
        print('Znaleziono element n indeksie ', c)
        break
    if element_do_zalezienia < lista[c]:
        r = c
    else:
        l = c

if lista[c] != element_do_zalezienia:
    print("Element miałby indeks ", c)