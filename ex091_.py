import random
from time import sleep
jogador = {}
grupo = []
ordem = []
final = {}
jogador["jogador"] = str(input('Digite seu nome:'))
jogador["dado"] = random.randint(1, 6)
grupo.append(jogador.copy())
print('Números Sorteados:')
print(f'jogador {jogador["jogador"]}', end=' ')
print(f'tirou {jogador["dado"]}')
sleep(0.5)
for c in range(1,6):
    jogador["jogador"] = (f'{c}')
    jogador["dado"] = random.randint(1, 6)
    grupo.append(jogador.copy())
    print(f'jogador{jogador["jogador"]}', end=' ')
    print(f'tirou {jogador["dado"]}')
    sleep(0.5)
print()
print('RANKING:')
for i, c in enumerate(grupo):
    if i == 0 or grupo[i]['dado'] > ordem[-1]['dado']:
        ordem.append(grupo[i])
    else:
        pos = 0
        while pos < len(ordem):
            if grupo[i]['dado'] <= ordem[pos]['dado']:
                ordem.insert(pos, grupo[i])
                break
            pos += 1
for i, c in enumerate(ordem[::-1]):
    print(f'{i+1}º lugar: Jogador {c["jogador"]} com {c["dado"]}')






#for j in grupo:
 #   for k, v in j.items():
  #      print(f'})




   # print(f'jogador {c} ', end='')
    #sorteio = random.randint(1, 6)
    #print(f'tirou {sorteio} no dado')
