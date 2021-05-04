from random import randint

n1escolha = int(input('Escolha [PAR] (00) ou [IMPAR] (11):'))
n1 = int(input('digite o número escolhido:'))
n2 = randint(1,10)
resultado = (n1 + n2) % 2


if n1escolha == 00:
    if resultado == 0:
        print('n1 venceu')
    else:
        print('n2 venceu')

if  n1escolha == 11:
    if resultado == 0:
        print('n2 venceu')
    else:
        print('n1 venceu')
print(n1)
print(n2)

print(resultado)




