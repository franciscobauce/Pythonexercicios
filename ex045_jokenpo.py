import random
from time import sleep
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')

lista = ['PEDRA', 'PAPEL', 'TESOURA']

PEDRA = 1
PAPEL = 2
TESOURA = 3

maquina = (random.choice(lista))
jogador = int(input('Escolha uma opção: '))



if jogador == 1:
    print('jogador => PEDRA')
if jogador == 2:
    print('jogador => PAPEL')
if jogador == 3:
    print('jogador => TESOURA')

print('Maquina =>', maquina)

if jogador or maquina == PEDRA:
    if jogador or maquina == PAPEL:
        print('papel vence')
    elif jogador or maquina == TESOURA:
        print('pedra vence')
if jogador or maquina == PAPEL:
    if jogador or maquina == TESOURA:
        print('Tesoura vence')
else:
    print('empate')





