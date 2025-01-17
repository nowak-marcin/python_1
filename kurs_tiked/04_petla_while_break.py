n = 0
while n < 5:
    print(n)
    n += 1
print('koniec1')

m = 0
while m < 5:
    m += 1
    print(m)
print('koniec2')

# wyświetl ciąg liczb parzystych od 4 do 16
liczba1 = 4
while liczba1 < 17:
    print(liczba1)
    liczba1 += 2
print('koniec3')

# break - przerywanie instrukcji while
# wypisz ciąg liczb od 0 do 4
liczba2 = 0
while True:
    if liczba2 == 5:
        break
    print(liczba2)
    liczba2 += 1
print('koniec4')

# obliczanie sumy liczb całkowitych do momentu wystąpienia 0
suma = 0
while True:
    a = int(input('podaj liczbę: '))
    suma += a
    print(suma)
    if a == 0:
        break
print('sumowanie dobiegło końca, podałeś 0')
print('koniec')



