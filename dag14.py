# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()
import matplotlib.pyplot as plt
import statistics as stat

nrow=103
ncol=101

bots=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data=[int(d) for d in re.findall(r'[-]?\d+',line)]
    #print(data)
    bots.append([data[1],data[0],data[3],data[2],data[1],data[0]]) #row, col, vrow, vcol,start rowcol   
f.close()

for bot in bots:
    bot[0]=(bot[4]+(bot[2]*100))%nrow
    bot[1]=(bot[5]+(bot[3]*100))%ncol
        
#Count
q1=q2=q3=q4=0
for bot in bots:
    if bot[0]<(nrow-1)/2:
        if bot[1]<(ncol-1)/2: q1+=1
        if bot[1]>(ncol-1)/2: q3+=1
    if bot[0]>(nrow-1)/2:
        if bot[1]>(ncol-1)/2: q2+=1
        if bot[1]<(ncol-1)/2: q4+=1
total_p1=q1*q2*q3*q4
print("Part 1",total_p1)


#Er zit af en toe een horizontale balk in alle locaties en af en toe een
#verticale balk in de data.
#Deze balken repereren en vallen op een bepaald moment samen.

balk1=list()
balk2=list()

for i in range(0,200):
    for bot in bots:
        bot[0]=(bot[4]+(bot[2]*i))%nrow
        bot[1]=(bot[5]+(bot[3]*i))%ncol
            
    print_plaatje=False
    #Balk is te vinden door de opvallende kleine spreiding in row of col
    #spreidin in de hoogte en breedte
    std_b=stat.stdev([bot[0] for bot in bots])
    std_h=stat.stdev([bot[1] for bot in bots])
    #print(i,std_b,std_h)
    if std_b<22: #Relatief kleine spreiding in deze richting
        balk1.append(i)
        print_plaatje=True
    if std_h<22: #Relatief kleine spreiding in deze richting
        balk2.append(i)
        print_plaatje=True
    
    #Laat plaatje zien als er een balk gevonden ins    
    #if print_plaatje==True:
    #    plt.figure(figsize=[6,6])
    #    plt.scatter([bot[0] for bot in bots],[bot[1] for bot in bots])
    #    plt.title(str(i))
    #    plt.show()
        
#print('Patroon balk 1:',balk1[0],'+ n1 *',balk1[1])
#print('Patroon balk 2:',balk2[0],'+ n2 *',balk2[1])

#Er is vast een betere manier om n1 en n2 te vinden en dus het goede aantal seconde, maargoed
i=0
offset1 = balk1[0]
offset2 = balk2[0]
delta1=balk1[1]-balk1[0]
delta2=balk2[1]-balk2[0]
while True:
    i+=1
    if (i-offset1)%delta1==0 and (i-offset2)%delta2==0:
        total_p2=i
        break    
#print('Valt samen op',total_p2)

#Teken eindoplossing

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
imagen=total_p2
for bot in bots:
    bot[0]=(bot[4]+(bot[2]*imagen))%nrow
    bot[1]=(bot[5]+(bot[3]*imagen))%ncol  
plt.figure(figsize=[6,6])
plt.scatter([bot[0] for bot in bots],[bot[1] for bot in bots])
plt.title(str(imagen))
plt.show()