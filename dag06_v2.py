# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import bisect
import time
start_time = time.time_ns()

def path_from_points(turnpoints):
    path=list()
    for a,b in zip(turnpoints,turnpoints[1:]):
        a=[int(d) for d in a.split('_')]
        b=[int(d) for d in b.split('_')]
        
        rows=[*range(min(a[0],b[0]),max(a[0],b[0])+1)]
        cols=[*range(min(a[1],b[1]),max(a[1],b[1])+1)]
        
        if len(rows)>len(cols):
            for r in rows:
                path.append(str(r)+'_'+str(cols[0]))
        if len(rows)<=len(cols):
            for c in cols:
                path.append(str(rows[0])+'_'+str(c))
    return path

def walk(block_rf,block_cf,start_r,start_c,dr):
    r=start_r
    c=start_c
    
    tp = list()
    tp.append(str(r)+'_'+str(c))
    while True:
        if dr==0: #up
            if block_cf[c]==[]: 
                r=0
                break
            if r<min(block_cf[c]): 
                r=0
                break
            ind = bisect.bisect_left(block_cf[c],r) #find location of next obstacle in column
            r=block_cf[c][ind-1]+1
            dr=1
            
        elif dr==2: #down
            if block_cf[c]==[]:
                r=len(block_cf)-1
                break
            if r>max(block_cf[c]):
                r=len(block_cf)-1
                break
            ind = bisect.bisect_right(block_cf[c],r)
            r=block_cf[c][ind]-1
            dr=3
            
        elif dr==1: #right
            if block_rf[r]==[]:
                c=len(block_rf)-1
                break
            if c>max(block_rf[r]):
                c=len(block_rf)-1
                break
            ind = bisect.bisect_right(block_rf[r],c) #find next obstacle in row
            c=block_rf[r][ind]-1
            dr=2
            
        elif dr==3: #left   
            if block_rf[r]==[]:
                c=0
                break
            if c<min(block_rf[r]):
                c=0
                break
            ind = bisect.bisect_left(block_rf[r],c)
            c=block_rf[r][ind-1]+1
            dr=0 
            
        tp.append(str(r)+'_'+str(c))
        
    #klaar    
    tp.append(str(r)+'_'+str(c))
    return tp

def loop(block_rf,block_cf,start_r,start_c,dr):
    r=start_r
    c=start_c
    tp = list()
    while True:
        if dr==0: #up
            if block_cf[c]==[]: return 0
            if r<min(block_cf[c]): return 0
            ind = bisect.bisect_left(block_cf[c],r) #find location of next obstacle in column
            r=block_cf[c][ind-1]+1
            dr=1
            
        elif dr==2: #down
            if block_cf[c]==[]: return 0
            if r>max(block_cf[c]): return 0
            
            ind = bisect.bisect_right(block_cf[c],r)
            r=block_cf[c][ind]-1
            dr=3
            
        elif dr==1: #right
            if block_rf[r]==[]: return 0
            if c>max(block_rf[r]): return 0
            
            ind = bisect.bisect_right(block_rf[r],c)            #find next obstacle in row
            c=block_rf[r][ind]-1
            dr=2
            
        elif dr==3: #left   
            if block_rf[r]==[]: return 0
            if c<min(block_rf[r]): return 0
            
            ind = bisect.bisect_left(block_rf[r],c)
            c=block_rf[r][ind-1]+1
            dr=0
            
        if str(r)+'_'+str(c)+'_'+str(dr) in tp:
            tp.append(str(r)+'_'+str(c)+'_'+str(dr))
            #print(tp)
            return 1
        
        tp.append(str(r)+'_'+str(c)+'_'+str(dr))
    #klaar    
    return 0


f = open('input.txt')
grid=list()
for row,line in enumerate(f):
    line=line.strip('\n')
    grid.append(line)
f.close()

block_rf=[ [] for a in range(0,len(grid))]
block_cf=[ [] for a in range(0,len(grid[0]))]

for row,line in enumerate(grid):
    for col,s in enumerate(line):
        if s=='#':
            block_rf[row].append(col)
            block_cf[col].append(row)
        if s=='^':
            start_r=row
            start_c=col

direc=0
### Find all points where the direction changes, including start and end
turnpoints = walk(block_rf,block_cf,start_r,start_c,0)

### Create a path list from the turnpoints list
path = path_from_points(turnpoints)

### Try every point on the route for a potential blockage
loop_count=0
for rc in set(path):
    [new_r_block,new_c_block]= [int(d) for d in rc.split('_')]

    if new_r_block == start_r and new_c_block ==start_c:
        #begin positie niet testen want daar mag toch niets komen
        continue
    
    block_rf[new_r_block].append(new_c_block)
    block_cf[new_c_block].append(new_r_block)
    block_rf[new_r_block].sort()
    block_cf[new_c_block].sort()

    loop_count += loop(block_rf,block_cf,start_r,start_c,0) 
    block_rf[new_r_block].remove(new_c_block)
    block_cf[new_c_block].remove(new_r_block)

print("Part 1",len(set(path)))
print("Part 2",loop_count)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))