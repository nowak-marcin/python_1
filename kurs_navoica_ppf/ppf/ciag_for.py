n = int(input('Który wyraz ciągu Fionacciego chcesz zobaczyć? '))

if n==1:
    print(0)
elif n==2:
    print(1)
else:
    l1 = 0
    l2 = 1
    for i in range(0, n - 2):
        fibo = l1 + l2
        l1 = l2
        l2 = fibo
    print('element nr', n, 'jest równy', fibo)
