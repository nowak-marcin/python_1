ile = int(input('Ile liczb chcesz dodać? '))
suma = 0 
for i in range(1, ile+1):
    print('Podaj liczbę nr', i, 'z', ile)
    liczba = float(input())
    suma += liczba
print('suma =', suma)

    
    
