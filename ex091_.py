import random
jogador = {}
grupo = []
ordem = []
print('Números Sorteados:')
for c in range(1,5):
    jogador["jogador"] = (f'{c}')
    jogador["dado"] = random.randint(1, 6)
    grupo.append(jogador.copy())
    print(f'jogador{jogador["jogador"]}', end=' ')
    print(f'tirou {jogador["dado"]}')
print()
print('RANKING:')
for c in grupo:
    if c == 0:
        ordem.append(grupo[0][:])
print(ordem)



#for j in grupo:
 #   for k, v in j.items():
  #      print(f'})




   # print(f'jogador {c} ', end='')
    #sorteio = random.randint(1, 6)
    #print(f'tirou {sorteio} no dado')
