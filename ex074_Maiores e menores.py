from random import randint

numeros = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(numeros)
print(sorted(numeros))
print(f'{sorted(numeros)[0]} MENOR')
print(f'{sorted(numeros)[-1]} MAIOR')