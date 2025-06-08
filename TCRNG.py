# Genera una lista n de numeros Pseudo Aleatorios usando LCG
def TCRNG(Semilla: int, a: int, c: int, Modulo: int, N: int):
    
    Lista = []

    for i in range(N):
        Semilla = ( (a * Semilla) + c) % Modulo     # La Semilla se mantiene en este scope
        Lista.append(Semilla)
    
    print (Lista)
    
#TCRNG (5, 2, 4, 10, 50)     # Se repite mucho despues de 4 elementos
#TCRNG (5, 2, 4, 25, 50)     # Se repite despues de 20 elementos
#TCRNG (7, 4, 8, 28, 50)     # Se repite despues de 3 elementos
#TCRNG (1, 1, 1, 64, 100)     # No se repite en 63 elementos, pero es lineal


# Revisa cuando se repite el ciclo del TCRNG
# Se sabe que en el momento q de el mismo valor inicial, por defincion de la formula
# que depende del valor anterior, los valores subsecuenctes dan lo mismo
# Modulo: Debe ser potencia de 2
# N: Se deberia dejar como 100 (random hasta 100)
def PeriodosTCRNG(Semilla: int, Modulo: int, N: int):
    
    a = 1
    while a < Modulo:          # a no puede ser 0
        c = 0
        while c < Modulo:
            i = 0
            X = Semilla
	    Lista = []
            
            while i < N:
                X = ( (a * X) + c) % Modulo
                
                if (X == Semilla):
                    print("a =", a, "; c =", c, "; Total = ", i, sep=" ")
		    if (i > 30):
                        print (Lista)
                    break
                i += 1

	     c += 1
    	a += 1

PeriodosTCRNG(1, 64, 100)



###########################################################

import random

# Seed Defautl: Hora del sistema
random.seed()
print (random.random())
print (random.random())

# Estos dan lo mismo porque se "reinicia" esa "sucesion randomica"
random.seed(100)
print (random.random())
print (random.random())

random.seed(100)
print (random.random())
print (random.random())


###############################################
## Weighed Random Number
###############################################

# Sacar el random con peso, se podria suponer una lista segun su peso y luego hacer un random normal:
#   [A,B,C,D] Pesos=[1,2,3,4]  ----->   [A,B,B,C,C,C,D,D,D,D]

import random

# Valores: Lista de String
# Pesos: Lista de Numeros
def WeightedRNG(Valores, Pesos):
    
    # Total Pesos de esta lista
    TotalPesos = 0
    for i in Pesos:
        TotalPesos += i
        
    # Inicia el valor random (el seed default es tiempo del sistema)
    # Usa el Metodo Mersenne Twister
    random.seed()
    RandomNum = int(random.random() * TotalPesos)    # Va desde [0, TotalPesos), se coge la parte entera
    
    SubPesos = 0
    Pos = 0
    for p in Pesos:
        SubPesos += p
        if (SubPesos >= RandomNum + 1):     # SubPesos va hasta RandomNum+1 que es TotalPesos
            print ("RandomNum = ", RandomNum, " Valor: ", Valores[Pos])
            return 1
        Pos += 1
        
    return -1
    
WeightedRNG(["A", "B", "C", "D"], [1,2,3,4])
