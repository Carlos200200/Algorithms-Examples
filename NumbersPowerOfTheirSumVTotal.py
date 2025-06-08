###################################
# Numbers that are a power of their sum of digits
# Codewars 5kyu
# Version Final 2 (Mas de 6 versiones anteriores)
###################################
# Todas las versions intentadas
# Con la funcion suma+1
###################################

import math

SumaDig = 1
Numero = 10
def SumaMas1V2():
    global SumaDig, Numero
    
    i = 0
    SubNum = Numero    # Numero antes de la suma
    while SubNum%10 == 9:
        SubNum //= 10   # Se convierte sin el ultimo dig
        SumaDig -= 9    # El conteo total pierde 9 unidades
    SumaDig += 1 # Valor del digito +1
    Numero += 1  # Actulizar Num


def power_sumDigTerm(n):

    global Numero
    
    IthPower = 0
    while True:
        #if (IsPowerOfSum1(Numero)):
        #if (IsPowerOfSum2(Numero)):
        #if (IsPowerOfSum3(Numero)):
        #if (IsPowerOfSum4(Numero)):
        #if (IsPowerOfSum5(Numero)):
        #if IsPowerOfSum6(Numero):
        if IsPowerOfSum7(Numero):
            IthPower += 1
            print (Numero)
            if (IthPower == n):
                return Numero
        SumaMas1V2()  # +1 Numero


Log10 = [0, 0.07, 0.3, 0.47, 0.6, 0.69, 0.78, 0.85, 0.9, 0.95]
def IsPowerOfSum1(Number: int) -> bool:

    global SumaDig, Log10
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False

    # Number of digits of Number and SumDigits
    StrNumber = str(Number)
    StrSumDigits = str(SumDigits)
    NumDigits = len(StrNumber)
    NumSumDigits = len(StrSumDigits)

    #--------------------------
    # Using Aprox. methods and propieties of log
    # -------------------------
    
    # Loga(b) = ln(b)/ln(a), check neighboors
    # Aprox. log(b) and log(a); log(12345) = log(10000*1,2345) = log(10.000) + log(1,2)
    Power1 = (NumDigits - 1) + Log10[ int(StrNumber[0]) // 10]
    Power2 = (NumSumDigits - 1) + Log10[ int(StrSumDigits[0]) ]
    Power = Power1 // Power2
    PowerTest = pow(SumDigits,Power)
    if PowerTest == Number or PowerTest*SumDigits == Number:
        return True
    else:
        return False

def IsPowerOfSum2(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False

    #--------------------------
    # Using exact definition of Loga(b)
    # -------------------------

    Expo = int(math.log(Number, SumDigits))
    Power = SumDigits**Expo
    if Power == Number or Power*SumDigits == Number:
        return True
    else:
        return False

def IsPowerOfSum3(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False
    
    #--------------------------
    # Using front to back definition
    # -------------------------
 
    DivisorNumber = Number // SumDigits    # They are multiples
    while DivisorNumber > SumDigits:
        if DivisorNumber % SumDigits == 0:
            DivisorNumber //= SumDigits
        else:
            return False
        
    return True if DivisorNumber == SumDigits else False


def IsPowerOfSum4(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False
    
    #--------------------------
    # Using clasical definition
    # -------------------------

    PowerSumDigits = SumDigits
    while PowerSumDigits <= Number:
        PowerSumDigits *= SumDigits
        if (PowerSumDigits == Number):
            return True
    
    return False



def IsPowerOfSum5(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False
    
    #--------------------------
    # Using ver2 but with Log table predifined
    # -------------------------
    
    #Expo = LogNAprox(Number)//LogN[SumDigits]
    Expo = Log10Aprox(Number)//Log10N[SumDigits]
    Power = SumDigits**Expo
    #print (SumDigits, Expo, "=", Power)
    if Power == Number or Power*SumDigits == Number:
        return True
    else:
        return False
    

def LogNAprox(N):
    if (N <= 100):
        return LogN[N]
    else:
        return LogN[100] + LogNAprox(N//100)

def Log10Aprox(N):
    if (N <= 100):
        return Log10N[N]
    else:
        return Log10N[100] + Log10Aprox(N//100)


LogN = [0]
for i in range(1,101):
    LogN.append(math.log(i))

Log10N = [0]
for i in range(1,101):
    Log10N.append(math.log10(i))


## Prueba: cuantos valores hay en cada sumatoria?
#SumN = [0 for x in range(101)]  # List Comprehension
#for i in range (1, 60466176):
#    SumaMas1V2()
#    SumN [SumaDig] += 1
#print (SumN)

#Potencias a^b, <2,3,4,5...>, dura 0.0006194114685058594 seg
PotenciasX = [[1], [1]]
for i in range(2, 91):
    PotenciasX.append( [i**k for k in range(31)] )


def IsPowerOfSum6(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False
    
    #--------------------------
    # Using Binary Search but with Table Predefined
    # -------------------------

    if (PotenciasX[SumDigits][2] == Number): return True

    Lower = 2
    Upper = 30
    Media = 15  # Lower+Upper//2
    
    while (Upper - Lower > 1):        
        if ( PotenciasX[SumDigits][Media] > Number ):    # [Lower, Media]
            Upper = Media
        else:                                            # [Media, Upper]
            Lower = Media
        Media = (Lower+Upper) >> 1  # Sum//2

    return True if ( PotenciasX[SumDigits][Media] == Number ) else False


def IsPowerOfSum7(Number: int) -> bool:

    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False
    
    #--------------------------
    # Using classical search back to front
    # -------------------------

    i = 2
    while True:
        X = PotenciasX[SumDigits][i]
        if (X == Number):
            return True
        if (X > Number):
            return False
        i += 1



NumbersCondition = []
def IsPowerOfSum_Test(Number: int) -> bool:
    global SumaDig
    
    SumDigits = SumaDig

    # 1^n = 1
    if (SumDigits == 1): return False

    # At least Number is multiple of SumDigits or has the same parity (odd or even)
    if (Number%2 != SumDigits%2 or Number%SumDigits != 0):
        return False

    ## A partir de aqui los valores se mantienen
    NumbersCondition.append( (SumDigits, Number) )

    


import time
TInicial = time.time()
#print (power_sumDigTerm(15))
#Numero = 2000
#SumaDig = 2
#print (IsPowerOfSum5(2000))

#for i in range(10, 60466177):
for i in range(10, 60466177):
    IsPowerOfSum_Test(Numero)
    SumaMas1V2()

print (len(NumbersCondition))


print (time.time() - TInicial, "Segundos")
# Version 1: 26.4 seg promedio
# Version 2: 23.05 seg promedio
# Version 3: 21.8 seg promedio
# Version 4: 22.29 seg promedio
# Version 5: 27.4 seg promedio Ver ln(n)
#            28.7 seg promedio Ver log10(n)
# Version 6: 28.5 seg promedio
# Version 7: 28.8 seg promedio


#---------------------------
# RESPUESTAS
# [81, 512, 2401, 4913, 5832, 17576, 19683, 234256, 390625, 614656, 1679616,
# 17210368, 34012224, 52521875, 60466176]
#--------------------------- 
