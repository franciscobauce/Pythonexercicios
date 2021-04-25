from datetime import date

menor = 0
maior = 0
atual = date.today().year

for c in range(0 , 7):
    ano = int(input('Digite o ano seu ano de nascimento:'))
    idade = atual - ano
    if idade < 18:
        menor += 1
        print(f'{idade} - Menor de idade  ')
    if idade >= 18:
        maior += 1
        print(f'{idade} - Maior de idade')

print(f'{menor} pessoas são menores de idade')
print(f'{maior} pessoas são maiores de idade')



