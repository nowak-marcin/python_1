# generator - to funkcja do tworzenia iteratora

def generator():
    yield 1
    yield 4
    yield 5

for i in generator():
    print(i)

# lub

x = generator()
print(next(x))
print(next(x))
print(next(x))

print('------')

def generator2(a,b):
    while a <= b:
        yield a
        a += 1

for i in generator2(2,10):
    print(i)

print('------')

def odwroc(dane):
    for i in range(len(dane) - 1, -1, -1):
        yield dane[i]

for i in odwroc('kukulka'):
    print(i, end='')