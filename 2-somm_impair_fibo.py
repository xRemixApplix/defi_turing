# -*- coding: utf8 -*-

# Variables d'initialisation du programme
somme = 2
i = prec = 1

# Tant que la valeur courante de la suite de Fibonacci est inférieure à la borne haute du programme
while i <= 4000000 :
    # Calcul nouvelle valeur courante de la suite de Fibonacci
    fibo_numb = i + prec
    # Si la novuelle valeur courante est impair et inférieure à la borne haute du programme
    if fibo_numb%2 != 0 and fibo_numb<4000000:
        # Ajout de la valeur courante à la somme globale
        somme += fibo_numb
    
    #### CODE A RAJOUTER POUR DEBUGGER ####
    # print("DEBUG : {}".format(fibo_numb))
    #######################################

    # Mise a jour des valeurs
    prec,i = i,fibo_numb


# Affichage de la reponse
print("Réponse : {}".format(somme))