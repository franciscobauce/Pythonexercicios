numeros = []
for i in range(1, 5 + 1):
    numeros.append(float(input("Digite seu peso: kg ")))
ordenados = sorted(numeros)

print(ordenados[0])
print(ordenados[-1])