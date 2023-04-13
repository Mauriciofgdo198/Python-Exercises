cont = i = n = maior = menor = 0
resp = "S"
while resp in "S":
    resp = str(input("Voce quer adicionar outro numero? (S/N) ")).strip().upper()[0]
    if resp == "S":
        n = int(input("Digite o numero: "))
        i = i + n
        cont += 1
        media = i/cont
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            else:
                menor = n
        print("A media é: {}".format(media))
        print("O maior valor é {}, e o menor valor é {}".format(maior, menor))
    else:
        print("Acabou!")
