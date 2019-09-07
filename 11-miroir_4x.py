#-*- coding: utf8 -*-

number=0

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

# Parcours des nombres de 0 à 2 500 000 (et non 10 000 000 car le 'n' ne peut avoir que 7 chiffres et 4*2 500 000 à 8 chiffres)
for i in range (2500000):
    # Si le miroir de 'n' est egale à 4 x 'n'
    if inverse(i)==4*i:
        number=i

# A la fin, on affiche la reponse
print("{}".format(number))