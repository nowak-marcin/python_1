punkty = int(input('Liczba punktów: '))

if punkty == 100:
    print("Gratulacje, wynik maksymalny")
elif punkty > 75:
    print('Bardzo dobry wynik')
elif punkty >= 50:
    print('Całkiem nieźle')
else:
    print('Niestety masz mniej niż 50 pkt')
print('koniec1')

# sprawdz czy podana liczba jest parzysta

a = int(input('Podaj liczbę: '))

if a % 2 == 0:
    print('liczba parzysta')
else:
    print('liczba nieparzysta')
print('koniec2')

# porównaj dwie liczby podane przez użytkownika i wyświetl wyynik

a = int(input('podaj pierwszą liczbę: '))
b = int(input('podaj drugą liczbę: '))

if a > b:
    print('pierwsza liczb jest większa')
elif b > a:
    print('druga liczba jest większa')
else:
    print('liczby są równe')
print('koniec3')

# określ czy osoba jest pełnoletnia

rok_urodz = int(input('podaj rok urodzenia: '))
wiek = 2021 - rok_urodz

if wiek >= 18:
    print('pełnoletni')
else:
    print('niepełnoletnia')
print('koniec4')
