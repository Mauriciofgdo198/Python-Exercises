n = input('Digite algo: ')
print('Seu tipo primitivo e: ' ,type(n))
print('Isso é um numero? ' ,n.isnumeric())
print('Isso é uma palavra?' ,n.isalpha())
print('Isso são numeros e/ou palavras?' ,n.isalnum())
print('So tem espaços?',n.isspace())
print('Esta em maiusculas?' ,n.isupper())
print('Esta em minusculas?' ,n.islower())

