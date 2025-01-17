# spełnienie nierówności boków trójkąta
# każdy bok jest mniejszy od sumy pozostałych

a = int(input('podaj bok trójkąta '))
b = int(input('podaj bok trójkąta '))
c = int(input('podaj bok trójkąta '))

if a < b + c and b < a + c and c < a + b:
    print('nierównosć trójkąta JEST spełniona')
else:
    print('nierównosć trójkąta NIE JEST spełniona')
print('koniec1')

# and i or dla warunków zagnieżdżonych

if a == 5 or b == 6 or c < 10:
    print('prawda')
else:
    print('nieprawda')
print('koniec2')