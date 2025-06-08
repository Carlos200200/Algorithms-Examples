###############
# Itertools (Pruebas)
###############


import time
import operator

L1 = list(range(1, 10001))
L2 = list(range(1, 10001))

def Mul(a,b):
    return a*b


#-------------------
# Prueba Eficiencia de Multiplicar 2 Listas
#-------------------

def MulListasClasica(L1, L2):
    Result = []
    for i in range(len(L1)):
        Result.append(L1[i]*L2[i])
    return Result

def MulListasListComprehension(L1, L2):
    return [L1[i]*L2[i] for i in range(len(L1))]

def MulListaMap1(L1, L2):
    return list(map(Mul, L1, L2))
def MulListaMap2(L1, L2):
    return list(map(lambda x,y: x*y, L1, L2))
def MulListaMap3(L1, L2):
    return list(map(operator.mul, L1, L2))

## Ciclos de prueba

NumIteraciones = 10
TMulLClasica = []
TMulLListCom = []
TMulLMap1 = []
TMulLMap2 = []
TMulLMap3 = []

for _ in range(NumIteraciones):
    TInicial = time.time()
    MulListasClasica(L1,L2)
    TFinal= time.time()
    TMulLClasica.append(TFinal-TInicial)

for _ in range(NumIteraciones):
    TInicial = time.time()
    MulListasListComprehension(L1,L2)
    TFinal= time.time()
    TMulLListCom.append(TFinal-TInicial)

for _ in range(NumIteraciones):
    TInicial = time.time()
    MulListaMap1(L1,L2)
    TFinal= time.time()
    TMulLMap1.append(TFinal-TInicial)

for _ in range(NumIteraciones):
    TInicial = time.time()
    MulListaMap2(L1,L2)
    TFinal= time.time()
    TMulLMap2.append(TFinal-TInicial)

for _ in range(NumIteraciones):
    TInicial = time.time()
    MulListaMap3(L1,L2)
    TFinal= time.time()
    TMulLMap3.append(TFinal-TInicial)

# Sacar promedio

print ("Promedio:", sum(TMulLClasica)/NumIteraciones)  # 0.0009102 seg
print ("Promedio:", sum(TMulLListCom)/NumIteraciones)  # 0.0007861 seg
print ("Promedio:", sum(TMulLMap1)/NumIteraciones)     # 0.0009721 seg
print ("Promedio:", sum(TMulLMap2)/NumIteraciones)     # 0.0009601 seg
print ("Promedio:", sum(TMulLMap3)/NumIteraciones)     # 0.0005039 seg


#################
# Clasico < ListComprehension < Map < Map con OperadorMul
################

