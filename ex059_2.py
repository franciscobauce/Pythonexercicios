from time import sleep

opcao2 = ''
opcao = ''
errada = ''
s = 0
v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
print()
while not opcao == 5:
    print('[ 1 ] Some!')
    print('[ 2 ] Subtraia!')
    print('[ 3 ] Multiplique!')
    print('[ 4 ] Divida!')
    print('[ 5 ] Sair do programa')
    print()
    opcao = int(input('Digite a opção desejada:'))
    print()
    if opcao == 1:
        print(f'O resultado da operação é {v1 + v2}')
    elif opcao == 2:
        print(f'O resultado da operação é {v1 - v2}')
    elif opcao == 3:
        print(f'O resultado da operação é {v1 * v2}')
    elif opcao == 4:
        print(f'O resultado da operação é {v1 // v2}')
    print()
    opcao2 = str(input('Voce quer continuar?[S/N]:')).strip().upper()
    if opcao2 == 'N':
        print('tchau')
        opcao = 5
    else:
        while opcao2 != 'N':
             opcap= str(input('Opção errada, digite novamente:')).strip().upper()
             opcao = 5

print('Até mais')

