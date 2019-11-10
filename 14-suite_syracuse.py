#-*- coding: utf8 -*-

def suite_syracuse(numb) :
    if numb%2 == 0 :
        return numb/2
    else :
        return (numb*3)+1

solution = 0
lng_solution = 0

for i in range(1, 1500000) :
    lng = 1
    numb = i

    while numb>1 :
        numb = suite_syracuse(numb)
        lng += 1

    if lng_solution<lng :
        solution = i
        lng_solution = lng

    print("{} : {}".format(i, lng))

print("\nSolution : {}".format(solution))