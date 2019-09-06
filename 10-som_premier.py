#-*- coding: utf8 -*-

import math

# Initialisation des variables
somme=5
i=5

while i < 10000000:
    verif=False
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            verif=True
            break

    if not verif:
        print(i)
        somme+=i

    i+=2
        
print("{}".format(somme))