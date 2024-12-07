# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def test_input(test_value,ind,cur,nms,has_concat):
    if ind==len(nms):
        if cur==test_value:
            options_list.append([cur,has_concat])
        return
    
    #Break het zoeken af, als de huidige waarde al te hoog is
    if cur>test_value:
        return
    #Open nieuwe opties
    # + spoor
    test_input(test_value,ind+1,cur+nms[ind],nms,has_concat)    
    # * spoor
    test_input(test_value,ind+1,cur*nms[ind],nms,has_concat)
    # concat spoor
    test_input(test_value,ind+1,int(str(cur)+str(nms[ind])),nms,1)
    
    return

f = open("input.txt", "r")
inputs=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','').replace(':','')
    numbers=[int(d) for d in line.split(' ')]
    inputs.append(numbers)
f.close()


total_1=0
total_2=0
for numbers in inputs:
    options_list=list()
    test_input(numbers[0],2,numbers[1],numbers,0)
    if len(options_list)>0:
        total_2+=numbers[0]

        for elem in options_list:
            if elem[1] == 0: #No concat was used so it fits part 1    
                total_1+=numbers[0]
                break

print("Part 1",total_1)
print("Part 2",total_2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
