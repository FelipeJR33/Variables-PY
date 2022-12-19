import math

jaDoentes = 1000
novosInfectadosPorDoente = 4
tempo = 100
totalDeInfectados = jaDoentes * math.pow(novosInfectadosPorDoente, tempo/7)

print(int(totalDeInfectados))