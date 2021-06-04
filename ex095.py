jogador = dict()
partidas = list()
time = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    perg = str(input('Você quer continuar?[S/N] '))
    if perg in "Nn":
        break
print('-=' * 30)
print(time)
print('-=' * 30)
print('cod nome gols  total')
for i, k in enumerate(time):
    print(f'{i} {k["nome"]} {k["gols"]} {k["total"]}')
while True:
    q = int(input('Mostrar dado de qual jogador? [999 para parar]'))
    print(time[q]['nome'])
    print(time[q]['gols'])
    for i, g in enumerate(time[q]["gols"]):
        print(f'No jogo {i} fez {g} gols')
    if q == 999:
        break
#for k, v in jogador.items():
 #  print(f'O campo {k} tem o valor {v}')
#print('-=' * 30)
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
#for i, v in enumerate(jogador['gols']):
#    print(f' => Na partida {i}, fez `{v} gols')
#print(f'Foi um total de {jogador["total"]} gols')

