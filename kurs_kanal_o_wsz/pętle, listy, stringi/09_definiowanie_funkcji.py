def funkcja_test():
    print('Funkcja...')

funkcja_test()
funkcja_test()

# return - przechowywanie wyniku do zastosowanie poza funcją
def dodaj(x, y = 1, z = 0):
    return (x + y + z)

print(dodaj(2, 3))
print(dodaj(2))

wynik = dodaj(2, 3, 5)
print(wynik)

# przekazanie funkcji do zmiennej:
def moja_funkcja(x):
    return x * x

moja_zmienna = moja_funkcja
print(moja_zmienna(5))

# przekazanie funkcji do innej funkcji
def moja_funkcja_2(f1, x):
    return f1(x) * x
print(moja_funkcja_2(moja_funkcja, 5))

# rekurencja - wywołanie funcji w ciele funkcji:

def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)
print(silnia(5))
print(silnia(1))



