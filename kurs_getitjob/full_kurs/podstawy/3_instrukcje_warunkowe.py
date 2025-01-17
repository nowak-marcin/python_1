for pojemnik1 in [1, 2, 3, 4]:
    print(pojemnik1)


pojemnik2 = int(input('Podaj liczbe od 0 do 10: '))

if pojemnik2 == 4:
    print('działa dla 4')
elif pojemnik2 == 5:
    print('dziala dla 5')
else:
    print('w pojemniku jest cos innego')


pojemnik2 += 1
print(pojemnik2)


pojemnik2 = 0

while pojemnik2 < 4:
    print('marcin')
    pojemnik2 += 1