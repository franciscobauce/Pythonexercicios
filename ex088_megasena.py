
import random
jogos = []
temp= []
n = int(input('Digite o número de vezes de sorteios:'))
for c in range(0, n):
    temp.append(random.sample(range(0, 60), 6))
    jogos.append(temp[:])
    print(f'Jogo {c} --> números: {temp}')
    temp.clear()

