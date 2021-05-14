numeros = (int(input('Digite um número:')), int(input('Digite um número:')),int(input('Digite um número:')),int(input('Digite um número:')))
cont = 0
contpar = 0
for n in numeros:
    print(n, end=' ')
    if n == 9:
        cont += 1
    if n >= 0:
        n = n % 2
        if n == 0:
            contpar += 1
print(f'\nTrês está na posicão {numeros.index(3)}')
print(f'A tupla possui {cont} números nove')
print(f'A tupla possui {contpar} números pares')

