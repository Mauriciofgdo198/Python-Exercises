import random
cont = n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = n11 = 0
while cont <= 10:
    n = random.randint(0, 9)
    if cont == 0:
        n1 = n
    elif cont == 1:
        n2 = n
    elif cont == 2:
        n3 = n
    elif cont == 3:
        n4 = n
    elif cont == 4:
        n5 = n
    elif cont == 5:
        n6 = n
    elif cont == 6:
        n7 = n
    elif cont == 7:
        n8 = n
    elif cont == 8:
        n9 = n
    elif cont == 9:
        n10 = n
    elif cont == 10:
        n11 = n
    cont += 1
    if cont == 10:
        print("O cpf aleatorio gerado foi: {}{}{}.{}{}{}.{}{}{}-{}{}".format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11))