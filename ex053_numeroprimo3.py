cont = 0
num = int(input('Digite um número:'))
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1                  
if cont == 2:
    print('é numero primo')
else:
    print('não é número primo')









