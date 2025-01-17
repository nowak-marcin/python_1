# listy - zmienne, indeksowane od zera, dopuszcza powtórzenia

l1 = [1, 2, 3, 'adam']

print(l1[3])

l1.append('kot')
print(l1)
l1.remove('adam')
print(l1)
l1.extend([10, 20])
print(l1)


tranzakcje = []

WYBOR = None

while WYBOR != '0':
    print('0-koniec operacji\n1-wplac kase\n2-wyplac kase\n3-sprawdz saldo\n4-uznania\n')
    WYBOR = input('wybierz opcje: ')

    if WYBOR == '1':
        kwota = input('podaj kwote wyplaty: ')
        tranzakcje.append(int(kwota))
    elif WYBOR == '2':
        kwota = input('podaj kwote do wyplaty: ')
        tranzakcje.append(-int(kwota))
    elif WYBOR == '3':
        print(f'saldo = {sum(tranzakcje)}')
    elif WYBOR == '4':
        uznania = []
        for kwota in tranzakcje:
            if kwota > 0:
                uznania.append(kwota)
        print(sum(uznania))


    print(tranzakcje)