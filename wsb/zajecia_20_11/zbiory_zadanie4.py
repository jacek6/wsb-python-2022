NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436, 3098])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}

# Wypiszmy:
# kobiety z Krzyków, które były chore w ostatnim roku.
print('kobiety z Krzyków, które były chore w ostatnim roku ', {e for e in krzyki.intersection(chorzy_rok) if e % 2 == 0})
# wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku.
print('wypiszmy mężczyzn z Centrum, którzy NIE byli chorzy w ostatnim roku ',
      {e for e in centrum.difference(chorzy_rok) if e % 2 == 1})

print(f'{centrum = }')
print(f'{chorzy_rok = }')
print(f'{centrum.difference(chorzy_rok) = }')
print('to powienien byc zbior pusty ', centrum.difference(chorzy_rok).intersection(chorzy_rok))
print('to powienien byc podzbior osob z centrum ', centrum.difference(chorzy_rok).intersection(centrum))