Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r'pogon\\szczecin.pl,
SyntaxError: EOL while scanning string literal
>>> r'pogon\\szczecin.pl\
a=r'pogon\\szczecin.pl'
SyntaxError: invalid syntax
>>> r'pogon\\szczecin.pl'
'pogon\\\\szczecin.pl'
>>> a=50
>>> a*a
2500
>>> "twoje saldo wynosi " + str(a) + " PLN."
'twoje saldo wynosi 50 PLN.'
>>> 'twoje saldo wynosi {a} PLN.'
'twoje saldo wynosi {a} PLN.'
>>> f'twoje saldo wynosi {a} PLN'
'twoje saldo wynosi 50 PLN'
>>> f'twoje saldo wynosi {a:2f} PLN'
'twoje saldo wynosi 50.000000 PLN'
>>> f'twoje saldo wynosi {a:.2f} PLN'
'twoje saldo wynosi 50.00 PLN'
>>> 1+str(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    1+str(a)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 1+a
51
>>> 1+str(2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    1+str(2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 'saldo =' + str(2)
'saldo =2'
>>> a+int('2')+float('3.0')
55.0
>>> chr(33)
'!'
>>> ord('!')
33
>>> print(3*'dupa!')
dupa!dupa!dupa!
>>> print(5*'*')
*****
>>> print((3*'???')+(2*'!!!'))
?????????!!!!!!
>>> f('twoje saldo wynosi {a} PLN.').capitalize()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    f('twoje saldo wynosi {a} PLN.').capitalize()
NameError: name 'f' is not defined
>>> f'twoje saldo wynosi {a} PLN.'.capitalize()
'Twoje saldo wynosi 50 pln.'
>>> f'twoje saldo wynosi {a} PLN'.tittle()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    f'twoje saldo wynosi {a} PLN'.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> 'twoje saldo wynosi '.capitalize() + a
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    'twoje saldo wynosi '.capitalize() + a
TypeError: can only concatenate str (not "int") to str
>>> 'twoje saldo wynosi '.tittle() + int(a)+ ' PLN'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    'twoje saldo wynosi '.tittle() + int(a)+ ' PLN'
AttributeError: 'str' object has no attribute 'tittle'
>>> 'twoje saldo wynosi '.tittle() + str(a) + ' PLN'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    'twoje saldo wynosi '.tittle() + str(a) + ' PLN'
AttributeError: 'str' object has no attribute 'tittle'
>>> 'twoje saldo wynosi '.capitalize() + str(a) + ' PLN'
'Twoje saldo wynosi 50 PLN'
>>> 'abc'[1]
'b'
>>> len('abc')
3
>>> len('abc'*5)
15
>>> len('abc'+5)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    len('abc'+5)
TypeError: can only concatenate str (not "int") to str
>>> "123"[0]
'1'
>>> odp='123'
>>> odp
'123'
>>> odp='t'+odp[0:]
>>> odp
't123'
>>> odp='0'+odp[1:]
>>> odp
'0123'
>>> '4'in odp
False
>>> '0' in odp
True
>>> '012' in odp
True
>>> 'witaj!'.center(40,'*')
'*****************witaj!*****************'
>>> 'witaj!'.center(40,'<').capitalize()
'<<<<<<<<<<<<<<<<<witaj!<<<<<<<<<<<<<<<<<'
>>> 'witaj!'.capitalize().rjust(40,'a')
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaWitaj!'
>>> 'witaj'.rjust(40,'a').capitalize()
'Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaawitaj'
>>> 'tekst'[0:]
'tekst'
>>> 'tekst'[1:]
'ekst'
>>> 'tekst'[0:1]
't'
>>> 'tekst'[0:2]
'te'
>>> 'tekst'[1:2]
'e'
>>> 'st' + 'tekst'[0:2]
'stte'
>>> 'tekst'[0:2] + 'st'
'test'
>>> 'tekst'[2:3]
'k'
>>> 'tekst'[3:]
'st'
>>> 'tekst'[-1:-2]
''
>>> 'tekst'[-1:]
't'
>>> 'tekst'{-0:-1]
SyntaxError: invalid syntax
>>> 'tekst'[-0:-1]
'teks'
>>> 'tekst'[:-3]
'te'
>>> 'tekst'[0:4:2]
'tk'
>>> 'tekst'[::2]
'tkt'
>>> 'tekst'[-0:-4:2]
't'
>>> 'tekst'[::-2]
'tkt'
>>> z='ala ma kota'
z


