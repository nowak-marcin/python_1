for i in [0,1,2,3,4]:
    print(i)
print('koniec1')

# funkcja range (x,y,z)
for i in range(2,4):
    print(i)
print('koniec2')

# zmienna jako liczba powtórzeń
n = int(input('podaj ilość powtórzeń: '))
for i in range(n):
    print('witaj')
print('koniec3')

# wyświetl ciąg liczb: 5,10,15,20,25
a = 0
for i in range(5):
    a += 5
    print(a)
print('koniec4')

# sumowanie 5 liczb podanych przez użytkownika
suma = 0
for i in range(5):
    liczba1 = int(input('podaj liczbę: '))
    suma += liczba1
print('suma podanych liczb wynosi: ', suma)
print('koniec5')

# tabliczka mnożenia do 10 dla liczny podanej przez użytkownika
liczba2 = int(input('podaj liczbę: '))
for i in range(1,11):
    print(i, 'x', liczba2, '=', i * liczba2)



