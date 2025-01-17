# zbiór - wartości są unikalne

# utworzenie zbioru

liczby1 = {0, 1, 2, 4}
print(liczby1)

# przekonwertowanie listy na zbiór

slowa = set(['a', 'b', 'c'])
print(slowa)

# metody dla zbioru

liczby1.add(5)
liczby1.remove(0)
print(liczby1)
print(1 in liczby1)

# operacje na zbiorach (suma, iloczyn, różnica, różnica symetryczna)

liczby1 = {0, 1, 2, 4}
liczby2 = {3, 4, 5, 6}

print(liczby1 | liczby2)
print(liczby1 & liczby2)
print(liczby2 - liczby1)
print(liczby2 ^ liczby1)