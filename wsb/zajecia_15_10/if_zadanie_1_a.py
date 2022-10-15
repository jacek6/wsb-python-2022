liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))

zarobki_netto = 0.8 * zarobki_brutto + 500 * liczba_dzieci
print('Twoje zarobki netto to: ', zarobki_netto, ' zł')