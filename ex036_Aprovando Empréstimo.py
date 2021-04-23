casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$ '))
parcelas = float(input('digite o número de parcelas:'))

valpar = casa // parcelas
percentual = 30/100
sal30 = salario * percentual/100

n1 = valpar * 10
n2 = (1 - (70/100)) * 10
necessario = n1 // n2

print(f'O Valor da parcela é de R${valpar:.2f}')

if valpar > sal30:
    print(f'Não é possivel fazer o seu financiamento, o valor da parcela é maior que 30 % do seu salário')
    print(f'Nessa condições o seu salário precisa ser no mínimo de:{necessario:.2f}')

else:
    print(f'seu financimaneto foi aprovado:')
    print(f'Em {parcelas} parcelas, o valor fica R${valpar} mensais')

