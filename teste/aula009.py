import random

frase = ("""Ouviram do Ipiranga as margens plácidas
De um povo heroico o brado retumbante
E o sol da liberdade, em raios fúlgidos
Brilhou no céu da pátria nesse instante""")
dividido = frase.split()
print(dividido)
escolhido = random.choice(dividido)
print('a palavras escolhida foi:', escolhido)



