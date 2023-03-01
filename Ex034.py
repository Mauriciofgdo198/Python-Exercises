salario = int(input("Qual seu salario? "))

if salario <= 1250.00:
    novo = salario * 1.15
    print("Seu novo salario sera de: {}" .format(novo))
else:
    novo = salario * 1.1
    print("Seu novo salario sera de: {}" .format(novo))