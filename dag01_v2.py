# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
start_time = time.time_ns()

f = open("input.txt", "r")
left_list=list()
right_list=list()
count_list=[0] * 99999
for line in f:
    numbers=[int(d) for d in line.split('   ')]
    left_list.append(numbers[0])
    right_list.append(numbers[1])
    count_list[numbers[1]]=count_list[numbers[1]]+1
f.close()


distance=0
similarity=0

#Vergelijk laagste links met laagste rechts etc
left_list.sort()
right_list.sort()
for left,right in zip(left_list,right_list):
    distance+=abs(left-right)
    similarity+=left*count_list[left]  

print("Part 1: ",distance)
print("Part 2: ",similarity)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))