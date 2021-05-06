contM = contidade = contfidade = 0
while True:
    perg = ' '
    sexo = ' '
    idade = int(input('Digite a idade:'))
    while not sexo in 'MF':
        sexo = str(input('Digite o sexo [M/F]:')).strip().upper()[0]
    while not perg in "SN":
        perg = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if idade < 20 and sexo == 'F':
        contfidade +=1
    if sexo == 'M':
        contM += 1
    if perg == 'N':
        break

print(f'quantos homens foram cadastrados? {contM}')
print(f'quantas pessoas tem mais de 18 anos? {contidade}')
print(f'quantas mulheres tem menos de 20 anos? {contfidade}')
print('até mais')
