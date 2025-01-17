# powtórzenie pętli for i zakres

for x in range(2,10,2):
    print(f'{x:5}{x*2:5}{x*3:5}{x/2:+5}')

# krotka - (pozycja elementu w sekwencji, wartość elementu)

for n, d in enumerate (['50', '100', '200']):
    print('Liczba nr', n+1, 'to', d)

# modyfikacje elemenentów

x = [1,2,3]
for n,w in enumerate(x):
    x[n] = w + 3
print(x)
