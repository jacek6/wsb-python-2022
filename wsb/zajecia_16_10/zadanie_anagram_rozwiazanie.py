slowo = input('Podaj słowo do sprawdzenia czy jest anagramem: ')

print('dlugosc podanego slowa to ', len(slowo))

czy_to_anagram = True
for i in range(len(slowo)):
    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        czy_to_anagram = False
        break
if czy_to_anagram:
    print('Podane slowo ', slowo, 'jest anagramem')

