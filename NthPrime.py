##########################
# Find the 10001st Prime
# Problem 7 Poject Euler
##########################

import time
import math


def NthPrime(n: int) -> int:
    
    StartTime = time.time()
    
    NumPrime = 0    # Numero Primo Actual
    Numero = 1
    while NumPrime != n:
        Numero += 1
        if (IsPrime(Numero)):
            NumPrime += 1
    
    print ("Tiempo Total: ", time.time() - StartTime)
    
    return Numero
    
def IsPrime(Numero: int) -> bool:
    
    # First conditionals by definition
    if (Numero <= 1):
        return False
    if (Numero == 2): 
        return True
    if (Numero % 2 == 0):   # No deberia estar aqui si Numero == 2
        return False
        
    # Start on 3 and only test even numbers
    Pos = 3
    while Pos <= math.sqrt(Numero):
        if (Numero % Pos == 0):
            return False
        Pos += 2
    return True
    
print (NthPrime (10001))