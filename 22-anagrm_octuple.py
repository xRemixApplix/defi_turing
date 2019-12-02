#-*- coding: utf8 -*-

for nb1 in range(100000, 999999//8) :
    for nb2 in range(nb1+1, 999999//8) :
        if sorted(str(nb1))==sorted(str(nb1*8)) and sorted(str(nb2))==sorted(str(nb2*8)) and sorted(str(nb1*8))==sorted(str(nb2*8)):
            print("Trouve",nb1+nb2)
