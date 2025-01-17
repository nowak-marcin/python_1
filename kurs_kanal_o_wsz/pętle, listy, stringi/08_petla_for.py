lista = ['subskrybuj', 'kanał', 'o', 'wszystkim']

# pętla while:

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# pętla for (przez):

for x in lista:
    print(x)

# funkcja range i list:

print(list(range(5)))

for y in range(5):
    print(y)

for y in range(1, 6):
    print(y)

for y in range(1, 6, 2):
    print(y)
    print('koniec')

# wypisz liczby parzyste mniejsze od 10

tabela = [1,2,10,8,6,2,2,1,9,20,10,15,13,10]

for x in tabela:
    if x % 2 == 0:
        continue
    print(x)


