# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
new_data=[0,0,0,0,0,0]
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    
    if i%4==0 or i%4==1 or i%4==2:
        #print(line)
        [A,B]=[int(d) for d in re.findall(r'\d+',line)]
        new_data[i%4*2]=A
        new_data[i%4*2+1]=B
    if i%4==3:
        data.append(new_data)
        new_data=[0,0,0,0,0,0]
f.close()
data.append(new_data)

cost_1=0
for game in data:
    
    #Twee vergelijkingen met twee onbekendes:
    #game[4]=A*game[0]+B*game[2]
    #game[5]=A*game[1]+B*game[3] 
    ##################
    #A=(game[4]-B*game[2])/game[0]
    #game[5]=((game[4]-B*game[2])/game[0])*game[1]+B*game[3]
    #game[5]/game[1]=((game[4]-B*game[2])/game[0])+B*game[3]/game[1]
    #game[5]/game[1]*game[0]=(game[4]-B*game[2])+B*game[3]/game[1]*game[0]
    #game[5]/game[1]*game[0]-game[4]=-B*game[2])+B*game[3]/game[1]*game[0]
    #game[5]/game[1]*game[0]-game[4]=B*(game[3]/game[1]*game[0]-game[2])   
    B=(game[5]/game[1]*game[0]-game[4])/(game[3]/game[1]*game[0]-game[2])
    A=(game[4]-B*game[2])/game[0]

    #Net niet gehele getallen even fixen
    err=0.001
    if (A<round(A)+err and A>round(A)-err and B<round(B)+err and B>round(B)-err)==False: #Als geen geheel aantal A of B
        continue
    
    #Max 100 drukken en meer dan 0 natuurlijk
    if A<=100 and A>0 and B>0 and B<=100:
        cost_1+=int(A*3+B)

cost_2=0
for game in data:
    game[4]=game[4]+10000000000000
    game[5]=game[5]+10000000000000

    B=(game[5]/game[1]*game[0]-game[4])/(game[3]/game[1]*game[0]-game[2])
    A=(game[4]-B*game[2])/game[0]
    
    err=0.001
    if (A<round(A)+err and A>round(A)-err and B<round(B)+err and B>round(B)-err)==False: #Als geen geheel aantal A of B
        continue
    
    A=int(round(A))
    B=int(round(B))
    
    #Meer dan 0 drukken is ook handig
    if A>0 and B>0:
        cost_2+=int(A*3+B)

print("Part 1",cost_1)
print("Part 2",cost_2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))