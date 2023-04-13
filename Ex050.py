soma = 0
for i in range(1, 7):
    n = int(input("Diga um numero: "))
    if n % 2 == 0:
        soma += n

print(soma)