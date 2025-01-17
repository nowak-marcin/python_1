# generatory
# yield - generowanie kolejnych iteracji działania funkcji, bez jej przerywania
# return - zwraca wynik pojedynczy, bez kolejnej iteracji

def generuj():
    i = 0
    while i < 5:
        yield i
        i += 1

print(generuj())
print(list(generuj()))

# generator można wykorzystać w pętli iteracyjnej for

for i in generuj():
    print(i)

# zwróc tylko parzyste

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

print(list(parzyste(10)))

for i in parzyste(10):
    print(i)

# zwróc liczby z podanego zakresu od 1 do x
# yield - zwróci tyle iteracji wyników ile zadeklarowano

def simpleGen(x):
    i = 0
    for i in range(1, x + 1):
        yield i
    i += 1

print(list(simpleGen(10)))

# return - zwróci tylko pierwszą iterację

def simpleGen(x):
    for i in range(1, x + 1):
        return i

print((simpleGen(10)))