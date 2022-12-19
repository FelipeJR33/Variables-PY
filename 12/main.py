import math

montante = 90_000
capital = 60_000
periodoEmMeses = 24
taxaDeJuros = math.pow(montante/capital, 1/periodoEmMeses) - 1


print(f'O seu financiamento de {capital} reais teve uma taxa de juros de {round(taxaDeJuros*100, 3)}%, pois após {periodoEmMeses} meses você teve que pagar ${montante} reais.')
