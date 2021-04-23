t1 = int(input('digite o primero termo:'))
r = int(input('digite a razão:'))
decimo = t1 + (10 -1) * r

for c in range(t1 , decimo + r, r):
    print(c)
