lista = [9,8,1,2]

print(lista[0])
lista[0] = 'tunczyk'
print(lista[0])
print(len(lista))
lista.append(100)
lista.insert(2,200)
print(lista)
del lista[3]
lista.remove(100)
print(lista)
print('koniec1')

# pętla for dla listy

liczby = [2,6,3,10]

for x in liczby:
    print(x)
    print(x*x)
print('koniec2')

# instrukcje warunkowe dla listy

a = int(input('sprawdż czy liczba jest na liscie: '))

if a in liczby:
    print(a,'jest na liście')
else:
    print(a,'nie ma na liście')
print('koniec3')
