#-*- coding: utf8 -*-

list_annee = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ecart = 0

def annee_chiffres_diff(annee) :
    a_ajouter = True

    annee_str = str(annee)

    for i in range(0, len(annee_str)-1) :
        for j in range (i+1, len(annee_str)) :
            if annee_str[i] == annee_str[j] :
                a_ajouter = False

    return a_ajouter


for nb in range(1, 2014) :
    if len(str(nb)) > 1 :
        if annee_chiffres_diff(nb) :
            list_annee.append(nb)

for i in range(0, len((list_annee))-1) :
    if list_annee[i+1] - list_annee[i] > ecart :
        ecart = list_annee[i+1] - list_annee[i]


print(len(list_annee)*ecart)