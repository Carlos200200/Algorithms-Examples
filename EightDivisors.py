##############################
# Problema 501 Project Euler
# Eight Divisors
#############################

## Proximo: Problem 837: Amidakuji

# Alguna info sobre sacar los Multiplos de n
# 1. Se puede recorrer de 1...n buscando si es multiplo o no
# 2. Viendo como "salen" los multiplos se puede ver q siguen en pares
#   2.1 Con esto se puede ver que puede ir de 1...n/2
#   2.2 Incluso, bajo el racionamiento de los primos puede ser de 1...sqrt(n)
#
# 3. Curiosamente, si sqrt(n) es entero entonces el numero tiene MULTIPLOS IMPARES
#    3.1 Funciones como math.frexp() o mejor N - int(N) para sacar los decimales

import math

# Retorna si hay 8 divisores en el numero n
def Hay8Divisores(Numero: int) -> bool:
    
    RaizNumero = math.sqrt(Numero)
    
    #if (RaizNumero - int(RaizNumero) == 0.0):
    #    return False
    
    # Recorrido de 2...sqrt(n)
    i = 2               # Valor temporal de multiplo, i -> 2...sqrt(n)
    Conteo = 2          # El 1 y el n
    while i <= RaizNumero:
        if (Numero % i == 0):
            Conteo += 2         # El multiplo actual y su hermano
            if (Conteo > 8):    # Corrobora si supera el limite
                return False
        i += 1
    
    # Ternary solo como ejercicio
    # Si sqrt(n) es entero entocnes los multiplos de n son impares, por lo que ese condicional hay q ponerlo
    return True if (Conteo == 8 and ((i-1)**2 != Numero)) else False

# print (Hay8Divisores (64))

# Cuenta cuantos numeros hasta Numero tienen 8 divisores
def Conteo8Divisores(Numero: int) -> int:
    Conteo = 0
    Div = []
    for i in range(2,Numero+1):
        if (Hay8Divisores(i)):
            Conteo += 1
            Div.append(i)
    print (Div)
    return Conteo

#print(Conteo8Divisores(100)) # 10
print(Conteo8Divisores(1000)) # 180
#print(Conteo8Divisores(1000000)) # 224427
#print(Conteo8Divisores(1000000000000)) # ????


################################################################################
## Intento Verison 2 del problema: Cambio del sqrt, pero hay q revisar tiempo de ejecucion
## Tiempo: A 20000 tiene 25 seg.
################################################################################


import math

# Retorna si hay 8 divisores en el numero n
def Hay8Divisores(Numero: int) -> bool:
    LimiteBusqueda = Numero
    PosBusqueda = 2              
    Conteo = 2          # El 1 y el n
    while PosBusqueda < LimiteBusqueda:
        if (Numero % PosBusqueda == 0):
            Conteo += 2         # El multiplo actual y su hermano
            LimiteBusqueda = Numero//PosBusqueda
            #print ("LimBusq: ", LimiteBusqueda)
            if (Conteo > 8):    # Corrobora si supera el limite
                return False
        PosBusqueda += 1
    
    # Si la raiz es entera entonces en verdad no se cuenta 2 sino 1
    return True if (Conteo == 8 and ((PosBusqueda-1) != LimiteBusqueda)) else False

#print (Hay8Divisores (64))

# Cuenta cuantos numeros hasta Numero tienen 8 divisores
def Conteo8Divisores(Numero: int) -> int:
    Conteo = 0
    #Div = []
    for i in range(2,Numero+1):
        if (Hay8Divisores(i)):
            Conteo += 1
            #Div.append(i)
    #print (Div)
    return Conteo

#print(Conteo8Divisores(100)) # 10
#print(Conteo8Divisores(1000)) # 180
print(Conteo8Divisores(1000000)) # 224427
#print(Conteo8Divisores(1000000000000)) # ????


#################################################################################################
## Intento 3: Con una lista que revise por lo menos si hay o no 8 divisores
## Tiempo: A 20000 tiene 0.5seg
#################################################################################################

import math
import time

TDiv = [0] * 1000000

# Retorna si hay 8 divisores en el numero n
def Hay8Divisores(Numero: int) -> bool:
    #LimiteBusqueda = Numero
    PosBusqueda = 2              
    Conteo = 2          # El 1 y el n
    RaizNumero = math.sqrt(Numero)
    
    # 1ra Busqueda, encuentra el penultimo divisor y revisa si este supera el valor
    # No olvidar que si es un primo, la busqueda revisa todo (son el 5%)
    while PosBusqueda <= RaizNumero:
        if (Numero % PosBusqueda == 0):
            Conteo += 2         # El multiplo actual y su hermano
            #LimiteBusqueda = Numero//PosBusqueda
            if (TDiv[Numero//PosBusqueda] >= 8):     # Esto supera los 8 divisores min
                TDiv[Numero] = 9    # Es una referencia q es mayor a 8
                return False
            else:
                PosBusqueda += 1
                break
        PosBusqueda += 1
    
    # 2da Busqueda, el Resto de valores    
    while PosBusqueda <= RaizNumero:
        if (Numero % PosBusqueda == 0):
            Conteo += 2         # El multiplo actual y su hermano
            if (Conteo > 8):    # Corrobora si supera el limite
                TDiv[Numero] = 9    # Es una referencia q es mayor a 8
                return False
        PosBusqueda += 1
    
    # Si la raiz es entera entonces en verdad no se cuenta 2 sino 1
    if (PosBusqueda-1 == RaizNumero):  # Raiz es entera
        TDiv[Numero] = Conteo-1
        return False
    if (Conteo == 8):
        TDiv[Numero] = Conteo
        return True

#print (Hay8Divisores (64))

# Cuenta cuantos numeros hasta Numero tienen 8 divisores
def Conteo8Divisores(Numero: int) -> int:
    Conteo = 0
    #Div = []
    for i in range(2,Numero+1):
        if (Hay8Divisores(i)):
            Conteo += 1
            #Div.append(i)
    #print (Div)
    return Conteo

TiempoInicial = time.time()

#print(Conteo8Divisores(100)) # 10
#print(Conteo8Divisores(1000)) # 180
#print(Conteo8Divisores(20000)) # 
print(Conteo8Divisores(1000000)) # 224427
#print(Conteo8Divisores(1000000000000)) # ????

print (time.time() - TiempoInicial)


############################################
# Estas funciones son para observar la complejidad de obtener la parte decimal de una raiz de distintas maneras.


def PotenciasCuadradaV1(Numero: int):
    Count = 0
    for i in range (1, Numero+1):
        RaizNumero = math.sqrt(i)
        if (RaizNumero - int(RaizNumero) == 0.0):
            Count += 1
    return Count
    
def PotenciasCuadradaV2(Numero: int):
    Count = 0
    for i in range (1, Numero+1):
        RaizNumero = math.sqrt(i)
        Fracc, Entero = math.modf(RaizNumero)
        if (Fracc == 0.0):
            Count += 1
    return Count
    
def PotenciasCuadradaV3(Numero: int):
    Count = 0
    for i in range (1, Numero+1):
        RaizNumero = math.sqrt(i)
        Fracc = RaizNumero % 1
        if (Fracc == 0.0):
            Count += 1
    return Count
            
#print (PotenciasCuadradaV1(1000000))
#print (PotenciasCuadradaV2(1000000))
#print (PotenciasCuadradaV3(1000000))