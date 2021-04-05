km = float(input('digite a km percorrida pelo veículo: km '))
dias = int(input('digite a quantidade de dias que o veículo foi utilizado: '))
custokm = km * 0.15
custodia = dias * 60
custototal = custokm + custodia
print(f'O custo total do aluguel do veículo foi de R${custototal:.2f}')

print(f'relatório detalhado de custos:')
print(f'gastos por kilometragem: R$ {custokm:.2f}')
print(f'gastos por dias utilizados: R$ {custodia:.2f}')