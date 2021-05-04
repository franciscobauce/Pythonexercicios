anterior = 0
proximo = int(input('digite um número:'))
i = 0


while i < 20:
    proximo = proximo + anterior
    anterior = proximo - anterior
    i += 1
    print(proximo, end=' ')