#-*- coding: utf8 -*-

from fonct_module import miroir
import math

palind = 0
nomb_a_test = 698


while palind == 0 :
    nomb_a_test+=1

    palin_nb = int(str(nomb_a_test)+str(miroir(nomb_a_test)[1]))
    print(palin_nb)

    if math.sqrt(palin_nb)%1 == 0 :
        palind = palin_nb

print(palind)