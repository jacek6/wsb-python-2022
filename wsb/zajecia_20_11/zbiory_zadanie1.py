NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# Sprawdźmy:
# ile jest osób, które chorowały w ostatnim roku na Krzykach.
print('ile jest osób, które chorowały w ostatnim roku na Krzykach: ', len(krzyki.intersection(chorzy_rok)))
# ile jest osób z Krzyków chorowało w ostatnim roku.
print('ile jest osób z Krzyków chorowało w ostatnim roku: ', len(krzyki.intersection(chorzy_rok)))
# ile osób chorowało w ostatnim miesiącu w centrum.
print('ile osób chorowało w ostatnim miesiącu w centrum: ', len(centrum.intersection(chorzy_miesiac)))
# ile osób mieszka w sumie w centrum i na krzykach.
print('ile osób mieszka w sumie w centrum i na krzykach: ', len(centrum.union(krzyki)))

print('ile jest osób z Krzyków chorowało w ostatnim miesiacu: ', len(krzyki.intersection(chorzy_miesiac)))

