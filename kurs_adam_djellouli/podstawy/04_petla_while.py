i = 0
while i < 10:
    print(i)
    i += 2
print('koniec1')

# instrukcja break (wyjście i zatrzymanie pętli)

while True:
    haslo = str(input('podaj hasło: '))
    if haslo == '1234':
        print('jesteś w systemie')
        break
    else:
        print('hasło jest błędne')
print('koniec2')

# instrukcja continue (powrót do kolejnego obiegu pętli)
# wypisz liczby od 1 do 10 bez podzielnych przez 3
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
print('koniec3')

