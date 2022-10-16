tekst = 'ala ma kota! oraz psa. the end'
# tekst[0] = 'A'

nowy_tekst = ''
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    nowy_tekst += ch
    print('stworzylem tekst: ', nowy_tekst)
print()
print('orginalny teskst ', tekst)
print('zmieniony teskst ', nowy_tekst)
print()
print('koniec programu')