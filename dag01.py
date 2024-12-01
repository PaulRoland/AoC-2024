# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
start_time = time.time_ns()



f = open("test.txt", "r")
left_list=list()
right_list=list()
for i,line in enumerate(f):

    [left,right]=line.split('   ')

    #maak een linkerlijst en rechterlijst van getallen
    left_list.append(int(left))
    right_list.append(int(right))
f.close()

#sorteer de twee lijsten, hierdoor matchen laagste, eennalaagste getallen etc. met elkaar
left_list.sort()
right_list.sort()

distance1=0
distance2=0
for left,right in zip(left_list,right_list):
    #Tel de afstanden tussen de nummers bij elkaar op
    distance1+=abs(left-right)
    
    #Tel hoevaak het huidige item voorkomt in de hele rechter lijst
    #Bereken similarity score
    distance2+=left*right_list.count(left)     


print("Part 1",distance1)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
print("Part 2",distance2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))