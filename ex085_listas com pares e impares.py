impar = []
par = []
lista = []
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.append(par)
lista.append(impar)
print(lista[0])
print(lista[1])


