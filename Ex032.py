ano = int(input("Digite um ano: "))
bissexto = ano % 4
if bissexto == 0:
    print("O ano eh bissexto")
else:
    print("O ano não eh bissexto")