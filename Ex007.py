nome = input('Qual o seu nome? ')
n1 = int(input('A nota da primeira prova do {} é: '.format(nome)))
n2 = int(input('A nota da segunda prova do {} é: '.format(nome)))
m = (n1+n2)/2
print('A media do {} é de: {}'.format(nome ,m))