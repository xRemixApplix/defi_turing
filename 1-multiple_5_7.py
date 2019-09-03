# -*- coding: utf8 -*-

# Variables d'initialisation du programme
somme = 0

# Pour chaque valeur inférieure a l'echelle haute du probleme
for i in range(2013) :
    # Si la division par 5 ou 7 n'a pas de reste
    if i%5==0 or i%7==0 :
        # Ajout de la valeur courante à la somme globale
        somme += i

    #### CODE A RAJOUTER POUR DEBUGGER ####
        #print("DEBUG : {}->Oui".format(i))
    #else :
        #print("DEBUG : {}->Non".format(i))
    #######################################

# Affichage de la reponse
print("Réponse : {}".format(somme))