import sys


def wymus_zgode_na_warunki():
    while True:
        odp = input('Czy zgadzasz sie na warunki działania programu (tak/nie/q wyjśćie): ')
        if odp == 'tak':
            return
        if odp == 'nie':
            print('Zgodna na warunki jest wymagana do dalszego działania')
            continue
        print('sprawdzam czy trzeba wyjść')
        if odp == 'q':
            sys.exit(0)

wymus_zgode_na_warunki()
print('program leci dalej')