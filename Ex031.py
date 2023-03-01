km = int(input("Quantos quilometros tem a viagem? "))
if km <= 200 and km >= 1:
    valor = km * 0.5
    print("O valor da viagem sera de: {}" .format(valor))
elif km <= 0:
    print("O valor esta incorreto! Tente novamente. ")
else:
    valor = km * 0.45
    print("O valor da viagem sera de: {}" .format(valor))