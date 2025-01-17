def dzielenie(x,y):
    assert y>0, 'y jest niedodatnie'
    if y==0:
        raise ZeroDivisionError('Dzielenie przez 0')
    print(x/y)

dzielenie(2,-1)

