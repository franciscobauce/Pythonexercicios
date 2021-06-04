lista = []
for c in range(0, 3):
    n = int(input('digite um numero:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
lista = [0, 4, 5]
print(lista[-1])





