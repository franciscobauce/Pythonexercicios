from datetime import date

ano = int(input('digite o ano de seu nascimento:'))
idade = date.today().year - ano
print(idade)


if  idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('Master')










