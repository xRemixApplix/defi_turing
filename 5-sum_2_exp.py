#-*- coding: utf8 -*-

# Initialisation de la valeur de la somme
somme = 0
# Parcours de chaque element du resultat de 2exp2222
for char in str(2**2222):
    # Ajout de chaque element à la somme
    somme += int(char)
# Affichage de la somme 
print(somme)