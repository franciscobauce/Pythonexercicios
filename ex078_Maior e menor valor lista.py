valor = []
cont = 0
for n in range(0,5):
    valor.append(int(input(f'Posição {n}, Digite um número:')))
    cont =+ 1
print(valor)
a = min(valor)
b = max(valor)
print(f'O maior valor é {b} e está na posição {valor.index(b)}')
print(f'O menorvalor e {a} e está na posição {valor.index(a)}')



