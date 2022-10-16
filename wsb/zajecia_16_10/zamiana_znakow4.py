tekst = 'ala ma kota! oraz psa. the end'
# tekst[0] = 'A'

znaki_nowego_tesktu = []
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    znaki_nowego_tesktu.append(ch)
print()
print('orginalny teskst ', tekst)
print('znaki_nowego_tesktu = ', znaki_nowego_tesktu)
nowy_tekst = ''.join(znaki_nowego_tesktu)  # składa tekst z listy tesktów
print('nowy_tekst ', nowy_tekst)
print()
print('koniec programu')