lista = ('arroz', 3.00, 'feijão', 5.00, 'massa', 3.00, 'lentilha', 51.00, 'açucar', 3.50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:-<30}', end=' ')
    else:
        print(f'R${lista[pos]:>5.2f}')


