ano = int(input('digite um ano:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 > 0:
    print('é ano bisexto')
else:
    print('não é ano bisexto')