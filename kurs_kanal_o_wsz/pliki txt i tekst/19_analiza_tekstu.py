myPlik = open('19_mytest2.txt', 'r')
tekst = myPlik.read()
myPlik.close()

# ile razy dana litera występuje w tym tekście

def policz(mytxt, znak):
    licznik = 0
    for z in mytxt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, 'a') + policz(tekst, 'A'))
print(policz(tekst.lower(), 'a'))

# ile procentowo w tekście występuje dana litera od a do x

for z in 'abcdex':
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)
    print('{0} - {1} - {2}%'.format(z.upper(), ile, round(procent, 1)))