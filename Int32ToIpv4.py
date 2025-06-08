##############################
# int32 to IPv4
# Codewars 5kyu
##############################

def int32_to_ip(int32):
    
    # Format Number to Binary32Bits
    Binary32b = format(int32, '032b')
    
    # Convert each Byte to Number and then to String
    Octet1 = str(int(Binary32b[0:8], base=2))
    Octet2 = str(int(Binary32b[8:16], base=2))
    Octet3 = str(int(Binary32b[16:24], base=2))
    Octet4 = str(int(Binary32b[24:32], base=2))
    
    return Octet1 + "." + Octet2 + "." + Octet3 + "." + Octet4


#######################
# Another Approach
# Other User
#######################

# There is a library that convert seemly
# Source: https://docs.python.org/3/library/ipaddress.html

from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))
