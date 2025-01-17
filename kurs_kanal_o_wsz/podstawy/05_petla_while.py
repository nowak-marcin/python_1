# pętla while, break, continue

i = 0
while True:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break
print('koniec')

# wypisz liczby od 0 do 4

liczba = 0
while True:
    print ('Liczba z przedziału 0-4:', liczba)
    liczba += 1
    if liczba >= 5:
        break
print('Koniec')