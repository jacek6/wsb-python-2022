import random

lista_kostek = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
print(lista_kostek)

if 1 in lista_kostek:
    print('jedna z kostek wyrzucila 1')
else:
    print('zadna kostka nie wyrzucila 1')