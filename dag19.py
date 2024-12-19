# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def find_design(towel,pos):
    global possible
    if possible==True: #afbreken zodra er een possible gevonden is
        return    
    
    if pos==len(towel):
        possible=True
        return
      
    for i in range(1,9):
        if pos+i>len(towel):
            break
        if towel[pos:pos+i] in designs:
            find_design(towel,pos+i)

permutations=dict()
def find_permutations(towel,pos):
    if pos==len(towel): #Aan het einde, dus dit is een optie
        return 1
    
    #Kijk of we ons geheugen kunnen gebruiken
    key=str(towel[pos:])
    if key in permutations:
        return permutations[key]
    
    #Open nieuwe opties, als er geen mogelijk is dan komt er mooi 0 uit.
    perms=0
    for i in range(1,9):
        if pos+i<=len(towel):
            if towel[pos:pos+i] in designs:
                perms+=find_permutations(towel,pos+i) #Som van alle komende opties

    #Klaar met de vertakkingen, schrijf het aantal gevonden opties weg om later snel te gebruiken
    permutations.update({key:perms})
    return perms
                
            
f = open("input.txt", "r")
designs=f.readline().replace('\n','').split(', ')

towels=list()
for i,line in enumerate(f):
    if line!='\n': 
        towels.append(line.replace('\n',''))
f.close()

total_p1=0
total_p2=0
for towel in towels:
    possible=False
    find_design(towel,0)
    if possible==True:
        total_p1+=1
        total_p2+=find_permutations(towel,0)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))