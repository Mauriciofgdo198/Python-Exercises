valor = int(input("Qual o valor da casa? "))
salario = int(input("Qual o salario do comprador? "))
ano = int(input("Em quantos anos o comprador vai pagar? "))
mensal = valor/(ano*12)
salario30 = salario * 0.3

if mensal > salario30:
    print("O valor excedeu 30% do salario do comprador, o emprestimo foi negado!")
else:
    print("O emprestimo foi aprovado!")