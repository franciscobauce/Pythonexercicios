lista = []
temp = []
while True:
    temp.append(str(input('Digite o nome do aluno:')))
    temp.append(float(input('Digite a primeira nota:')))
    temp.append(float(input('Digite a segunda nota nota:')))
    lista.append(temp[:])
    temp.clear()
    p = str(input('Você quer continuar?[S/N]'))
    if p in 'Nn':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{((c[1] + c[2]) // 2):>8.1f}')
while True:
    p2 = int(input('Mostrar nota de qual aluno?'))
    if p2 == 999:
        break
    else:
        print(f'{"NOME":<14}{"P1":>1}{"P2":>5}')
        print(f'{lista[p2][0]:<14}{(lista[p2][1]):>1} {lista[p2][2]:>5}')


