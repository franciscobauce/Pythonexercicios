n = 0
cont = 0
soma = 0
n = int(input('Digite um número:'))
while not n == 999:
    cont += 1
    soma += n
    n = int(input('Digite um número:'))
print(cont)
print(soma)
