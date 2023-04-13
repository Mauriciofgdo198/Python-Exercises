valor = int(input("Diga o valor do produto: "))
vista = valor * 0.9
vista_cartão = valor * 0.95
x = valor * 1.2

forma = str(input("Qual sera a forma de pagamento? (Dinheiro, Cartão ou Dividido)"))

if forma == "dinheiro":
    print(vista)
elif forma == "cartão":
    print(vista_cartão)
elif forma == "dividido":
    print(x)