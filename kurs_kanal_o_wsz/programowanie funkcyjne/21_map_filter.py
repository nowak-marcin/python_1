liczby = [2, 10, 12, 15, 20, 25, 30, 35]

# fukcja map - działa iteracyjnie na każdym elemencie kolekcji, w sposób zdefiniowany w funkcji
# list - konwertowanie wyniku mapy na listę

def funkcja(x):
    return x * 2

wynik = map(funkcja, liczby)
print(wynik)
print(list(wynik))

# to samo, ale z funkcją lambda

wynik2 = map(lambda x: x * 2, liczby)
print(list(wynik2))

# funkcja filter - nie modyfikuje kolekcji, zwraca tylko wyniki zgodne z warunkiem w funcji

wynik3 = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))
