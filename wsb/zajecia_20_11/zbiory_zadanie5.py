from functools import reduce

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345,  6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

wszystkie_zbiory = {'NFZ': NFZ, 'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}

def czy_pesel_ok(pesel: int) -> bool:
    return pesel >= 10**3 and pesel < 10**4

def przyjmuj_pesel():
    while True:
        i = input('Podaj pesel: ').strip()
        try:
            potencjalny_pesel = int(i)
            if not czy_pesel_ok(potencjalny_pesel):
                print('Pesel musi mieć 4 znaki')
                continue
            return potencjalny_pesel
        except ValueError:
            print('Proszę podać prawidłowy pesel')

zbior_wszystkich_zlych_peseli = {p for p in reduce(lambda a, b: a.union(b), wszystkie_zbiory.values()) if not czy_pesel_ok(p)}
print('zbior_wszystkich_zlych_peseli ', zbior_wszystkich_zlych_peseli)

pesel = przyjmuj_pesel()

if pesel % 2 == 0:
    print('podany pesel ', pesel, ' należy do kobiety')
else:
    print('podany pesel ', pesel, ' należy do mężczyzny')



for nazwa, zbior in wszystkie_zbiory.items():
    zbior_zlych_peseli = {p for p in zbior if not czy_pesel_ok(p)}
    if zbior_zlych_peseli:
        print('znaleziono złe pesele: ', zbior_zlych_peseli)
    if pesel in zbior:
        print('podany pesel ', pesel, ' wystepuje w zbiorze ', nazwa, ' ten zbiór to ', zbior)
