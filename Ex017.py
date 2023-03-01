import math
co = int(input('Qual o valor do cateto oposto? '))
ca = int(input('Qual o valor do cateto adjacente? '))
h = (ca**2)+(co**2)
h1 = math.sqrt(h)
print('O comprimento da hipotenusa sera de {}.'.format(h1))