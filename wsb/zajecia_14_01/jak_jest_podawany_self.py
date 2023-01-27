"""
2 notacje funkcyjne, 2 sposoby wywołania funkcji klasy:

odp = str.lower(input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona): '))

odp = (input('Na której liście chcesz operować? ([N]iebieska, Czerwona):').lower())

"""


zmienna1 = 'tesk'
zmienna2 = ['tesk']


class strNaPorzeby_kursu:

    def lower(self):
        return 'abc'

tekst = 'NORMANY Tekst'
print('lower tekst = ', tekst.lower())
print('lower tekst = ', str.lower(tekst))

tekstWlasny = strNaPorzeby_kursu()
print('lower tekstWlasny = ', tekstWlasny.lower())
print('lower tekstWlasny = ', strNaPorzeby_kursu.lower(tekstWlasny))

print('jest taka funkcja jak lower ', strNaPorzeby_kursu.lower)