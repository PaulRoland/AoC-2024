# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def walk(grid,start_row,start_col):
    dirs=[[-1,0],[0,1],[1,0],[0,-1]]
    curdir=0
    
    row=start_row
    col=start_col
    
    step_list=list()
    step_list.append(str(row)+'_'+str(col))
    stepdir_list=list()
    stepdir_list.append(str(row)+'_'+str(col)+'_'+str(curdir%4))
    
    while row!=0 and col!=0 and row!=len(data)-1 and col!=len(data[0])-1:

        if data[row+dirs[curdir%4][0]][col+dirs[curdir%4][1]] != '#':
            row=row+dirs[curdir%4][0]
            col=col+dirs[curdir%4][1]
            
            step_list.append(str(row)+'_'+str(col))           
            stepdir_list.append(str(row)+'_'+str(col)+'_'+str(curdir%4))
        else:
            curdir+=1
            stepdir_list.append(str(row)+'_'+str(col)+'_'+str(curdir%4))
    return [len(set(step_list)),stepdir_list]


def walk_hasloop(grid,start_row,start_col):
    dirs=[[-1,0],[0,1],[1,0],[0,-1]]
    curdir=0 #up
    row=start_row
    col=start_col

    stepdir_list=list()
    
    while row!=0 and col!=0 and row!=len(grid)-1 and col!=len(grid[0])-1:

        if grid[row+dirs[curdir%4][0]][col+dirs[curdir%4][1]] != '#':
            row=row+dirs[curdir%4][0]
            col=col+dirs[curdir%4][1]
            
            if str(row)+'_'+str(col)+'_'+str(curdir%4) in stepdir_list:
                #we zitten in een loop
                return 1   
            stepdir_list.append(str(row)+'_'+str(col)+'_'+str(curdir%4))
        else:
            #turn right
            curdir+=1
            if str(row)+'_'+str(col)+'_'+str(curdir%4) in stepdir_list:
                #we zitten in een loop
                return 1  
            stepdir_list.append(str(row)+'_'+str(col)+'_'+str(curdir%4))
    return 0

data=list()
f = open("input.txt", "r")
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s=='^':
            start_row=row
            start_col=col

    data.append(line)
    print(line)
f.close()

[total_1,steps]=walk(data,start_row,start_col)
print("Part 1",total_1)

#steps has all locations
#plaatst een object 1 vooruit en check of het een loop is
blocks=0
block_list=list()

#for i,optie in enumerate(steps[:-1]):
for block_r in range(0,len(data)):
    #print(block_r)
    for block_c in range(0,len(data[0])):
        
        #[row,col,curdir]=[int(d) for d in optie.split('_')]
        grid = list(data)

        #dirs=[[-1,0],[0,1],[1,0],[0,-1]]
        #
        #    block_r=row+dirs[curdir%4][0]
        #    block_c=col+dirs[curdir%4][1]
            
        if data[block_r][block_c] != '#':
            #Probeer alleen nieuwe

            grid[block_r]=grid[block_r][:block_c]+'#'+grid[block_r][block_c+1:]
        
            if walk_hasloop(grid,start_row,start_col) == 1:
                blocks+=1
                block_list.append(str(block_r)+'_'+str(block_c))

print("Part 2",len(set(block_list)),"maar denk aan startpositie")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))