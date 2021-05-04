cont = 0
soma = 0
n = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'{cont}')
print(f'{soma}')


