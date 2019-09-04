#-*- coding: utf8 -*-

palind=0

# Fonction qui retourne le nombre 'miroir' du celui donné en parametre
def inverse(n):
    # Transformation en "str" du nombre
    n=str(n)
    # Initialisation d'une liste vide
    list = []
    # Parcours de la chaine de caractere
    for char in n:
        # On met chaque caractère de la chaine dans une liste
        list.append(char)
    # Inversion de la liste
    list.reverse()
    # Transformation de la liste en chaine de caractere
    n="".join(list)
    # On retourne la chaine transformer en entier
    return int(n)

# Parcours de tout les nombres à 3 chiffres
for i in range (100, 999):
    # Parcours de tout les nombres à 4 chiffres
    for j in range(1000, 9999):
        # Nombre a tester = produit de i et j
        num_a_tester=i*j
        # Si on trouve un palindrome et qu'il est supérieur au plus grand palindrome trouvé jusqu'à maintenant
        if num_a_tester==inverse(num_a_tester) and num_a_tester>palind:
            # Affection du palindrome à la variable 'palind'
            palind=num_a_tester

# A la fin, on affiche le plus grand palindrome trouv&
print("{}".format(palind))