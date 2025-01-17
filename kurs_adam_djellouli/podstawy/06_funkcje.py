def james(ilosc):
    for i in range (0,ilosc):
        print('nazywam się james')

james(3)
print('koniec1')

def suma(a,b):
    print(a+b)

suma(3,5)
suma(4,4)
print('koniec2')

# funkcja wywołująca inne funkcje
# return - przekazanie wartości do innej funkcji
def dodaj(a,b):
    return(a+b)
def odejmij(a,b):
    return(a-b)
def iloczyn(a,b):
    return(a*b)
def kalkulator(wybor,a,b):
    if wybor == 1:
        print('suma liczb wynosi:',dodaj(a,b))
    if wybor == 2:
        print('różnica liczb wynosi:',odejmij(a,b))
    if wybor == 3:
        print('iloczyn liczb wynosi:', iloczyn(a,b))

kalkulator(2,5,3)
print('koniec3')

for i in range(1,4):
    kalkulator(i,10,5)
print('koniec4')




