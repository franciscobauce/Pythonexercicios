total = 0
mil = 0
maior = 0
menor = 0
minimo = ' '
while True:
    pergunta = ' '
    produto = str(input('Digite o produto:'))
    valor = int(input('Digite o valor:'))
    total += valor
    if valor == 0:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < maior:
        menor = valor
    if valor == menor:
        minimo = produto
    if valor > 1000:
        mil += 1
    while not pergunta in "SN":
        pergunta = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if pergunta in 'N':
        break
print(total)
print(mil)
print('FIM')
print(f'{maior} Maior')
print(f'{menor} Menor')
print(minimo)

