contM = 0
contidade = 0
contfidade = 0
perg = ' '
while True:
    while True:
        sexo = str(input('Digite o sexo [M/F]:')).strip().upper()[0]
        if sexo == 'M':
            contM += 1
        if sexo in 'MF':
            break
    idade = int(input('Digite a idade:'))
    while perg not in 'SN':
        perg = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if perg in 'N':
        break
    if idade < 18:
        contidade += 1
    if idade < 20 and sexo == 'F':
        contfidade +=1


print(contM)
print(contidade)
print(contfidade)
print('Até mais')