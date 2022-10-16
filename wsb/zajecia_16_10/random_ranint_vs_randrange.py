import random

# randint może zwrócić 5 (podany górny zakres)
for i in range(15):
    print('randint = ', random.randint(1, 5))
print()

# randrange nigdy nie zwrócic podanego górnego zakresu
# randrange może przyjść krok locsowania = co ile losować
for i in range(15):
    # print('randrange ', random.randrange(1, 100, 20))
    print('randrange ', random.randrange(1, 5))