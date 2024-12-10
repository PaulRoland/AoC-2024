# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
PWFI YFRP, ZIK XVNVC% KTW GOXA MMQEMOTH
@author: Paul
"""

from collections import deque
import time
start_time = time.time_ns()

f = open("input.txt", "r")

tmap=list()
start_keys=list()
end_keys=list()

#Load data
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if int(s)==0:
            key=str(row)+'_'+str(col)
            start_keys.append(key)
        if int(s)==9:
            key=str(row)+'_'+str(col)
            end_keys.append(key)
    tmap.append(line)   
f.close()

#create a graph from the data
graph=dict()
nrow=len(tmap)
ncol=len(tmap[0])
for row,line in enumerate(tmap):
    for col,v in enumerate(line):
        
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        for direc in dirs:
            if row+direc[0]>=nrow or row+direc[0]<0 or col+direc[1]>=ncol or col+direc[1]<0:
                continue
            
            if int(tmap[row+direc[0]][col+direc[1]])-int(v)==1: #Look up difference of exactly one
                key=str(row)+'_'+str(col)
                new_key=str(row+direc[0])+'_'+str(col+direc[1])
                if key in graph:
                    graph[key].append(new_key)
                else:
                    graph.update({key:[new_key]})

###Count the trailheads for p1 and p2. 
trail_heads1=0
trail_heads2=0
#Start at start_keys and maybe end at end_keys
for start in start_keys:
    heap=deque([start])
    end_visited=list()
    while heap:
        search_key=heap.popleft()
        
        #Als dit een einde is, is dit een oplossing voor p2
        if search_key in end_keys:
            trail_heads2+=1
            #En als we er nog niet eerder zijn geweest voor p1
            if search_key not in end_visited:
                end_visited.append(search_key)
                trail_heads1+=1
            continue
        #Niet bij het einde open nieuwe paden
        if search_key in graph:
            for new_key in graph[search_key]:
                heap.append(new_key)

print("Part 1",trail_heads1)
print("Part 2",trail_heads2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))