# -*- coding: utf8 -*-

# Affichage de la reponse
print("Réponse : {}".format(sum(i for i in range(2013) if not i%5 or not i%7)))