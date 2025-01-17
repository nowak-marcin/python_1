# lambda - fukcja anonimowa, można wywołać tylko w miejscu deklaracji
def mojaFunkcja(f, liczba):
    return f(liczba)

print(mojaFunkcja(lambda x: x * x, 3))

def kwadrat(x):
    return x * x

print(kwadrat(5))

# lub

wynik = (lambda x: x * x)(5)
print(wynik)

# lub

wynik2 = lambda x: x * x
print(wynik2(5))

# lambda z więcej niż jednym argumentem

wynik3 = lambda x, y: x * y
print(wynik3(2,3))

# lub

print((lambda x, y: x * y)(2,3))