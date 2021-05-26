lista1 = []
lista2 = []
lista3 = []
cont = 0
while True:
    lista1.append(int(input('Digite um número:')))
    if lista1[cont] % 2 == 0:
        lista2.append(lista1[cont])
        print('par')
    else:
        lista3.append(lista1[cont])
        print('impar')
    cont += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Você quer continuar?[S/N]')).strip().upper()
    if p == 'N':
        break
print(lista1)
print(lista2)
print(lista3)



