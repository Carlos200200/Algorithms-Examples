############################
# The Binary Binary Expansion
# Codewars 5kyu
############################


import math

def true_binary(n):
    
    # Got the first n<2^x
    Pos = int(math.log2(n))
    L = []
    
    Res = n
    for x in range(Pos, -1, -1):
        if Res > 0:
            L.append(1)
            Res -= (2**x)
        else:
            L.append(-1)
            Res += (2**x)
            
    return L


######
## Ver 2: A little of performance (number to 200.000 digits)
########

import math
import sys
sys.set_int_max_str_digits(0)

def true_binary2(n):
    
    # Got the first n<2^x
    Pos = int(math.log2(n))
    L = []
        
    Res = n
    Power = 2**Pos
    for x in range(0, Pos+1):
        if Res > 0:
            L.append(1)
            Res -= Power
        else:
            L.append(-1)
            Res += Power
        Power >>= 1
            
    return L

#######
## Ver. Final: Another approach only with list
## No idea the math behind this
########

#import sys
#sys.set_int_max_str_digits(0)

def true_binary(n):
    
    NBin = list( map(int, format(n, 'b')) )
    
    p = 0
    while p < len(NBin):
        if (NBin[p] == 0):
            NBin[p] = 1
            q = p + 1
            while (NBin[q] != 1):
                NBin[q] = -1
                q += 1
            NBin[q] = -1
            p = q
        p += 1
        
    return NBin


######
# Versiones Codewars
#

# [-1 if x == '0' else 1 for x in bin(n)[1:-1]]
#Creador del problema:
#true_binary=lambda n:[1]+[int(c)*2-1 for c in bin(n)[2:-1]]




import time
STime = time.time()
#true_binary(25841347989787928861)
print(time.time() - STime)

