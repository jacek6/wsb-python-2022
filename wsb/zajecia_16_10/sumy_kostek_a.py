import random

sukcesy_wyrzuconych_sum = [0] * 13

for nr_powtorzenia in range(1000):
    wynik_kostki_1 = random.randint(1, 6)
    wynik_kostki_2 = random.randint(1, 6)

    wyrzucona_suma = wynik_kostki_1 + wynik_kostki_2
    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')