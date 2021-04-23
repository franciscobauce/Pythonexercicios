from random import randint

lista = ['PEDRA ', 'PAPEL', 'TESOURA']
computador = randint(0,2)

print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

jogador = int(input('Escolha uma opção: '))
print(f'Jogador jogou {lista[jogador]}')
print(f'Computador jogou {lista[computador]}')

if jogador or computador == 0 and jogador or computador == 1:
    print ('papel vence')
elif jogador or computador == 1 and jogador or computador == 2:
    print('tesoura vence')
elif jogador or computador == 2 and jogador or computador -- 0:
    print('pedra vence')
else:
    print('empate')








