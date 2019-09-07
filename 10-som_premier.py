
#version python 3.4 
# -*- coding: utf-8 -*- 
import math
import time

# Initialisation des variables
n=10000000
premiers=[True]*n # A priori tous premiers au départ
premiers[0]=False # 0 n'est pas premier 
premiers[1]=False # 1 non plus 
racine=math.sqrt(n) # La borne pour les tests (enregistré pour éviter de refaire le calcul à chaque tour de boucle)
somme = 0
 
# La fonction qui dit pour chaque element de la iste s'il est un nombre premier ou non
def eratosthene (): 
    i=2 
    while i <= racine: 
        k=2 
        h=(n-1)/i
        while k<=h: 
            premiers[k*i]=False 
            k+=1 
        # Après i=2 ou 3, il n'y a plus de nombre premier consecutif
        if i<3:
            j=i+1
        else:
            j=i+2 
        # Si premiers[j] deja egal à False alors on passe à l'index suivant afin d'eviter des tours de boucles inutiles
        while not premiers[j]: 
            j+=1 
        i=j 
 

eratosthene()
for i in range(0,n):
    if premiers[i]:
        somme += i

print(somme)
