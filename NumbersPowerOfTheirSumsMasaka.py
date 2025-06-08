###################################
# Numbers that are a power of their sum of digits
# Codewars 5kyu
# Version Masaka (Mas de 6 versiones anteriores)
###################################
# Se usa una tabla y se busca de ahi los datos
###################################


#Tabla de Potencias a^b, <2,3,4,5...>, dura 0.0006194114685058594 seg
PotenciasTable = [[1], [1]]
for i in range(2, 91):
    PotenciasTable.append( [i**k for k in range(31)] )


# -------------------------
#    Incluso no necesito ni la tabla, ejecutando los valores hace los mismo
#    que acceer a memoria
# ----------------------------

def power_sumDigTerm(n):

    Results = []
    for a in range (2, 90):
        for b in range(2, 30):
            if ( IsPowerOfSumMasaka(PotenciasTable[a][b], a) ):
                Results.append(PotenciasTable[a][b])

    Results.sort()
    #print (Results, len(Results))
    return Results[n-1]

# A^x = Number
def IsPowerOfSumMasaka(Number: int, A: int) -> bool:

    # ----Vuelve esta version
    # Sum of Digits
    SumDigits = 0
    SubNumber = Number    # Number to divide
    while (SubNumber):      # While SubNumber != 0
        SumDigits += SubNumber % 10
        SubNumber = SubNumber // 10

    ## Se sabe que Number si es potencia, entonces es saber si su sama es A
    return True if (SumDigits == A) else False



import time
TInicial = time.time()
print(power_sumDigTerm(15))  # 0,029 seg, EN SERIO!!!!, max hasta n=40
print (time.time() - TInicial, "Segundos")



#---------------------------
# RESPUESTAS
# [81, 512, 2401, 4913, 5832, 17576, 19683, 234256, 390625, 614656, 1679616,
# 17210368, 34012224, 52521875, 60466176]
#---------------------------
