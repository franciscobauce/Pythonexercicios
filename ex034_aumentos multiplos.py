salario = float(input('digite o salário:'))
if salario > 1250:
    print(f'{(salario * 10 / 100) + salario}')
else:
    print(f'{(salario * 15 / 100) + salario}')

