NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()
#  Sprawdźmy poprawność danych:
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.
if chorzy_rok.intersection(chorzy_miesiac) == chorzy_miesiac:
    print('każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.')
else:
    print('BŁĄD !')

# nikt nie powinien mieszkać jednocześnie w Centrum i na Krzykach – jeśli tak, trzeba usunąć.
if krzyki.intersection(centrum):
    print("Ktoś mieszka na krzykach i w centrum: ", krzyki.intersection(centrum))

# każdy: chory, zdrowy, z Krzyków i z Centrum, powinien być w bazie NFZ, jeśli nie ma, trzeba dopisać.
osoby_do_dopisania_do_NFZ = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    if NFZ.intersection(zbior) != zbior:
        kto_jest_poza_nfz = zbior.difference(NFZ.intersection(zbior))
        assert NFZ.union(kto_jest_poza_nfz).intersection(zbior) == zbior
        print("ktoś jest poza bazą NFZ, ze zbioru: ", nazwa, " te osoby to ", kto_jest_poza_nfz)
        osoby_do_dopisania_do_NFZ = osoby_do_dopisania_do_NFZ.union(kto_jest_poza_nfz)

print("dopisze do NFZ osoby: ", osoby_do_dopisania_do_NFZ)
NFZ = NFZ.union(osoby_do_dopisania_do_NFZ)

print('teraz NFZ to: ', NFZ)