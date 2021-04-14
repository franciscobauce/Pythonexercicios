t1 = float(input('digite um tamanho:'))
t2 = float(input('digite um tamanho:'))
t3 = float(input('digite um tamanho:'))

cores = ('azul' :'033[m')

lista = [t1, t2, t3]
lista = sorted(lista)

if lista[0] + lista[1] >= lista[2]:
    print('não é possivel formar um tringulo')
else:
    print('é possivel formar um triangulo')

