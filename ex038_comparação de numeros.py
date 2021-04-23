n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))

if n1 > n2:
    print(f'Primeiro valor é maior!', end=' ' 
          f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'Segundo valor é maior!', end=' '
          f'{n2} é maior que {n1}')
else:
    print('Os dois numeros possuem o mesmo valor')


