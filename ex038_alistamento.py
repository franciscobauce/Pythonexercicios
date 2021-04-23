from datetime import date

nascimento = int(input('Digite o ano do seu nascimento:'))
anoatual = date.today().year
idade = anoatual - nascimento
falta = 18 - idade
passou = idade - 18

if idade == 17:
    print(f'Você tem {idade} anos, ainda não tem idade para se alistar, você deve se alistar daqui há {falta} ano!'
          f'Você deverá se alistar em {falta + anoatual}')

elif idade < 17:
    print(f'Você tem {idade} anos, ainda não tem idade para se alistar, você deve se alistar daqui {falta} anos!')

elif idade == 18:
    print('Aliste-se, você está na idade certa!')

elif idade > 18:
    print(f'Você tem {idade} anos já passou da idade de se alistar, se você ainda não se alistou, aliste-se você está {passou} anos atrasado!'
          f'Voce deveria ter se alistado em {anoatual - passou}')


