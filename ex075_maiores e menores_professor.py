from random import randint

numeros = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

for n in numeros:
    print(n , end=' ')
print(f'\n{min(numeros)} Menor')
print(f'{max(numeros)} Maior')