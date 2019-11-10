#-*- coding: utf8 -*-

sept_dgt = []
huit_dgt = []

sept = huit = 2
sept_bis = huit_bis = False

somme = 0

while sept <= 2013 :
    sept_dgt.append(sept)
    sept_bis = not sept_bis

    if sept_bis :
        sept += 10
    else :
        sept += 2

while huit <= 2013 :
    huit_dgt.append(huit)
    huit_bis = not huit_bis

    if huit_bis :
        huit += 12
    else :
        huit += 2

for elt in sept_dgt :
    if elt in huit_dgt :
        somme += elt

print(somme)