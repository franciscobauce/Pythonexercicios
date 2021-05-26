lista = []
dados = []
contn = 0
for c in range(0,4):
    dados.append(input('O seu nome:'))
    dados.append(input('Digite o peso:'))
    if c == 0 or dados[1] > lista[-1][1]:
        lista.append(dados[:])
    else:
        pos = 0
        while pos < len(lista):
            if dados[1] <= lista[pos][1]:
                lista.insert(pos, dados[:])
                break
            pos += 1
    dados.clear()
    contn += 1
print(lista)
print(f'{contn} pessoas foram cadastradas')
print(f'os maiores pesos foram {lista[0][0]} com {lista[0][1]}kg e {lista[1][0]} com {lista[1][1]}kg')
print(f'os maiores pesos foram {lista[-1][0]} com {lista[0][1]}kg e {lista[-2][0]} com {lista[1][1]}kg')
