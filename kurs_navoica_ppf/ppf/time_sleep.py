import time

sekundy = int(input('Ile sekund chcesz czekać? '))
while sekundy !=0:
    print('Pozostało', sekundy, 'sek')
    sekundy -= 1
    time.sleep(1)
print('koniec')










