from random import randint
from time import sleep
numero = (randint(0,10))
print(numero)

escolha = int(input('escolha um número:'))
print('==' *21)
print(('==' * 7), 'PROCESSANDO',('==' * 7))
print('==' *21)
sleep(3)

if escolha == numero:
    print(f'"acertou" o número sorteado foi {numero}')
else:
    print(f'"errou" o numero sorteado foi {numero}')












