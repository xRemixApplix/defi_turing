#-*- coding: utf8 -*-

from fonct_module import miroir

palind=0

# Parcours de tout les nombres à 3 chiffres
for i in range (100, 999):
    # Parcours de tout les nombres à 4 chiffres
    for j in range(1000, 9999):
        # Nombre a tester = produit de i et j
        num_a_tester=i*j
        # Si on trouve un palindrome et qu'il est supérieur au plus grand palindrome trouvé jusqu'à maintenant
        if num_a_tester==miroir(num_a_tester)[0] and num_a_tester>palind:
            # Affection du palindrome à la variable 'palind'
            palind=num_a_tester

# A la fin, on affiche le plus grand palindrome trouv&
print("{}".format(palind))