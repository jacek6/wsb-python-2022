NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

wszystkie_zbiory = {'NFZ': NFZ, 'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}

pesel = int(input('Podaj pesel: '))

if pesel % 2 == 0:
    print('podany pesel ', pesel, ' należy do kobiety')
else:
    print('podany pesel ', pesel, ' należy do mężczyzny')


for nazwa, zbior in wszystkie_zbiory.items():
    if pesel in zbior:
        print('podany pesel ', pesel, ' wystepuje w zbiorze ', nazwa, ' ten zbiór to ', zbior)
