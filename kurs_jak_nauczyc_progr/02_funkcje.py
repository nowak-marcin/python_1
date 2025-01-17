def hello(name, age=55):
    print('Czesc ' + name + "!")
    print('Masz ' + str(age) + ' lat.')


hello('Marcin', 40)
hello('Michał')
hello('Daniel', age=60)


def strip_and_uppercase(text):
    return str(text).strip().upper()

text = ' jestem DO zmiany'
text = strip_and_uppercase(text)
print(text)