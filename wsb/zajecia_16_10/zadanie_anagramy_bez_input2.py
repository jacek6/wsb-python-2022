slowo = 'kajxk'

print('dlugosc podanego slowa to ', len(slowo))

for i in range(len(slowo)):
    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        break

# if i > 0:
if i == len(slowo) - 1:
    print('Podane slowo ', slowo, 'jest anagramem')

