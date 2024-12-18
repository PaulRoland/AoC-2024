# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()

f = open("input.txt", "r")
grid = np.zeros((71,71))
max_byte=1024

fall_byte=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [r,c]=[int(d) for d in line.split(',')]
    
    fall_byte.append([r,c])    
f.close()


offset=0


forward=True
refinement=[500,100,20,5,1]
ri=0

while True:
    grid = np.zeros((71,71))
    for [r,c] in fall_byte[:max_byte+offset]:    
        grid[r,c]=1
    #Start soling
    start_r=0
    start_c=0
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    
    heap=list()
    heap.append([start_r,start_c,0])
    grid_visited=np.zeros((71,71))
    minscores=np.ones((71,71))*9999
    i=0
    while i<len(heap):
        cr=heap[i][0]
        cc=heap[i][1]
        cur_score=heap[i][2]
    
        while True:
            options=list()
            for dirs in directions:
                if cr+dirs[0]<0 or cr+dirs[0]>70 or cc+dirs[1]<0  or cc+dirs[1]>70:
                    continue
                if grid[cr+dirs[0],cc+dirs[1]]==0:
                    options.append(dirs)
            
            #print(options)
            if cur_score>minscores[cr,cc]:
                break
            minscores[cr,cc]=cur_score
            
            #Een optie
            if len(options)==0:
                break
                #loopt dood
                
            if len(options)==1: #een optie
                    cr+=options[0][0]
                    cc+=options[0][1]
                    
            elif len(options)>1: #meere opties

                if grid_visited[cr,cc]==0:
                    grid_visited[cr,cc]=1
                    for dirs in options:
                            heap.append([cr+dirs[0],cc+dirs[1],cur_score+1])

                break
            #Next element in heap    
        i+=1

    # Offset 0 is part 1
    if offset==0:
        print("Part 1",int(minscores[70,70]))
    
    ####Daarna een methode om met steeds kleinere stappen heen en weer te zoeken om snel het goede getal te vinden
    if ri==len(refinement)-1 and minscores[70,70]==9999:
        last_rc=str(r)+','+str(c)
        print("Part 2",last_rc)
        break
    
    if ri==len(refinement)-1 and minscores[70,70]<9999:
        forward=True
    
    if forward==True and minscores[70,70]==9999:
        print("Tried",max_byte+offset,"Changing search direction")
        ri+=1
        forward=False
  
    if forward==False and minscores[70,70]<9999:
        print("Tried",max_byte+offset,"Changing search direction")
        ri+=1
        forward=True

    
    if forward==True:
        offset+=refinement[ri]
    else:
        offset-=refinement[ri]
       


print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))