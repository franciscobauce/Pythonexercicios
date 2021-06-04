lista = []
pessoa = {}
dicio = {}
perg = ' '
while perg not in "N":
    pessoa['nome'] = str(input(f'digite seu nome:'))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input(f'Digite seu sexo[M/F]:'))[0].strip().upper()
        if sexo not in 'MF':
            print('errado')
        else:
            pessoa['sexo'] = sexo
    pessoa['idade'] = int(input(f'Digite sua idade:'))
    perg = str(input("Você quer continuar?[S/N]"))[0].strip().upper()
    dicio['cadastro'] = (pessoa.copy())
    lista.append(dicio.copy())
    pessoa.clear()
print(lista)
print(f'A) {len(lista)} pessoas foram cadastradas')
somaidade = 0
for c in lista:
    for v in c.values():
        somaidade += v["idade"]
media = somaidade // len(lista)
print(f'B) A média das idades é {media}')
print('C) As mulheres cadastradas foram:')
for c in lista:
    for k, v in c.items():
        if v['sexo'] in 'F':
            print(f'{v["nome"]}')
print(f'D) LISTA COM PESSOAS COM MAIS DE {media} ANOS  DE  IDADE:')
for c in lista:
    for k, v in c.items():
        for p, u in v.items():
            if v['idade'] > media:
                print(f'{p} = {u};', end=' ')

  #      if v['idade'] > media:
   #         print(f'PESSOAS COM MAIS DE {media} ANOS  DE  IDADE:')
    #        print(f'{k} {v}')




