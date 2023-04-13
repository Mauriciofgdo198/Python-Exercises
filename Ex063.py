n = int(input("Digite quantos termos quer da sequencia fibonacci: "))
cont = 0
t1 = 0
t2 = 1
while cont <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1