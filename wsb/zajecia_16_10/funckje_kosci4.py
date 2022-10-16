import random


def rzuc_kostka():
    return random.randint(1, 6)


def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    if wynik_rzutu >= 4:
        return True
    else:
        return False

def sytuacja2_czy_jest_sukces():
    wyniki_rzutow = [rzuc_kostka(), rzuc_kostka(), rzuc_kostka()]
    if 6 in wyniki_rzutow:
        return True
    else:
        return False

sukcesy_stytuacji1 = 0
sukcesy_stytuacji2 = 0

for i in range(1000):
    if sytuacja1_czy_jest_sukces():
        sukcesy_stytuacji1 += 1
    if sytuacja2_czy_jest_sukces():
        sukcesy_stytuacji2 += 1

if sukcesy_stytuacji2 > sukcesy_stytuacji1:
    print('bardziej prawdopodobna jest sytuacja 2')
else:
    print('bardziej prawdopodobna jest sytuacja 1')
print('sukcesy_stytuacji1 = ', sukcesy_stytuacji1, '    sukcesy_stytuacji2 = ', sukcesy_stytuacji2)

