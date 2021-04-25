maior = 0
menor = 0

for c in range(1, 3 + 1 ):
    idade = int(input('Digite sua idade:'))
    print('DIGITE SEU SEXO:')
    print('[1] SEXO MASCULINO')
    print('[2] SEXO FEMININO')
    sexo = str(input('DIGITE A OPÇÃO:'))
    if sexo == 1 and c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade

print(menor)
print(maior)
