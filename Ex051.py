t = int(input("Diga o primeiro termo da progressão aritmetica: "))
r = int(input("Diga a razão da progressão artimetica: "))
d = t + (10 -1) * r
for i in range(t, d + r, r):
    print(i)