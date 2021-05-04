from random import randint
from time import sleep
count = 1 + 0
numero = (randint(0, 10))
print(numero)
escolha = int(input('escolha um número:'))

while not escolha == numero:
    count += 1
    if escolha > numero:
        escolha = int(input('Você ERROU para menos! Escolha um número novamente:'))
    else:
        escolha = int(input('Você ERROU para mais! Escolha um número novamente:'))
if escolha == numero:
    print(f'"ACERTOU" o número sorteado foi {numero}')
    print(f'Foram necessários {count} palpites para acertar.')



