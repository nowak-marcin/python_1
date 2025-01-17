a = int(input('podaj liczbę całkowitą dodatnią: '))

if a % 2 == 0 and a > 0:
    print('liczba parzysta')
elif a < 0:
    print('podaj liczbę dodatnią!')
elif a == 0:
    print('Podaj liczbę większą od zera!')
else:
    print('liczba nieparzysta')
print('koniec1')
