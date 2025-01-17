# *args - domyślny argument funcji przyjmujący kolejne wartości
# niezdefiniowane w funkcji - w posatci krotki ()
# *kwargs - domyślny argument funcji przyjmujący kolejne wartości
# niezdefiniowane w funkcji - w posatci słownika {}

def funkcja(arg1, arg2='world', *args, **kwargs):
    print(arg1, arg2, args, kwargs, len(args), len(kwargs.values()))
    # lub jako kolejne wartości (bez słownika i krotki)
    print(arg1, arg2, *args, *kwargs.values())
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x)


funkcja('hello')
funkcja('czesc', 'swiecie')

funkcja('czesc', 'swiecie', '!!!', ':-)', autor='marcin', rok=2024, miesiac='II')



