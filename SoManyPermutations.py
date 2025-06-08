#############################
## So Many Permutations!
## Codewars 4 Kyu
#############################


################
# Create the permutations of a string
# Can't repeat, so can be a set
##



Permutations = []

def permutations(s):
    global Permutations
    
    # Test Problems: doesnt restart Permutations
    Permutations = []
    FormatPerm = []
    
    CreatePermutations(list(s), [])
    
    # Convert to string
    for i in range(0, len(Permutations)):
        String = ''
        for k in range(0, len(s)):    # len(s) = len(Permutations[i])
            String += Permutations[i][k]
        FormatPerm.append(String)
    
    return set(FormatPerm)

def CreatePermutations(Values, SubString):
    global Permutations
    
    if (len(Values) == 1):
        SubString.append(Values[0])
        Permutations.append(SubString)
    else:
        for i in range(0, len(Values)):
            TempSubString = SubString.copy()
            TempSubString.append(Values[i])
            TempValues = Values.copy()
            TempValues.pop(i)
            CreatePermutations(TempValues, TempSubString)
    return



############################
## Another Approach:
## Using Itertools, map and join
############################

import itertools

def Permutations(s):
    return list(map(''.join,itertools.permutations(s)))
