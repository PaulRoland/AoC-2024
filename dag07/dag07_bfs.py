# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def bfs_input1(test_value,numbers,start_index):
    #heap  [cur_value,cur_index]
    heap = [[numbers[start_index],start_index]]
    i = 0
    
    while i<len(heap):
        [value,ind] = heap[i]
        i+=1
        #Als deze waarde klopt en we zijn op het eind
        if value == test_value and ind == len(numbers)-1:
            return value
        
        #Ga door met het volgende item, deze kan het niet meer worden
        if ind == len(numbers)-1 or value>test_value: 
            continue
        
        #Gooi nieuwe opties op de hoop
        heap.append([value+numbers[ind+1],ind+1])
        heap.append([value*numbers[ind+1],ind+1])        
    return 0


def bfs_input2(test_value,numbers,start_index):
    heap = [[numbers[start_index],start_index]]
    i = 0
    while i<len(heap):
        [value,ind] = heap[i]
        i+=1
        if value > test_value:
            continue
        if ind == len(numbers)-1:
            if value == test_value:
                return value
            continue

        heap.append([value+numbers[ind+1],ind+1])
        heap.append([value*numbers[ind+1],ind+1])      
        heap.append([int(str(value)+str(numbers[ind+1])),ind+1]) 
    return 0


f = open("input.txt", "r")
inputs=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','').replace(':','')
    numbers=[int(d) for d in line.split(' ')]
    inputs.append(numbers)
f.close()

total_1=0
total_concats=0
for numbers in inputs:
    part1=bfs_input1(numbers[0],numbers,1)
    total_1+=part1
    
    if part1 == 0:#Probeer ook nog met concats
        total_concats+=bfs_input2(numbers[0],numbers,1)


print("Part 1",total_1)
print("Part 2",total_1+total_concats)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
