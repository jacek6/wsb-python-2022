haslo = 'aBa123!'

znaki_specjalne = '!@#$%^&*()-+{}|:"<>?,./;[]\\'

czy_jest_cyfra = False
czy_jest_znak_specjalny = False
czy_jest_litera_duza = False
czy_jest_litera_mala = False
for ch in haslo:
    if ch.isdigit():
        czy_jest_cyfra = True
    if ch.isalpha():
        if ch.isupper():
            czy_jest_litera_duza = True
        else:
            czy_jest_litera_mala = True

    if ch in znaki_specjalne:
        czy_jest_znak_specjalny = True

if czy_jest_cyfra and czy_jest_znak_specjalny and czy_jest_litera_mala and czy_jest_litera_duza\
        and len(haslo) > 6:
    print('haslo jest silne')
else:
    print('haslo jest slabe')