# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def safe(numbers):  
    if numbers[1]>=numbers[0]: #controleer ascending
        for a,b in zip(numbers[:-1],numbers[1:]): #vergelijk opeenvolgende nummers
            if b-a<1 or b-a>3:  #verschil moet tussen 1 en 3 zijn
                return 0
            
    elif numbers[1]<numbers[0]: #controleer descending
        for a,b in zip(numbers[:-1],numbers[1:]): #vergelijk opeenvolgende nummers
            if a-b<1 or a-b>3:  #verschil moet tussen 1 en 3 zijn
                return 0
    return 1


def safe2(numbers):
    if safe(numbers)==1:
        return 1
    
    #Onveilig report? probeer nu met elk afzonderlijk nummer missend
    for j in range(1,len(numbers)+1):
        print(j)
        print(numbers[:j-1]+numbers[j:])
        if safe(numbers[:j-1]+numbers[j:])==1:
            return 1
    return 0
                    
            
f = open("input.txt", "r")
t_safe=0
t_safe2=0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    reports=[int(d) for d in  line.split(' ')]
    
    t_safe+=safe(reports)
    t_safe2+=safe2(reports)
    
f.close()

print("Part 1",t_safe)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
print("Part 2",t_safe2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))