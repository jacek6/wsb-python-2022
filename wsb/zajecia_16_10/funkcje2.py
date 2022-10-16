odp = input('Czy chcesz się przywitać? (tak/nie): ')  #tak

def przywitaj_sie():
    print('Dzień dobry, witam.')

def ile_to_2_plus_2():
    return 4

print('decyzja co zrobić')

if odp == 'tak':
    przywitaj_sie()

print('2 + 2 = ', ile_to_2_plus_2())

wynik = ile_to_2_plus_2()
print('wynik = ', wynik)
