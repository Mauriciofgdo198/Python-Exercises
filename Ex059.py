n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
o = int(input("Escolha uma das operações: \n(1) Somar \n(2) Multiplicar \n(3) Maior \n(4) Novos numeros \n(5) Sair do programa \nEscolha: "))
while o != "5":
    if o == 1:
        soma = n1 + n2
        print("A soma dos numeros {} e {} totalizam: {}".format(n1, n2, soma))
    elif o == 2:
        mult = n1 * n2
        print("A multiplicação dos numeros {} e {} totalizam: {}".format(n1, n2, mult))
    elif o == 3:
        if n1 > n2:
            print("O maior numero é: {}".format(n1))
        elif n1 == n2:
            print("Os numeros tem o mesmo valor.")
        else:
            print("O maior numero é: {}".format(n2))
    elif o == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
print("Voce saiu do programa. ")