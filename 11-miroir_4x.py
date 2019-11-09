#-*- coding: utf8 -*-

from fonct_module import miroir

# Parcours des nombres de 0 à 2 500 000 (et non 10 000 000 car le 'n' ne peut avoir que 7 chiffres et 4*2 500 000 à 8 chiffres)
for i in range (2500000):
    # Si le miroir de 'n' est egale à 4 x 'n', 'number' egal 'i' sinon il reste egal a 'number'
    number = i if miroir(i)[0]==4*i else number
    
# A la fin, on affiche la reponse
print("{}".format(number))