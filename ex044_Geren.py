valor = float(input('Digite o valor das compras: R$ '))
print('[1] - à vista dinheiro ou cheque')
print('[2] - à vista cartão')
print('[3] - 2x no cartão')
print('[4] - 3x ou mais cartão')
opcao = int(input('Escolha a opção desejada: '))

i = 2 / 100
m2 = 2
#vf = valor * (1+i)**m#
if opcao == 1:
    print(f'O valor com desconto de 5% fica R$ {valor - valor * 5 //100:.2f}')

if opcao == 2:
    print(f'O valor total fica: R${valor:.2f} ')

if opcao == 3:
    vj = (valor * (1+i) ** 2)
    print(f'Parcelado em {2:} vezes, o valor da parcela fica R$ {vj // 2}')
    print(f'O valor total fica: R$ {vj:.2f}')

if opcao == 4:
    m3 = int(input('digite o numero de parcelas: '))
    vj = (valor * (1+i) ** m3)
    print(f'Parcelado em {m3} vezes, o valor da parcela fica  R${vj // m3}')
    print(f'O valor total fica: R$ {vj:.2f}')




