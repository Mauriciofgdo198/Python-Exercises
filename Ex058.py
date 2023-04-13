import random
n = int(input("Tente acertar o numero escolhido entre 0 e 10: "))
c = random.randint(1, 10)
while n != c:
    n = int(input("Você errou, tente novamente! "))
print("Você acertou!!! O numero escolhido era {}.".format(c))