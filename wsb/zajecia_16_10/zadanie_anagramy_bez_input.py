# slowo = 'kajak'
slowo = 'wrggsdvksdmvklaeipqeio wevpksd vsd'

print('dlugosc podanego slowa to ', len(slowo))

for i in range(len(slowo)):
    print('na pozycji ', i, 'znajduje sie litera', slowo[i], ' po przeciwnej stronie jest litera ', slowo[len(slowo) - 1 - i])

    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        break
