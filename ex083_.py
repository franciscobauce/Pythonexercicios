lista = ['arvore', 'feijao']
cont1 = 0
cont2 = 0
for c in lista:
    for a in c:
        print(a)
        if a in '(':
            cont1 += 1
        if a in ')':
            cont2 += 1
print(cont1)
print(cont2)
print('até mais')