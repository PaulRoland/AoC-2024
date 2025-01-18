# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def blink_stone(stone,cur_blink,end):
    key=str(stone)+','+str(end-cur_blink)
    
    if key in stone_mem:
        return stone_mem[key]
    
    if cur_blink==end:
        return 1
    
    total = 0
    if stone==0:
        total = blink_stone(1,cur_blink+1,end)
    elif stone==1:
        total = blink_stone(2024,cur_blink+1,end)
    elif len(str(stone))%2==0:
        total += blink_stone(int(str(stone)[:len(str(stone))//2]),cur_blink+1,end)
        total += blink_stone(int(str(stone)[len(str(stone))//2:]),cur_blink+1,end)
    else:
        total = blink_stone(stone*2024,cur_blink+1,end)
    
    stone_mem.update({key:total})
    return total
            
    
f = open("input.txt", "r")
for i,line in enumerate(f):
    stones=[int(d) for d in line.split(' ')]
    
f.close()
total_p1=0
total_p2=0
stone_mem=dict()
for stone in stones:
    total_p1+=blink_stone(stone,0,25)   
    total_p2+=blink_stone(stone,0,75)



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))