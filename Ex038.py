n1 = int(input("Diga um numero inteiro: "))
n2 = int(input("Diga um numero inteiro: "))

if n1 > n2:
    print("O valor {} é maior que o {}.".format(n1, n2))
elif n2 > n1:
    print("O valor {} é maior que o {}.".format(n2, n1))
else:
    print("Não existe valor maior, os dois são iguais!")