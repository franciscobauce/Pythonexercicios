peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'seu imc é {imc:.2f}',end=' ')

if imc < 18.5:
    print('=> abaixo do peso')
elif 18.5 <= imc < 25:
    print('=> Peso Ideal')
elif  25 <= imc < 30:
    print('=> Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')