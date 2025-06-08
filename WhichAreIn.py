#######################
# CodeWars 6Kyu Which are In?
#######################

def in_array(array1, array2):
    R = []
    for Word1 in array1:
        for Word2 in array2:
            if (Word1 in Word2):
                R.append(Word1)
                break
    R.sort()
    
    # Since Python 3.7 dict is guaranteed to maintain insertion order
    return list(dict.fromkeys(R))