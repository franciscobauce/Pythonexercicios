salario = float(input('Digite o valor do seu salário: R$ '))
reajuste = float(input('Digite o percentual de reajuste: % '))
diferenca = (salario * reajuste/100)
novo = salario + (salario * reajuste/100)
print(f'Com {reajuste}% de reajuste, o seu salário vai aumentar R${diferenca:.2f},  totalizando R${novo:.2f}')
