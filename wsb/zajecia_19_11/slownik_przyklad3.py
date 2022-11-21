kursy_walut_do_PLN = {'PLN': 1, 'EUR' : 4.6, 'USD' : 4.5, 'BTC' : 1000000}

zarobki = ['5001PLN', '972EUR', '1043USD', '1897CHF', '693EUR', '790USD']

for z in zarobki:
    kwota = float(z[:-3])
    waluta = z[-3:]
    print(kwota, waluta)

    if waluta in kursy_walut_do_PLN:
        kwota_w_pln = kwota * kursy_walut_do_PLN[waluta]
    else:
        kwota_w_pln = '?'

    print(z, ' -> ', kwota_w_pln)
