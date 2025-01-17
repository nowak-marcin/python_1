dni_tyg = ['pon','wt','sr','czw','pia']

print(dni_tyg[4])

# wprowadz 5 liczb do listy:

n = 5
moja_lista = [0]*n
def wprowadzElementy():
    for i in range(n):
        moja_lista[i]=int(input('podaj liczbę '))

wprowadzElementy()
print(moja_lista, 'koniec1')

# append - dodanie elementów do listy

dni_tyg.append('sob')
print(dni_tyg)
print(len(dni_tyg))

# wprowadź do listy 4 wybrane imiona, wyzeruj listę przed wprowadzeniem

n=4
imiona = [0]*n

def dodajImiona():
    for i in range(n):
        imiona[i]= str(input('podaj imię: '))

dodajImiona()
print(imiona, 'koniec2')