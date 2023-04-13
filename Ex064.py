c = 999
n = 0
i = 0
cont = 0
while n != 999:
    n = int(input("Digite o numero: "))
    if n != 999:
        i = i + n
        cont += 1
print("Foram digitados {} numeros, e a soma deles deu: {}".format(cont, i))
