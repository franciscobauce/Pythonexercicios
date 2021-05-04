primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    print(total)
    mais = int(input('quantos termos mais voce quer mostrar?:'))
print('FIM')
















