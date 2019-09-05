#-*- coding: utf8 -*-

import math

# Initialisation des variables
count=2
id=3
nb=5
# Tant que on pas atteint la 23456eme position des nombres premiers
while count < 23456 :
    # Verif primalite à False
    verif=False
    # Pour un nombre entre 2 et la racine carrée du nombre vérifié + 1
    for j in range(2, int(math.sqrt(nb))+1):
        # Si on trouve un multiple du nombre vérifiée
        if nb%j==0:
            # Verif primalite a True
            verif=True
    # Si Verif primalite est False
    if not verif:
        # Enregistrement du nombre premier trouve et de sa position
        id=nb
        count+=1
    # Increment du nombre verifiée
    nb+=1
# Affichage du 23456eme nombre premier
print("{}".format(id))
