numeros = (int(input('Digite um número:')), int(input('Digite um número:')),int(input('Digite um número:')),int(input('Digite um número:')))
cont = 0
contpar = 0
pares = 0
for n in numeros:
    print(n, end=' ')
    if n == 9:
        cont += 1
print(f'\nA tupla possui {cont} números nove')
if 3 in numeros:
    print(f'Três está na posicão {numeros.index(3)}')
else:
    print('A tupla nao possui o número três')
print('Os valores pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        contpar += 1
        print(n, end=' ')
print(f'\nA tupla possui {contpar} números pares')
