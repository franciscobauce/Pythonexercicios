saque: 0
while True:
    pergunta = ' '
    saque = int(input('Digite o valor do saque:'))
    n100 = saque // 100
    n100r = saque % 100
    n50 = n100r // 50
    n50r = n100r % 50
    n20 = n50r // 20
    n20r = n50r % 20
    n10 = n20r // 10
    n10r = n20r % 10
    n5 = n10r // 5
    n5r = n10r % 5
    if n100 != 0:
        print(f'{n100} notas de 100')
    if n50 != 0:
        print(f'{n50} notas de 50')
    if n20 != 0:
        print(f'{n20} notas 20')
    if n10 != 0:
        print(f'{n10} notas 10')
    if n5 != 0:
        print(f'{n5} notas 5')
    while not pergunta in'SN':
        pergunta = str(input('Voce quer fazer uma nova transação? [S/N]')).upper().strip()[0]
    if pergunta == 'N':
        break
print('FIM')




