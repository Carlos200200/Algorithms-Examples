################
# Pruebas Time
################


import time

# Prueba FOR
TInicial = time.time()

for i in range(1, 10000000):
    SumDigits = 0
    for Digits in str(i):
        SumDigits += int(Digits)

print (time.time() - TInicial)

# Prueba WHILE
TInicial = time.time()
i=0
while i < 10000000:
    SumDigits = 0
    for Digits in str(i):
        SumDigits += int(Digits)
    i += 1

print (time.time() - TInicial)

# Prueba no str() y int()
TInicial = time.time()

for i in range(1, 10000000):
    SumDigits = 0
    j = i
    while j > 99:
        SumDigits += j % 10
        j = j // 10
    SumDigits += j % 10
    SumDigits += j // 10

print (time.time() - TInicial)


