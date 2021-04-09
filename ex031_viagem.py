viagem = float(input('Digite em KM a distância da viagem: '))
vcurta = 0.50
vlonga = 0.45
if viagem <= 200:
    print(f'O custo total da viagem de km {viagem:.0f} foi de R${viagem * vcurta:.2f} \ '
          f'Sendo o custo por km percorrído de R$ {vcurta:.2f}')
else:
    print(f'O custo total da viagem de km {viagem:.0f} foi de R${viagem * vlonga:2.2f}')
    print(f'Sendo o custo por km percorrido de R$ {vlonga:.2f}')
    print(f'Por ser uma viagem com mais de 50km, você está economizando R$ {(viagem * vcurta) - (viagem * vlonga):.2f}!!')
