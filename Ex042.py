l1 = int(input("Diga o valor da primeira reta: "))
l2 = int(input("Diga o valor da segunda reta: "))
l3 = int(input("Diga o valor da terceira reta: "))

if l1 > l2 and l1 > l3:
    if l2 + l3 >= l1:
        print("Esses valores de retas formam um triangulo. ")
    else:
        print("Esses valores de retas não formam um triangulo. ")
elif l2 > l1 and l2 > l3:
    if l1 + l3 >= l2:
        print("Esses valores de retas formam um triangulo. ")
    else:
        print("Esses valores de retas não formam um triangulo. ")
elif l3 > l1 and l3 > l2:
    if l1 + l2 >= l3:
        print("Esses valores de retas formam um triangulo. ")
    else:
        print("Esses valores de retas não formam um triangulo. ")