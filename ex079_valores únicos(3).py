valores = []
while True:
    v1 = int(input('Digite um valor:'))
    if v1 not in valores:
        valores.append(v1)
    else:
        print('Não foi possível adicionar esse numero')
    p = ' '
    while p not in 'SN':
        p = str(input('Você quer continuar[S/N]:')).strip().upper()[0]
    if p == 'N':
        break
print(f'Você digitou os números: {sorted(valores)}')
print('Até mais')

