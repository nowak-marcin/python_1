def napisz():
    print('adam')
    print('jest')
    print('fajny')


napisz()
napisz()


# return - zwraca zdefiniowaną wartość i pozwala przekazać tę wartość do zmiennej,
# return - przerywa działanie funkcji w lini, w której się znajduje


def zrob_kanapke(pieczywo, smarowidlo):
    print('robie kanapkę z chlebem', pieczywo, 'posmarowanym', smarowidlo)
    print(f'robie kanapke z chlebem {pieczywo} posmarowanym {smarowidlo}')
    return


co_jadles1 = zrob_kanapke('pszennym', 'maslem')
co_jadles2 = zrob_kanapke('zytnim', 'smalcem')
