texto = str(input('digite uma palavra:')).strip().upper()
#pali = str(texto[-1:] + texto[-2:-1] + texto[-3:-2] + texto[-4:-3])#
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto)
print(inverso)