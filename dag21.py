# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
from functools import cache
import time
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(line)
    
f.close()

numpad=  [['7','8','9'],['4','5','6'],['1','2','3'],['','0','A']]

numpad=dict()
numpad.update({'7':[0,0],'8':[0,1],'9':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'1':[2,0],'2':[2,1],'3':[2,2],'0':[3,1],'A':[3,2]})

nump_r=3
nump_c=2


newp=dict()
## Beste moves van x naar y
#        from   to A   ^    >    v      <
newp.update({'A':['A','<A','vA','<vA','v<<A']})
newp.update({'^':['>A','A','v>A','vA','v<A']})
newp.update({'>':['^A','<^A','A','<A','<<A']})
newp.update({'v':['^>A','^A','>A','A','<A']})
newp.update({'<':['>>^A','>^A','>>A','>A','A']})
let_dict={'A':0,'^':1,'>':2,'v':3,'<':4}


move_dict=dict()

def moves(start_letter,end_letter,depth):
    key = start_letter+'_'+end_letter+'_'+str(depth)
    if key in move_dict:
        return move_dict[key]
    #print(start_letter,end_letter,depth)
    
    string = newp[start_letter][let_dict[end_letter]]
    
    if depth==0:
        return len(string)
    
    total_moves=0
    for b,e in zip('A'+string,string):
        total_moves+=moves(b,e,depth-1)
    
    move_dict.update({key:total_moves})
    return total_moves

total_p1=0
total_p2=0
for code in data:
    tstr=''
    nump_r=3
    nump_c=2

    outputs=list()
    outputs.append('')
    for letter in code:
        new_options=list()
        #find coordinates of current letter
        [new_nump_r,new_nump_c]=numpad[letter]
        
        #We zitten op de onderste rij en moeten naar de linker kolom. Dan is er maar 1 kortste route
        if nump_r==3 and new_nump_c==0:
            #Eerst omhoog dan naar links
            new_options.append('^'*max(nump_r-new_nump_r,0)+'<'*max(nump_c-new_nump_c,0)+'A')
        
        #We zitten op de linker kolom en moeten naar 0 of A
        elif nump_c==0 and new_nump_r==3:
            #1 kortste mogelijkheid > V
            new_options.append('>'*max(new_nump_c-nump_c,0)+'v'*max(new_nump_r-nump_r,0)+'A')
            
        elif nump_r!=new_nump_r and nump_c!=new_nump_c:
            #Beweging is in rechthoek 789456123 of 89 56 23 0A
            #Twee opties mogelijk die even kort zullen zijn
            #row and kolom zijn niet hetzelfde
            new_options.append('^'*max(nump_r-new_nump_r,0)+'v'*max(new_nump_r-nump_r,0)+'<'*max(nump_c-new_nump_c,0)+'>'*max(new_nump_c-nump_c,0)+'A') #^>> ^^>
            new_options.append('<'*max(nump_c-new_nump_c,0)+'>'*max(new_nump_c-nump_c,0)+'^'*max(nump_r-new_nump_r,0)+'v'*max(new_nump_r-nump_r,0)+'A') #>^ >^^
        
        else:
            #anders is er maar 1 optie
            new_options.append('<'*max(nump_c-new_nump_c,0)+'>'*max(new_nump_c-nump_c,0)+'^'*max(nump_r-new_nump_r,0)+'v'*max(new_nump_r-nump_r,0)+'A')
                             
                
        nump_r=new_nump_r
        nump_c=new_nump_c
        options=list(outputs)
        outputs=list()
        for option in options:
            for add in new_options:
                outputs.append(option+add)
        
    ## Part 1
    min_code=1000000000000000
    for tstr in outputs:
        total_moves=0
        for b,e in zip('A'+tstr,tstr):
            total_moves+=moves(b,e,2-1)
        min_code=min(min_code,total_moves)
    total_p1+=int(code[:3])*min_code
    
    ## Part 2
    min_code=1000000000000000
    for tstr in outputs:
        total_moves=0
        for b,e in zip('A'+tstr,tstr):
            total_moves+=moves(b,e,25-1)
        min_code=min(min_code,total_moves)
    total_p2+=int(code[:3])*min_code        



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))