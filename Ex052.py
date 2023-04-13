t = 0
n = int(input("Diga um numero: "))
for i in range(1, n + 1):
     if n % i == 0:
        t += 1
if t == 2:
    print("O numero eh primo")
else:
    print("O numero não eh primo")
