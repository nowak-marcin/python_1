from time import sleep

print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(5)
print('buuuuum')

for pojemnik in [3, 2, 1]:
    print(pojemnik)
    if pojemnik <= 2:
        sleep(1)
    sleep(1)
print('buuuuum')