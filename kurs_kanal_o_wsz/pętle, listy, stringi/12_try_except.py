# wyjątek - dzielenie liczby przez zero, wartość string

x = 12
y = 'r'

try:
    print (x/y)
    print('wynik dzielenia prawidłowy')
except (ZeroDivisionError, TypeError):
    print('podałeś 0 lub daną typu tekstowego')
except:
    print('inny błąd')
finally:
    print('koniec1 - wykonam się zawsze')

