n = []
cont = 0
while True:
    n.append(int(input('Digite um numero:')))
    cont += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Você quer continuar?[S/N}')).strip().upper()[0]
    if p == 'N':
        break
print('Até mais')
print(f'Você digitou {len(n)} elementos')
print(sorted(n, reverse = True))
print(f'Foram adicionados a lista {cont} números')
if 5 in n:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

