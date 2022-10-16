haslo = 'abc123!'

# cyfry = ['0', '1', ...]
cyfry = '1234567890'
znaki_specjalne = '!@#$%^&*()-+{}|:"<>?,./;[]\\'

czy_jest_cyfra = False
for cyfra in cyfry:
    if cyfra in haslo:
        czy_jest_cyfra = True
        break

czy_jest_znak_specjalny = False
for znak in znaki_specjalne:
    if znaki_specjalne in haslo:
        czy_jest_znak_specjalny = True
        break

if czy_jest_cyfra and czy_jest_znak_specjalny and len(haslo) > 6:
    print('haslo jest silne')
else:
    print('haslo jest slabe')