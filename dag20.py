# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()

f = open("input.txt", "r")
numbers=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    numbers.append(int(line))
f.close()

i=0
offset=0
insert_index=np.array([])
remove_index=np.array([])
numbers_org=list(numbers)
numbers_changed=list()
while i<len(numbers):

    offset=-np.sum(remove_index<=i)+np.sum(insert_index<=i)
    
    old_index=i+offset
    movenumber=numbers[old_index]
    
    new_index=(i+offset+movenumber)
    if new_index<=0: new_index-=1
    if new_index>len(numbers): new_index+=1
    
    new_index=new_index%len(numbers)

    numbers_changed.append(movenumber)
    del numbers[old_index]
    numbers.insert(new_index,movenumber)
    
    insert_index=np.append(insert_index,new_index)
    remove_index=np.append(remove_index,old_index)

    i+=1
    
ind=numbers.index(0)
print("Part 1",numbers[(ind+1000)%len(numbers)]+numbers[(ind+2000)%len(numbers)]+numbers[(ind+3000)%len(numbers)])
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))