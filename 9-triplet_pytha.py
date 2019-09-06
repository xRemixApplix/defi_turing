#-*- coding: utf8 -*-

import math
prod=0

for i in range(1, int(1800)):
    for j in range (i, 1800):
        k = int(math.sqrt(i**2+j**2))
        if i+j+k==3600 and i**2+j**2==k**2 and i*j*k>prod:
            prod=i*j*k
            #### CODE A RAJOUTER POUR DEBUGGER ####
            # print("{}, {} et {} : {}".format(i, j, k, i*j*k))
            #######################################

print("{}".format(prod))