texto = str(input('digite uma palavra:')).strip().upper()
pali = str(texto[-1:] + texto[-2:-1] + texto[-3:-2] + texto[-4:-3])

if pali == texto:
    print('palindromo')
