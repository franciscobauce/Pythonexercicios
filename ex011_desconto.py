valor = float(input('digite o valor do produto:R$ '))
desconto = float(input('digite o percentual de desconto: %'))
novo = valor-(valor/100*desconto)
print(f'o valor do produto com {desconto}% de desconto, fica R$ {novo:.2f}')