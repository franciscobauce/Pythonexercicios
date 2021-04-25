maior = 0
soma = 0
cont = 0
velho = ''
for c in range(1, 2 + 1 ):
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade:'))
    print('DIGITE SEU SEXO:')
    print('[1] SEXO MASCULINO')
    print('[2] SEXO FEMININO')
    sexo = str(input('DIGITE A OPÇÃO:'))
    print()
    soma += idade
    if idade < 20 and sexo == '2':
        cont += 1
    if c == 1 and sexo == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade
            velho = nome

print(f'Neste grupo a média de idade é', soma / c, 'anos.')
print(f'Neste grupo existem {cont} mulher(es) abaixo de 20 anos.')
print(f'Neste grupo de pessoas o homem mais velho tem`{maior} anos de idade e se chama {velho}.')

