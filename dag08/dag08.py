# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import itertools as it
import time
import math
start_time = time.time_ns()

f = open("input.txt", "r")
max_r=0
max_c=0
#Maak een lijst van alle antennas, per frequentie
antennas=[ [] for d in range(0,200)]
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s!='.':
            antennas[ord(s)].append([row,col])
max_r=row+1
max_c=col+1  
f.close()

antinodes1=list()
for freq in antennas:
    if len(freq)<=1:
        continue
    
    #Gebruik elke combinatie van twee antennas
    for (ant_a,ant_b) in it.combinations(freq,2):
        
        drow = ant_b[0]-ant_a[0]
        dcol = ant_b[1]-ant_a[1]
        
        node_1 = [ant_a[0]-drow,ant_a[1]-dcol]
        node_2 = [ant_b[0]+drow,ant_b[1]+dcol]
        
        #Probeer een antinode aan weerzijde te plaatsen op dezelfde afstand als a en b hebben van elkaar
        if node_1[0]>=0 and node_1[0]<max_r and node_1[1]>=0 and node_1[1]<max_c:
            antinodes1.append(str(node_1[0])+'_'+str(node_1[1]))
        if node_2[0]>=0 and node_2[0]<max_r and node_2[1]>=0 and node_2[1]<max_c:
            antinodes1.append(str(node_2[0])+'_'+str(node_2[1]))

antinodes2=list()
for freq in antennas:
    if len(freq)<=1:
        continue
    
    for (ant_a,ant_b) in it.combinations(freq,2):
        drow = ant_b[0]-ant_a[0]
        dcol = ant_b[1]-ant_a[1]
        
        #Vind alle stappen direct exact in lijn met a,b. Gebruik largest common divisor hiervoor
        row_step=int(drow/math.gcd(drow,dcol))
        col_step=int(dcol/math.gcd(drow,dcol))
        
        for n in range(-max_r,max_r):
            test_r=ant_a[0]+n*row_step
            test_c=ant_a[1]+n*col_step
            
            if test_r>=0 and test_r<max_r and test_c>=0 and test_c<max_c:
                antinodes2.append(str(test_r)+'_'+str(test_c))
        
print("Part 1",len(set(antinodes1)))
print("Part 2",len(set(antinodes2)))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
