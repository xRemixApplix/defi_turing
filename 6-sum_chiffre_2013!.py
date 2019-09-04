#-*- coding: utf8 -*-

# Initialisation des valeurs
produit = 1
somme = 0
i = 2013

# Parcours des elements
while i > 0:
    # Produit de l'element avec valeur actuel
    produit *= i
    i -=1

# Parcours de chaque element du produit final
for char in str(produit):
    # Ajout de chaque element à la somme
    somme += int(char)
# Affichage de la somme 
print(somme)