import math


altura = 3
raio = 1
areaLateral = altura * (2 * math.pi * raio)
areaDasBases = 2 * (math.pi * math.pow(raio,2))
areaTotal = areaLateral + areaDasBases


print(round(areaTotal,2))