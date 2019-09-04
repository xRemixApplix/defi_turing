#-*- coding: utf8 -*-

# Fonction qui decompose le nombre en parametre en suite de multiplication de nombre premier sous forme de liste
def decompose(n) :
    # Initialisation d'une liste vide
    list_facteur = []
    # On débute la verification à partir de 2 (1 n'étant pas un nombre premier)
    d=2
    # On teste la divisibilite du nombre par 2, puis son quotiant jusqu'a obtenir un nombre impair
    while n%d==0:
        list_facteur.append(d)
        q=n//d
        n=q
    # On fait de même avec 3, puis avec tout les nombres impairs (de 2 en 2)
    d=3
    while d<=n:
        while n%d==0:
            list_facteur.append(d)
            q=n//d
            n=q
        d += 2
    # Retourne la liste de nombre premier
    return list_facteur

# Fonction qui extrait le plus grand nombre d'une liste
def plus_grand_nombre(list):
    return max(list)

print("{}".format(plus_grand_nombre(decompose(20130101))))