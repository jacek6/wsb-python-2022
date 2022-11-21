 # Żeńskie Numery PESEL mają ostatnią cyfrę parzystą, męskie – nieparzystą.
 # Zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ).

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

def podziel_zbiory(zbior):
    damski = {e for e in zbior if e % 2 == 0}
    meski = {e for e in zbior if e % 2 == 1}
    return damski, meski

zbior_wszystkich = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    damski, meski = podziel_zbiory(zbior)
    print()
    print('W zbiorze ', nazwa)
    print('kobiety to ', damski)
    print('mężczyźni to ', meski)

    zbior_wszystkich = zbior_wszystkich.union(zbior)

damski, meski = podziel_zbiory(zbior_wszystkich)
print('wszystkich kobiet jest ', len(damski))
print('wszystkich mężczyzn jest ', len(meski))