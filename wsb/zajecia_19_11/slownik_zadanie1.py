hasla_uzytkownikow = {'jacek': 'abc',
                      'ania': '123'}

def zmien_haslo(uzytkownik, aktualne_haslo, nowe_haslo):
    if uzytkownik not in hasla_uzytkownikow:
        print('Nie znany użytkownik ', uzytkownik)
        return
    if hasla_uzytkownikow[uzytkownik] != aktualne_haslo:
        print('Hasło nie pasuje')
        return
    hasla_uzytkownikow[uzytkownik] = nowe_haslo

def spr_haslo(uzytkownik, haslo) -> bool:
    if uzytkownik not in hasla_uzytkownikow:
        return False
    return hasla_uzytkownikow[uzytkownik] == haslo

while True:
    print('1. zmien haslo')
    print('2. spr haslo')
    print('3. pokaż hasła')
    print('4. wyjście')

    odp = input('co chcesz zrobić (1/2)?: ')
    if odp == '1':
        zmien_haslo(input('Podaj użytkownika: '), input('Podaj aktualne hasło: '), input('Podaj nowe hasło: '))
    elif odp == '2':
        print(spr_haslo(input('Podaj użytkownika: '), input('Podaj aktualne hasło: ')))
    elif odp == '3':
        print(hasla_uzytkownikow)
    elif odp == '4':
        break
