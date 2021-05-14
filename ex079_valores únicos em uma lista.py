valores = []
for c in range(0,1):
    v1 = int(input('Digite um valor:'))
    v2 = int(input('Digite um valor:'))
    v3 = int(input('Digite um valor:'))
    valores.append(v1)
    if v2 != v1:
        valores.append(v2)
    if v3 != v1 and v3 != v2:
        valores.append(v3)
print(valores)

