from random import randint
computador = randint(0, 5)
numero = int(input("Vamos jogar! Adivinhe o numero que eu escolhi de 0 a 5: "))
if numero == computador:
    print("Você acertou! Meus parabens! ")
elif numero >= 6 or numero < 0:
    print("Você escolheu um numero invalido. ")
else:
    print("Você errou, tente novamente! ")