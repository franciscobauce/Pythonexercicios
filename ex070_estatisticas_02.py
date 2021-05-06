total = 0
mil = 0
maior = 0
menor = 0
minimo = ' '
cont = 0
while True:
    pergunta = ' '
    produto = str(input('Digite o produto:'))
    valor = int(input('Digite o valor:'))
    total += valor
    cont += 1
    if cont == 1 or valor < menor:
        menor = valor
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
print(f'{menor} Menor')
print(minimo)
