# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
start_time = time.time_ns()
import numpy as np
f =open("input.txt")
data=list()

for row,line in enumerate(f):
    line=line.replace('\n','')
    for col,s in enumerate(line):
        if s=='S':
            start_row=row
            start_col=col
        if s=='E':
            end_row=row
            end_col=col
    line=line.replace('E','.')
    line=line.replace('S','.')
    data.append(line)
    
directions = [[0,1],[1,0],[0,-1],[-1,0]]

running=True

cur_dir=[0,1]

minscores=np.ones((len(data),len(data[0])))*9999999

heap=list()
heap.append([start_row,start_col,0,cur_dir])
i=0

while i<len(heap):
    cr=heap[i][0]
    cc=heap[i][1]
    cur_score=heap[i][2]
    cur_dir=heap[i][3]
    #print(i)
    #print(cr,cc,cur_score,cur_dir)
    while True:
    #Kijk niet achterom
        exclude_dir=[cur_dir[0]*-1,cur_dir[1]*-1]
        #print(exclude_dir)
        options=list()
        for dirs in directions:
            if dirs==exclude_dir:
                #Teruggaan is geen optie
                continue
            if data[cr+dirs[0]][cc+dirs[1]]=='.':
                options.append(dirs)
        #print(cr,cc,"options",options)
        
        if cur_score>minscores[cr][cc]:
            break
        minscores[cr][cc]=cur_score
        #Een optie
        if len(options)==0:
            break
            #loopt dood
            
        if len(options)==1:
            
            #Ene optie is rechtdoor
            if options[0]==cur_dir:
                cr+=options[0][0]
                cc+=options[0][1]
                cur_score+=1
            else: #Ene optie is een bocht om
                cur_dir=options[0]
                cur_score+=1001
                cr+=options[0][0]
                cc+=options[0][1]
                
                #Meerdere opties op dit punt
        elif len(options)>=2:
            #print(cur_score,cr,cc,options)
            
            for dirs in options:
                if dirs!=cur_dir:
                    heap.append([cr+dirs[0],cc+dirs[1],cur_score+1001,dirs])
                if dirs==cur_dir:
                    heap.append([cr+dirs[0],cc+dirs[1],cur_score+1,dirs])
                    
            break
        #Next element in heap    
    i+=1
    
#backtrack
cr=end_row
cc=end_col
prev=minscores[end_row,end_col]+1
path=list()

heap=list()
heap.append([cr,cc,prev])

nodes_visited=list()
i=0
while i<len(heap):
    cr=heap[i][0]
    cc=heap[i][1]
    prev=heap[i][2]
    i+=1
    while True:
        cur_score=minscores[cr,cc]

        options=list()
        key=str(cr)+'_'+str(cc)
        path.append([cr,cc])
        if key in nodes_visited:
            break
        
        for dirs in directions:
            if minscores[cr+dirs[0],cc+dirs[1]]==prev-2 or minscores[cr+dirs[0],cc+dirs[1]]==prev-1002 or minscores[cr+dirs[0],cc+dirs[1]]==cur_score-1:
                options.append(dirs)
            #Dit is een obscure edge case
            elif minscores[cr+dirs[0],cc+dirs[1]]<cur_score: #score is wel kleiner, maar niet met de goede afwijking. Kan zijn dat er een splitsing tussen invalt met een lagere score die het verpest
                if minscores[cr+dirs[0]*2,cc+dirs[1]*2]==cur_score-2:
                    path.append([cr+dirs[0],cc+dirs[1]])
                    key=str(cr+dirs[0])+'_'+str(cc+dirs[1])
                    nodes_visited.append(key)
                    heap.append([cr+dirs[0]*2,cc+dirs[1]*2,cur_score-1])
                    
        if len(options)==1:
            cr=cr+options[0][0]
            cc=cc+options[0][1]
            prev=cur_score
            path.append([cr,cc])
        else:
            
            key=str(cr)+'_'+str(cc)
            #print(key,options,prev)
            nodes_visited.append(key)
            for dirs in options:
                heap.append([cr+dirs[0],cc+dirs[1],cur_score])

            
        if cr==start_row and cc==start_col:
            break
minscores2=np.ones((len(data),len(data[0])))
path2=list()
for loc in path:
    minscores2[loc[0],loc[1]]=0
    path2.append(str(loc[0])+'_'+str(loc[1]))
    
print("Part 1",int(minscores[end_row,end_col]))
print("Part 2",len(set(path2)))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
        
        
        