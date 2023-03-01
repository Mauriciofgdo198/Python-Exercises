cidade = str(input('Qual o nome da sua cidade? '))
cidadem = cidade.upper()
contemsanto = cidadem[:6]
print('Se aparecer 0, o nome de sua cidade inicia com Santo, caso apareça -1 o o nome de sua cidade não inicia com Santo.')
print('\n')
print(contemsanto.find('SANTO '))