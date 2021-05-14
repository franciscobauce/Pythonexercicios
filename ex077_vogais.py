lista = ('abacate', 'leite')
cont = 0
for pal in lista:
    print(f'\nNa palavra {pal.upper()} temos', end=' ')
    for vogal in pal:
        if vogal in 'aeiou':
            print(f'{vogal.upper()}', end=' ')








