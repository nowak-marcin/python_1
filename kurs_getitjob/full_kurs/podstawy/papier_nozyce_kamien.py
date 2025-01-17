# gra do 3 zwycięstw jednego z graczy

gracz1_wynik = 0
gracz2_wynik = 0
opcje = ['papier', 'kamien', 'nozyczki']

while gracz1_wynik != 3 and gracz2_wynik != 3:

    sprawdzaj_wybor = True
    while sprawdzaj_wybor:
        wybor_gracza1 = input('Gracz1 wybrał: ')
        if wybor_gracza1 in opcje:
            sprawdzaj_wybor = False

    sprawdzaj_wybor = True
    while sprawdzaj_wybor:
        wybor_gracza2 = input('Gracz2 wybrał: ')
        if wybor_gracza2 in opcje:
            sprawdzaj_wybor = False

    if wybor_gracza1 == 'papier' and wybor_gracza2 == 'kamien'\
    or wybor_gracza1 == 'kamien' and wybor_gracza2 == 'nozyczki'\
    or wybor_gracza1 == 'nozyczki' and wybor_gracza2 == 'papier':
        print('Gracz1 wygral!')
        gracz1_wynik += 1
    elif wybor_gracza1 == wybor_gracza2:
        print('remis!')
    else:
        print('Gracz2 wygral!')
        gracz2_wynik += 1
print('koniec gry')

if gracz1_wynik > gracz2_wynik:
    print('cala gre wygral Gracz1')
else:
    print('cala gre wygral Gracz2')