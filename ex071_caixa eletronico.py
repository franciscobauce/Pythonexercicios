saldo = 1000
not1 = 100
not2 = 50
not3 = 10
while True:
    saque = int(input('valor do saque:'))
    saldo -= saque
    print(saldo)
    if saldo == 0:
        break


