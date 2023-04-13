n = int(input("Digite o numero inicial: "))
r = int(input("Digite a razão: "))
cont = 0
termos = 1
while termos != 0:
    termos = int(input("Digite outro termo: "))
    while cont <= 10:
        print(n)
        n = n + r
        cont += 1
print("Acabou!")