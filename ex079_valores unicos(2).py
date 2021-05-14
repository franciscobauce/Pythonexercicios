valores = []
for c in range(0,5):
    v1 = int(input('Digite um valor:'))
    if v1 not in valores:
        valores.append(v1)
print(sorted(valores))
