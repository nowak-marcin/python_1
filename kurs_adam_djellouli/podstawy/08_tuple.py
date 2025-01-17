# tuple (krotki) - elementy indeksowane, nie można ich zmieniać, duplikaty dozwolone

przyklad1 = (1,2,3,3,20,300)

print(len(przyklad1), type(przyklad1))
print(przyklad1[5], 'koniec1')

for x in przyklad1:
    print(x)
print('koniec2')

# konwersja tupla na listę

przyklad2 = (2,'piwo',100)

przyklad2 = list(przyklad2)
print(przyklad2, type(przyklad2))

# konwersja listy na tupla

przyklad3 = [0,5,'wino']

przyklad3 = tuple(przyklad3)
print(przyklad3, type(przyklad3))



