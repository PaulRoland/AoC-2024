# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")

def check_word(start_x,start_y,search):
    directions = [[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0]]
    found_count=0
    for direc in directions:
        x=start_x
        y=start_y
        found = True

        for step in range(1,len(search)):
            x+=direc[1]
            y+=direc[0]
            
            if x<0 or x>=len(data[0]):
                found=False
                break;
            if y<0 or y>=len(data):
                found=False
                break;
            
            if data[y][x]!=search[step]:
                found=False
                break;
                
        if found == True:
            found_count+=1
    return found_count


def check_x(start_x,start_y,search):
    if start_x==0 or start_y==0 or start_x==len(data[0])-1 or start_y==len(data)-1:
        return 0
    
    str1=data[start_y+1][start_x+1]+data[start_y][start_x]+data[start_y-1][start_x-1]
    str2=data[start_y+1][start_x-1]+data[start_y][start_x]+data[start_y-1][start_x+1]
    
    if (str1==search or str1[::-1]==search) and (str2==search or str2[::-1]==search):
        return 1
    return 0


start_x=list()
start_y=list()
start_a_x=list()
start_a_y=list()
data=list()

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for j,s in enumerate(line):
        if s=='X':
            start_x.append(j)
            start_y.append(i)
        if s=='A':
            start_a_x.append(j)
            start_a_y.append(i)
    data.append(line)
f.close()

total1=0
for x,y in zip(start_x,start_y):
    total1+= check_word(x,y,'XMAS')

total2=0
for x,y in zip(start_a_x,start_a_y):
    total2+= check_x(x,y,'MAS')
    

print("Part 1",total1)
print("Part 2",total2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
