# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()


##Teken de grid, was wel handig
def print_grid(grid):
    global cr
    global cc
    for row,line in enumerate(grid):
        pr='' 
        for col,s in enumerate(line):
            if s==2: pr+=u'\u2588'
            elif s==1: pr+='O'
            elif s==3: pr+='['
            elif s==4: pr+=']'
            else: pr+=' '
            #Robot ook tekenen
            if row==cr and col==cc: pr=pr[:-1]+'@'
        print(pr)


f = open("input.txt", "r")
read_instr=False
gridd=list()
instr_list=''
for i,line in enumerate(f):
    if line=='\n':
        read_instr=True
        continue
    
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    if read_instr==True:
        instr_list+=line
    else:
        gridd.append(line)
f.close()

#Zet om naar grid en grid2, grid2 is twee keer zo groot
grid=np.zeros((len(gridd),len(gridd[0])))
grid2=np.zeros((len(gridd),2*len(gridd[0])))
for row,line in enumerate(gridd):
    for col,s in enumerate(line):
        if s== '#':
            grid[row,col]=2
            grid2[row,col*2]=2
            grid2[row,col*2+1]=2
        elif s=='O':
            grid[row,col]=1
            grid2[row,col*2]=3 #box is now 3&4 instead of 1
            grid2[row,col*2+1]=4
        elif s=='@':
            start_r=row
            start_c=col
            
#######################
#Part 1        
cr=start_r
cc=start_c
for instr in instr_list:
    if instr=='>': direc=[0,1]
    if instr=='<': direc=[0,-1]
    if instr=='^': direc=[-1,0]
    if instr=='v': direc=[1,0]
    
    #Als het plekje vrij is maak de beweging
    test_r=cr+direc[0]
    test_c=cc+direc[1]
    if grid[test_r,test_c]==0:
        cr=test_r
        cc=test_c
        
    elif grid[test_r,test_c]==1: #Beweegbaar ding
        boxes=1

        while grid[test_r+direc[0]*boxes,test_c+direc[1]*boxes]==1: #er zijn meer beweegbare dingen
            boxes+=1

        if grid[test_r+direc[0]*boxes,test_c+direc[1]*boxes]==0: #Als de volgende plek leeg is:
            grid[test_r,test_c]=0 #Huidige vakje is leeg, maar met robot
            grid[test_r+direc[0]*boxes,test_c+direc[1]*boxes]=1 #Laatste vakje is een box
            cr=test_r
            cc=test_c
end1_r=cr
end1_c=cc
# Bereken de eindscore        
total_p1=0      
for row,line in enumerate(grid):
    for col,d in enumerate(line):
        if d==1: #box
            total_p1+=100*row+col            

            
#####################
#Part 2
cr=start_r
cc=start_c*2
#print_grid(grid2)
for instr in instr_list:
    if instr=='>': direc=[0,1]
    if instr=='<': direc=[0,-1]
    if instr=='^': direc=[-1,0]
    if instr=='v': direc=[1,0]
    
    #Als het plekje vrij is maak de beweging
    test_r=cr+direc[0]
    test_c=cc+direc[1]
    #print("\nMove instr",instr)
    if grid2[test_r,test_c]==0:
        cr=test_r
        cc=test_c
        #print_grid(grid2)
        
    elif grid2[test_r,test_c]>2: #Beweegbaar ding [] is 34 in de grid
        boxes=1
        
        if instr=='>' or instr=='<': #Horizontale beweging is vanouds
            while grid2[test_r,test_c+2*direc[1]*boxes]>2: #er zijn meer beweegbare dingen
                boxes+=1
            #print(cr,cc,instr,"verschuifbaar ding",boxes)
            #Geen beweegbaar ding meer
            if grid2[test_r,test_c+direc[1]*boxes*2]==0: #Als de volgende plek leeg is:
                #print("verschoven")
                l1=cc
                r1=cc+direc[1]*boxes*2
                l2=test_c
                r2=test_c+direc[1]*boxes*2
    
                grid2[test_r,min(l2,r2):max(l2,r2)+1]=grid2[test_r,min(l1,r1):max(l1,r1)+1] #eem lekker slicen
                grid2[test_r,test_c]=0 #Huidige vakje is leeg op de kaart, maar natuurlijk wel met robot
                cr=test_r
                cc=test_c
                
        if instr=='^' or instr=='v': #verticale beweging is bijzonder
           #Maak een lijst van blokjes die bewegen
           mbs=[[test_r,test_c]] #Moving boxes
           #Als we nu tegen ] duwen voeg [ toe
           if grid2[mbs[0][0],mbs[0][1]]==4:
               mbs.append([test_r,test_c-1])               
           #Als we nu tegen ] duwen voeg ] toe
           elif grid2[mbs[0][0],mbs[0][1]]==3:
               mbs.append([test_r,test_c+1])
           
            
           moving=True
           i=0
           while i<len(mbs):
               cur_loc=mbs[i]
               check_loc=[mbs[i][0]+direc[0],mbs[i][1]]
               
               #Kijk of het volgende vakje niet gebelokker is voor elk blokje, anders wordt de hele beweging geblokkeerd!
               if grid2[check_loc[0],check_loc[1]]==2: #object in de weg
                   moving=False
                   break
               
               #Als het volgende blokje ook beweegbaar en [ is
               if grid2[check_loc[0],check_loc[1]]==3:
                   #Voeg [ toe als deze nog niet in de lijst staan
                   if [check_loc[0],check_loc[1]] not in mbs:
                       mbs.append([check_loc[0],check_loc[1]])
                   #Voeg nieuwe ] toe
                   if [check_loc[0],check_loc[1]+1] not in mbs:
                       mbs.append([check_loc[0],check_loc[1]+1])
               
                #Als het volgende blokje ook beweegbaar en ] is    
               if grid2[cur_loc[0]+direc[0],cur_loc[1]]==4:
                   #Voeg nieuwe ] toe
                   if [check_loc[0],check_loc[1]] not in mbs:
                       mbs.append([check_loc[0],check_loc[1]])
                   #Voeg nieuwe [ toe
                   if [check_loc[0],check_loc[1]-1] not in mbs:
                       mbs.append([check_loc[0],check_loc[1]-1])
               i+=1
           #Voer de verplaatsingen uit
           if moving==True:
               cr=test_r
               cc=test_c
               for cur_loc in mbs[::-1]:#reverse order
                   grid2[cur_loc[0]+direc[0],cur_loc[1]]=grid2[cur_loc[0],cur_loc[1]]
                   grid2[cur_loc[0],cur_loc[1]]=0

#Bereken de eindscore               
total_p2=0      
for row,line in enumerate(grid2):
    for col,d in enumerate(line):
        if d==3: #box left side
            total_p2+=100*row+col                

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))

end2_r=cr
end2_c=cc
cr=end1_r
cc=end1_c
print_grid(grid)
print('\n')
cr=end2_r
cc=end2_c
print_grid(grid2)