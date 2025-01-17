# funkcja join

lista = ['a', 'b', 'c']
print(', '.join(lista))

# metody replace, startswith, endswith, upper, lower

print('pogon szczecin'.replace('pogon','mks pogon'))
print('to jest zadanie'.startswith('to'))
print("raz dwa trzy".endswith('dwa'))
print('raz dwa trzy'.upper())
print('raz dwa trzy'.lower())

# wyszukanie dowolnego znaku w stringu

print("dwa" in "raz dwa trzy")
print('--------')

# funkcje all i any

lista2 = [10, 20, 24, 36, 40]

if all([i % 2 == 0 for i in lista2]):
    print('wszystkie parzyste')
else:
    print("niewszytkie parzyste")

if any([i == 20 for i in lista2]):
    print('tak, 20 jest na liscie')
else:
    print('20 nie ma liście')

# funkcja enumerate - zwraca (indeks, wartość)

for i in enumerate(lista2):
    print(i)
    print(i[0] + 1, '-', i[1])