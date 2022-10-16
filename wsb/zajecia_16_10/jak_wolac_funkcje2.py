import random
def rzuc_kostka():
    print('RZUT')
    return random.randint(1, 6)

def sytuacja1():
    wynik_rzutu = rzuc_kostka()
    return wynik_rzutu >= 4

sukces = 0
for i in range (10):
    wynik_sytuacj1 = sytuacja1()
    if wynik_sytuacj1:
        print(wynik_sytuacj1)
        sukces += 1
print(sukces)