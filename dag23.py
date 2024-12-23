# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import itertools as it
 
f = open("input.txt", "r")
graph=dict()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [a,b]=line.split('-')
    if a in graph:
        graph[a].append(b)
    else:
        graph.update({a:[b]})
    if b in graph:
        graph[b].append(a)
    else:
        graph.update({b:[a]})
f.close()


### Part 1
sets=dict()
#sets of three computers
for key in graph:
    for element in it.combinations(graph[key],2):
        items=[key]
        items.extend(element)
        items.sort()
        
        key2 = ','.join(items)
    
        if key2 in sets:
            sets[key2]+=1
        else:
            sets.update({key2:1})
    
total_p1=0
for key in sets:
    if sets[key]==3 and (key[0]=='t' or key[3]=='t' or key[6]=='t'):
        total_p1+=1


### Part 2            
for offset in range(0,3):
    sets=dict()
    for key in graph:
        for element in it.combinations(graph[key],13-offset):
            items=[key]
            items.extend(element)
            items.sort()
            
            key2 = ','.join(items)
        
            if key2 in sets:
                sets[key2]+=1
            else:
                sets.update({key2:1})
    v = list(sets.values())
    if max(v) == 13-offset+1:
        k = list(sets.keys())
        total_p2=k[v.index(max(v))]
        break
        

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))