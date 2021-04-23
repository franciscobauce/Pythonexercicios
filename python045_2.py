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

print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO')
sleep(1)

if jogador == 1:
    print('jogador => PEDRA')
if jogador == 2:
    print('jogador => PAPEL')
if jogador == 3:
    print('jogador => TESOURA')

print('Maquina =>', maquina)

if jogador == PEDRA and maquina == 'PAPEL':
    print('PAPEL VENCEU')
elif jogador == PEDRA and maquina == 'TESOURA':
    print('TESOURA VENCEU')
elif jogador == PAPEL and maquina == 'PEDRA':
    print('PAPEL VENCEU')
elif jogador == PAPEL and maquina == 'TESOURA':
    print('TESOURA VENCEU')
elif jogador == TESOURA and maquina == 'PEDRA':
    print('PEDRA VENCEU')
elif jogador == TESOURA and maquina == 'PAPEL':
    print('TESOURA VENCEU')
else:
    print('Empate')


