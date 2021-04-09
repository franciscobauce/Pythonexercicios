from time import sleep

velocidade = int(input('Digite a velocidade do veículo:'))
multa = (velocidade - 80) * 7.00
excesso = (velocidade - 80)
print('PROCESSANDO')
sleep(1)
if velocidade >80:
    print(f'O veículo ultrapassou em {excesso}Km/h o limite de velocidade')
    print(f'O valor a ser pago de multa é de R${multa:.2f}')
else:
    print('O veículo está dentro do limite de velocidade')