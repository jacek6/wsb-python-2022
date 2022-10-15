liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))


if zarobki_brutto < 3000:
    zarobki_netto = zarobki_brutto
elif zarobki_brutto < 5000:
    zarobki_netto = zarobki_brutto * 0.9
else:
    zarobki_netto = zarobki_brutto * 0.8

if liczba_dzieci >= 2:
    zarobki_netto += 500
if liczba_dzieci >= 3:
    zarobki_netto += 500

print('Twoje zarobki netto to: ', zarobki_netto, ' zł')