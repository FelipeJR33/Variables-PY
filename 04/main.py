import math

capital = 1000
juros = 0.125
tempo = 5
montante = capital * ((1+juros) ** tempo)


print(int(montante))