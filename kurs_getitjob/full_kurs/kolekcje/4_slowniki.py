# slownik (dict) - dopasowanie klucz-wartosc, kolejnosc zachowana, klucz niezmienny

slownik1 = {'auto': 'car', 'rower': 'bicycle'}

print(slownik1['auto'])

for x in slownik1.keys():
    print(x)

for x in slownik1.values():
    print(x)

for x in slownik1.items():
    print(x)

slownik1['narty'] = 'skies'
print(slownik1['narty'])

print(slownik1.get('miska', 'nie ma takiej wartości'))


# szyfrator

tekst = 'adam'

wynik = []

klucz_szyfrujacy = {'a': 'z', 'd': 'w', 'm': 'e'}

for x in tekst:
    wynik.append(klucz_szyfrujacy[x])

print(wynik)
print(''.join(wynik))