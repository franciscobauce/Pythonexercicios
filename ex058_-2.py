from random import randint
from time import sleep
count = 0
numero = (randint(0, 10))
print(numero)
acertou = False
palpites = 0

while not acertou:
    escolha = int(input('escolha um número:'))
    palpites += 1
    if escolha == numero:
        acertou = True
    else:
        if escolha > numero:
            print('Você para mais')
        else:
                print('Voce errou para menos')

print('Acertou')
print(palpites)

