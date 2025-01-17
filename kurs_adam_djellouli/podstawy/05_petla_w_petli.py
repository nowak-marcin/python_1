# utwórz kwadrat 5x10 złożony ze znaków "*"

for i in range(0,5):
    for j in range(0,10):
        print('*', end='')
    print('\r')
print('koniec1')

# utórz kwadrat w postaci:
# 1111
# 2222
# 3333

for i in range(0,3):
    for j in range(0,4):
        print(i+1, end='')
    print('\r')
print('koniec2')

# utwórz trojkąt o podstawie 4 '*' i wysokości 4 '*'

for i in range(0,4):
    for j in range (0, i+1):
        print('*', end='')
    print('\r')
print('koniec3')

# utwórz trójkąt prostokątny o a=5 i h=5:

n = 5
for i in range(0,5):
    for j in range(0, n-(i+1)):
        print(end='')
    for j in range (0, i+1):
        print('*', end='')
    print('\r')
print('koniec4')






