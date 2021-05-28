listanum = []
mai = 0
men = 0
max = 0
min = 0
for c in range(0, 5):
    listanum.append(int(input('Digite um número:')))
    if c == 0:
        mai = listanum[c]
        men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'o maior valor foi {mai} e está na posição ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'o menor valor foi {men} e está na posição ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()








