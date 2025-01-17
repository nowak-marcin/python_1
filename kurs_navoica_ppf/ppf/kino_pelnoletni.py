pelnoletni = str(input('Czy jesteś pełnoletni? [TAK/NIE]'))
filmDlaDoroslych = str(input('Czy interesuję cię film dla dorosłych? [TAK/NIE]'))
cenaBiletu = 40

if pelnoletni == 'TAK':
    print('Cena biletu wynosi', cenaBiletu, 'PLN.')
else:
    if filmDlaDoroslych == 'TAK':
        print('To nie jest film dla dzieci.')           
    else:
        print('Cena biletu wynosi', cenaBiletu / 2, 'PLN')

      
                 



