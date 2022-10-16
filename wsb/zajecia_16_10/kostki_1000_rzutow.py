import random

sukcesy_przy_rzucie_1_koscia = 0
sukcesy_przy_rzucie_3_kostkami = 0

for nr_powtorzenia_testu in range(1000):
    pierwsza_kostka = random.randint(1, 6)
    kostki = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    if pierwsza_kostka >= 4:
        # print('sukces przy rzucie 1 kostka')
        sukcesy_przy_rzucie_1_koscia += 1

    if 6 in kostki:
        # print('sukces przu rzucami wieloma kostkami')
        sukcesy_przy_rzucie_3_kostkami += 1

if sukcesy_przy_rzucie_1_koscia > sukcesy_przy_rzucie_3_kostkami:
    print('jest wiecej sukcesow przy rzucie 1 koscia')
elif sukcesy_przy_rzucie_1_koscia == sukcesy_przy_rzucie_3_kostkami:
    print('jest to tak samo prawdopodobne')
else:
    print('jest wiecej sukcesow przy rzucie 3 kostkami')

print('sukcesy_przy_rzucie_1_koscia = ', sukcesy_przy_rzucie_1_koscia)
print('sukcesu_przy_rzucie_3_kostkami = ', sukcesy_przy_rzucie_3_kostkami)

