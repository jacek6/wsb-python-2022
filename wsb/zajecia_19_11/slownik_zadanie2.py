from typing import List


def zlicz_slowa(lista_slow: List[str]):
    slownik_wystapien = {}
    for slowo in lista_slow:
        if slowo in slownik_wystapien:
            slownik_wystapien[slowo] = slownik_wystapien[slowo] + 1
        else:
            slownik_wystapien[slowo] = 1
    return slownik_wystapien

print(zlicz_slowa(['ala', 'ma', 'kota', 'ala']))