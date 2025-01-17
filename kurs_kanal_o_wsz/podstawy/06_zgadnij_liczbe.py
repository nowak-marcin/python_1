from random import randint

los = randint(1,10)
odp = -1
i = 0
print('zagadnij liczbe z przedzialu 1-10')

while odp != los:
    i += 1
    odp = int(input('podaj liczbe: '))
    if odp > los:
        print('niestety wylosowana liczba jest mniejsza od twojej')
    elif odp < los:
        print('niestety wylosowana liczba jest wieksza od twojej')
print('brawo! odgadłes za', i, 'razem.')