logi = (
    ('2020-12-10', 'ERROR'),
    ('2020-12-10', 'INFO'),
    ('2020-12-10', 'WARNING'),
    ('2020-12-11', 'ERROR'),
    ('2020-12-11', 'ERROR'),
    ('2020-12-11', 'WARNING'),
    ('2020-12-11', 'WARNING'),
    ('2020-12-11', 'INFO'),
    ('2020-12-12', 'ERROR'),
    ('2020-12-12', 'ERROR'),
    ('2020-12-12', 'ERROR'),
    ('2020-12-12', 'INFO'),
    ('2020-12-13', 'INFO'),
    ('2020-12-13', 'INFO'),
    ('2020-12-13', 'WARNING'),
    ('2020-12-13', 'ERROR'),
    ('2020-12-13', 'WARNING'),
    ('2020-12-14', 'ERROR'),
)

#czyszczenie danych

czyste_dane = []

for log in logi:
    if log not in czyste_dane:
        czyste_dane.append(log)

print(len(logi))
print(len(czyste_dane))

#odrzuc powtarzajace sie dane

def czy_zawiera(czyste_dane, logi_do_spr):
    for log in logi_do_spr:
        if log not in czyste_dane:
            return False
    return True

logi_do_spr = (
    ('2020-12-10', 'ERROR'),
    ('2020-12-10', 'INFO'),
)

sprawdzenie1 = czy_zawiera(czyste_dane, logi_do_spr)
print(sprawdzenie1)


# set (zbiór) - mozna edytowac, ma tylko unikalne elementy

nasz_zbior = set()
nasz_zbior.add(100)
nasz_zbior.add(50)
nasz_zbior.add(0)

print(nasz_zbior)
print(nasz_zbior.pop())
print(nasz_zbior.pop())

nasz_zbior2 = {20, 10, 50}

print(nasz_zbior2.issuperset([20, 10]))

# to samo zadanie z setem
# czyszczenie danych

czyste_dane = set(logi)

print(len(logi))
print(len(czyste_dane))

# odrzuc powtarzajace sie dane

def czy_zawiera(czyste_dane, logi_do_spr):
    return czyste_dane.issuperset(logi_do_spr)

print(czy_zawiera(czyste_dane, logi_do_spr))
