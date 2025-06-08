####################
# Divisores 2n^2
# Project Euler 735
####################

#####
# Idea del problema:
# La busqueda de divbisores de un numero N va de 1...sqrt(N), lo que en este problema seria
# desde el rango 1...sqrt(2)N.
# Como no puede superar los divisores a N entonces la busquyeda se puede hacer hasta 1...N.
#
####


# Retorna la cantidad de divisores de 2Numero^2 pero que es menor a Numero
def Divisores2N2(Numero: int) -> int:
    Conteo = 1      # Divisor 1
    Pos = 2
    Num2NPow2 = 2*(Numero**2)
    
    # Tiene que llegar hasta num por la definicion del problema
    while Pos <= Numero:    # Se busca rango 2....Numero los divisores de 2n^2
        # Corrobora con 2N^2
        if (Num2NPow2 % Pos == 0):
            Conteo += 1
        Pos += 1
    return Conteo

print (Divisores2N2(3))

# Retorna la Sum f(1)+f(2).....+f(n)
def FSum(Numero: int) -> int:
    Total = 1
    for i in range(2,Numero+1):
        Total += Divisores2N2(i)
    return Total
    
#print (FSum(15)) #63
#print (FSum(1000)) #15066
#print (FSum(10000))
#print (FSum(1000000000000)) # ???
#L = []
#for i in range(1, 16):
#    L.append(FSum(i))
#print (L)