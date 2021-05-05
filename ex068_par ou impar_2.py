from random import randint
cont = 0

while True:
    jogadoresc = ' '
    while jogadoresc not in 'PI':
        print('[P] PAR')
        print('[I] ÍMPAR')
        jogadoresc = str(input('Digite a opção escolhida:')).strip().upper()[0]
    if jogadoresc == 'P':
        print(f'Jogador escolheu PAR')
        print(f'computador escolheu ÍMPAR')
    else:
        print(f'Jogador escolheu ÍMPAR')
        print(f'computador escolheu PAR')
    jogador = int(input('digite o número escolhido:'))
    computador = randint(1,10)
    print(f'Jogador jogou {jogador}')
    print(f'Computador jogou {computador}')
    resultado = (jogador + computador) % 2
    if resultado == 0:
        print("Deu Par")
    else:
        print('Deu Ímpar')
    if jogadoresc == 'P':
        if resultado == 0:
            print('Jogador venceu')
        else:
            print('Computador venceu')
    if  jogadoresc == 'I':
        if resultado == 1:
            print('Jogador venceu')
        else:
            print('Computador venceu')
    if jogadoresc != resultado:
        break
    cont += 1
print(f'Jogador venceu {cont} partidas consecutivas')









#while True:
 #   print('[0] PAR')
  #  print('[1] ÍMPAR')
   # jogadoresc = int(input('Digite a opção escolhida:'))
    #computadoresc = randint(0, 1)
    #if jogadoresc == 0:
     #   print(f'Jogador escolheu PAR')
    #else:
     #   print(f'jogador escolheu ÍMPAR')
    #if computadoresc == 1:
     #   print(f'computador escolheu PAR')
    #else:
     #   print(f'computador escolheu ÍMPAR')
   # if jogadoresc == computadoresc:
    #    break
