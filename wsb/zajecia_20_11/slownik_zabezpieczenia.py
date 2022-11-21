from collections import defaultdict

slownik = {}

print(slownik.get('a'))
print(slownik.get('a', 'wartosc gdy nie zjadziemy'))

domyslny_slownik = defaultdict(list)
print(domyslny_slownik['a'])

domyslny_slownik = defaultdict(lambda: 50)
print(domyslny_slownik['a'])