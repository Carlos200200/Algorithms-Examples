####################################
# Extract the domain name from a URL
# Codwwars 5kyu
###################################


import re

def domain_name(url):
    
    # Eliminating the 1st part of a url (http, www, etc...)
    Domain = re.sub("https?://|www.", "", url)
    
    # Pruning the rest (.com, .net, etc...)
    # \. -> scape of "."; .* -> Any letter 0+ ocurrences
    Domain = re.sub("\..*", "", Domain)
    
    return Domain

#########################
# Another Approach
########################

import re

# Group0=All match, Each group is in "()"
# Retrieve group 3 because is where is the domain
def domain_name(url):
    Pattern = "(https?://)?(www.)?([a-z0-9\-]+).\S+"
    return re.search (Pattern, url).group(3)
