import random
n1 = random.randint(0, 999)
n2 = random.randint(0, 999)
n3 = random.randint(0, 999)
n4 = random.randint(0, 99)

print('O numero do CPF aleatorio e: {:003d}.{:003d}.{:003d}-{:02d}'.format(n1, n2, n3, n4))