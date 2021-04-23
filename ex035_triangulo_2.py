t1 = float(input('digite um tamanho:'))
t2 = float(input('digite um tamanho:'))
t3 = float(input('digite um tamanho:'))


lista = [t1, t2, t3]
lista = sorted(lista)

if lista[0] + lista[1] >= lista[2]:
    print('é possivel formar um triangulo')
    if lista[0] == lista[1] == lista[2]:
        print('É um tringulo equilátero')
    elif lista[0] != lista[1] != lista[2] != lista[0]:
        print('É um triângulo escaleno')
    else:
        print('É um triângulo isósceles')
else:
    print('não é possivel formar um tringulo')

    327,16

