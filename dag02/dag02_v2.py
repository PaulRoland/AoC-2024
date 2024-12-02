# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def asc_desc_continously(numbers):    
    asc={1,2,3} #Continously ascending with these steps
    desc={-1,-2,-3} #Continously descending
    
    diffs=[a-b for a,b in zip(numbers[1:],numbers[:-1])]
    
    #continuous and with right stepsize if the set of diffences is a subset of either asc or desc 
    if set(diffs)<=asc or set(diffs)<=desc:
        return 1
    return 0


def safe2(numbers):
    #Probeer nu met elk afzonderlijk nummer missend
    for j in range(0,len(numbers)):
        if asc_desc_continously(numbers[:j]+numbers[j+1:])==1:
            return 1
    return 0
                    
total_1=0
total_2=0          
  
f = open("input.txt", "r")
for line in f:
    report=[int(d) for d in line.split(' ')]
    total_1+=asc_desc_continously(report)
    total_2+=safe2(report)
f.close()

print("Part 1",total_1)
print("Part 2",total_2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
