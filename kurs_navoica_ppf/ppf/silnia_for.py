print("Obliczamy silnię")
n = int(input('Podaj n: '))
silnia = 1
for i in range(0, n):
    silnia = silnia * (i+1)
print(n, 'silnia jest równe', silnia)
