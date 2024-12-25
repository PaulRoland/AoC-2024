# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
n=-1
images=list()
for i,line in enumerate(f):
    if line=='\n':
        continue
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    
    if i%8==0:
        n+=1
        images.append([])
    images[n].append(line)
        
    print(line)
        
f.close()

locks=list()
keys=list()
nk=-1
nl=-1
#Locks
for image in images:
    if set(image[0])!={'#'}:
        continue
    
    lock=[0,0,0,0,0]
    for row,line in enumerate(image):
        for col,s in enumerate(line):
            if s=='#':
                lock[col]=row
    locks.append(lock)
        
#Keys
for image in images:
    if set(image[0])!={'.'}:
        continue
    
    key=[0,0,0,0,0]
    for row,line in enumerate(image[::-1]):
        for col,s in enumerate(line):
            if s=='#':
                key[col]=row
    keys.append(key)

pairs=0
for lock in locks:
    for key in keys:    
        overlap=False
        for c,[k,l] in enumerate(zip(key,lock)):
            
            if k>=(6-l):
                print("lock",lock,"and key",key,"overlap at",c+1)
                overlap=True
                break
        
        if overlap==False:
            pairs+=1
        
     
        



print("Part 1",pairs)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))