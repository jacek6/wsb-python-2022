
zarobki = ['5001PLN', '972EUR', '1043USD', '1897PLN', '693EUR', '790USD']

zarobki_netto = []

for z in zarobki:
    kwota = float(z[:-3])
    waluta = z[-3:]
    print(kwota, waluta)

    if waluta == 'PLN':
        kwota_w_pln = kwota
    elif waluta == 'EUR':
        kwota_w_pln = kwota * 4.71
    elif waluta == 'USD':
        kwota_w_pln = kwota * 4.55
    else:
        print(f'BŁĄD nie znana waluta: {waluta}')
    print('Zarobki brutto w PLN ', kwota_w_pln)

    podatek = 0
    if kwota_w_pln > 3000:
        podatek = kwota_w_pln * 0.1
    if kwota_w_pln > 5000:
        podatek = kwota_w_pln * 0.2
    print('podatek dla kwoty PLN ', kwota_w_pln, ' wynosi ', podatek)
    netto = kwota_w_pln - podatek

    zarobki_netto.append(netto)

print('zarobki_w_pln = ', zarobki_netto)
