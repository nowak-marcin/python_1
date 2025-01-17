lista = [1, 4, "c", "d", "e"]

# odwołanie się do elementu:
print(lista[4])
# zmiana wartości elementu:
lista[2] = 3
print(lista)

# odwołanie się do elementu stringa (jak do listy):
tekst = "Pogoń Szczecin"
print(tekst[0])

# dodanie elementu do listy:
print(lista + [10, "P"])
lista += [20, "MKS"]
print(lista)

# mnożenie (powielenie) listy:
print(lista * 2)

# długość listy:
print("ilość elementów: ", len(lista))

# metody do odwoływania się do obiektu listy:

# append - dodaje element na końcu listy:
lista.append("ZS")
lista.append([2, "AB"])
print(lista)
print(lista[8][0])

# insert - wstaw element:
lista.insert(3, 3)
print(lista)

# count - ilość wystąpień:
print('Ilość wystąpień dla 3:', lista.count(3))

# index - zwróca indeks dla elementu:
print('Indeks dla MKS:', lista.index('MKS'))

# remove - usuń element
lista.remove(20)
print(lista)

lista2 = [1, 20, 35, -5, 0]

# minimalna i maksymalna wartość z listy:
print('Minimum:', min(lista2), "Maksimum:", max(lista2))

# sort - sortuj listę:
lista2.sort()
print(lista2)

# revers - odwróc listę:
lista2.reverse()
print(lista2)

# clear - wyczyszczenie listy:
lista2.clear()
print(lista2)






