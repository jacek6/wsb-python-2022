haslo = 'abc123'

# cyfry = ['0', '1', ...]
cyfry = '1234567890'

czy_jest_cyfra = False
for cyfra in cyfry:
    if cyfra in haslo:
        czy_jest_cyfra = True
        break

if czy_jest_cyfra:
    print('haslo ma cyfre')
else:
    print('haslo musi miec cyfre')