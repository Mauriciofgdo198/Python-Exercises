n1 = float(input("Diga o valor da nota da primeira prova: "))
n2 = float(input("Diga o valor da nota da segunda prova: "))
media = (n1 + n2)/2

if media < 5.0:
    print("REPROVADO")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")