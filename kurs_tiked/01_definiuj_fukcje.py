def powitanie():
    for i in range(5):
        print('Witaj!')

powitanie()

# funkcja z argumentami
def pole_trojkata(a,h):
    wynik = 0.5*a*h
    print(wynik)

pole_trojkata(2,4)
pole_trojkata(3,6)

# return - instrukcja zwracająca wartość
def szescian(a):
    return 6*(a*a)

bok = int(input('Podaj bok sześcianu: '))
pole = szescian(bok)
print('Pole sześcianu wynosi:', pole)

# napisz funkcję, która wyświetli twój adres, powtórz 3 razy
def dane_adres():
    print("MNowak")
    print("Hoża 1, Szczecin")

for x in range(3):
    dane_adres()

# mnożenie dwóch liczb, ustaw domyślne wartości argumentów na 0
def iloczyn_liczb(a=0,b=0):
    print(a*b)

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
iloczyn_liczb(a,b)

# podniesienie do kwadratu dla dowolnej liczby
def kwadrat_liczb(liczba):
    wynik = liczba * liczba
    return wynik

a = int(input('Podaj liczbę: '))
print('Liczba', a, 'podniesiona do kwadratu daje:', kwadrat_liczb(a))