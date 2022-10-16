import random
def rzuc_kostka():
    return random.randint(1, 6)

def sytuacja1():
    wynik_rzutu = rzuc_kostka()
    return wynik_rzutu >= 4

sukces = 0
for i in range (10):
    if sytuacja1():
        print(sytuacja1())
        sukces += 1
print(sukces)