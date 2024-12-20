from curses.ascii import isalpha

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('So tem espaço?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', isalpha())
print('È alfanumerico?', a.isalnum())
print('Ésta em maiusculas?', a.isupper())
print('Esta em minuscula?', a.islower())
print('esta capitalizada?', a.istitle())
