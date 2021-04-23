n = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: [ 1 ] converter para BINÁRIO')
print('Escolha uma das bases para conversão: [ 2 ] converter para OCTAL')
print('Escolha uma das bases para conversão: [ 3 ] converter para HEXADECIMAL')

op = int(input('Sua opção: '))

if op == 1:
    print(f'O número {n} em binário fica {bin(n)[2:]}')
elif op == 2:
    print(f'O número {n} em binário fica {oct(n)[2:]}')
elif op == 3:
    print(f'O número {n} em binário fica {hex(n)[2:]}')
else:
    print('Você digitou uma opção invalida, tente novamente!')

