lista = []
for c in range(0, 4):
    lista.append(int(input('Digite um número:')))
for e in lista:
    if lista[e] % 2 == 0:
        print(lista[e])
