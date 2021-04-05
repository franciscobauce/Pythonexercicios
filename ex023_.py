numero = input('digite um número:')
u = numero[-1::]
d = numero[-2:-1:]
c = numero[-3:-2:]
m = numero[-4:-3:]

print(f'unidade {u}')
print(f'dezena {d}')
print(f'centena {c}')
m = (m.replace('','0'))

print(f'milhar {m.rstrip()}')
