opcao = ''
opcao2 = ''

while not opcao == 5:
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segundo valor:'))
    print('Os valores escolhidos foram:')
    print()
    print(f'{v1} e {v2}')
    print()
    print('O que voce quer fazer?')
    print()
    print('[ 1 ] Somar!')
    print('[ 2 ] Subtrair!')
    print('[ 3 ] Multiplicar!')
    print('[ 4 ] Dividir!')
    print('[ 5 ] Sair do programa')
    print('[ 6 ] Trocar números')
    print()
    opcao = int(input('Digite a opção desejada:'))
    print()
    if opcao == 4 or opcao == 3 or opcao == 2 or opcao == 1:
        if opcao == 1:
            print(f'O resultado da operação é {v1 + v2}')
        elif opcao == 2:
            print(f'O resultado da operação é {v1 - v2}')
        elif opcao == 3:
            print(f'O resultado da operação é {v1 * v2}')
        elif opcao == 4:
            print(f'O resultado da operação é {v1 // v2}')
        print()
        while not opcao2 == 9:
            opcao2 = int(input('Voce quer continuar?[S(9)/N(5)]:'))
            if opcao2 == 9:
                print('VAMOS LÁ')
            elif opcao2 == 5:
                print('tchau')
                opcao2 = 9
                opcao = 5
            else:
                print('OPÇÃO INVÁLIDA')
    elif opcao == 6:
        print('Escolha os números:')
        print('')
print('Até mais')

