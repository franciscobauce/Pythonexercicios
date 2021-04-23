numero = int(input('Digite um número:'))
if numero == 3 or numero == 5 or numero == 7 or numero == 11:
    print ('primo')
elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0 and numero % 11 != 0:
    print('primo')
else:
    print('não primo')

