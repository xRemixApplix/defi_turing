#-*- coding: utf8 -*-

"""
    Module regroupant toutes les fonctions utilisées dans le défi de turing
"""

def miroir(n):
    """
        Fonction retournant le nombre miroir du nombre donné en parametre

        Ex.: miroir(13456) retourne 65431
    """
    # Initialisation d'une liste vide
    list = []
    # Parcours de la chaine de caractere
    for char in str(n):
        # On met chaque caractère de la chaine dans une liste
        list.append(char)
    # Inversion de la liste
    list.reverse()
    # On retourne la chaine transformer en entier
    return int("".join(list))