import random

ile_razy_rzucic_koscia = int(input('Ile razy rzucic koscia: '))  # 11

sukcesy_wyrzuconych_sum = [0] * ile_razy_rzucic_koscia * 7

for nr_powtorzenia in range(10000):
    wyrzucona_suma = 0
    for rzut_kostka in range(ile_razy_rzucic_koscia):
        wyrzucona_suma += random.randint(1, 6)

    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartosc = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartosc:
        maksymalna_wartosc = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, ' wyrzucono ja ', maksymalna_wartosc, ' razy')