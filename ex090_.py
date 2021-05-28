fichas = {}
fichas['nome'] = str(input('Nome:'))
fichas['nota'] = float(input(f'Média de {fichas["nome"]}:'))
print('__' * 30)
if fichas["nota"] > 7:
    fichas['resultado'] = ('Aprovado')
else:
    fichas['resultado'] = ('Reprovado')
for a, w in fichas.items():
    print(f'O {a} é {w}')
