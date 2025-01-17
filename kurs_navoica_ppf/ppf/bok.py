import math

# wprowadzenie pola
pole = float(input('Podaj pole kwadratu '))

# obliczenie boku i podanie wyniku
if pole > 1 or 0 < pole < 1:
  bok = math.sqrt(pole)
  print('Bok kwadratu = ', bok)

# przypadki negatywne
elif pole == 0:
  print('pole równa się 0 więc bok też jest równy 0')
elif pole == 1:
  print('pole równa się 1 więc bok też jest równy 1')
else:
  print('pole kwadratu nie może być liczbą ujemną!')
print('koniec')



