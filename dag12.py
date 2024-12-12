# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import time
import numpy as np

start_time = time.time_ns()

f = open("input.txt", "r")
plants=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    plants.append(line)
f.close()
#Afmetingen grid van planten
nrow=len(plants)
ncol=len(plants[0])

#Maak een lijst van regions met bijbehorende coordinates
cells_visited=np.zeros((nrow,ncol))
regions=list()
dirs=[[0,1],[1,0],[0,-1],[-1,0]]
for row,line in enumerate(plants):
    for col,s in enumerate(line):
        
        #Als we dit vakje al hebben bekeken bij een eerdere zoektocht skip hem dan.
        if cells_visited[row][col]==1:
            continue
        
        #Voeg vakje toe aan bekeken cells
        cells_visited[row][col]=1
        
        region=list()
        region.append([row,col])
        
        i=0
        heap = [[row,col]]
        while i<len(heap):
            for direc in dirs:
                cr = heap[i][0]+direc[0]
                cc = heap[i][1]+direc[1]
                #Does the next location exist?
                if cr>=nrow or cr<0 or cc>=ncol or cc<0:
                    continue
                #Niet al bezocht
                if cells_visited[cr][cc]==1:
                    continue
                
                #Plant hoor erbij
                if plants[cr][cc] == s:
                    region.append([cr,cc])
                    cells_visited[cr][cc]=1
                    heap.append([cr,cc])
            i+=1
        regions.append(region)


####################
#Find options for holes in each region
hole_list=list()
for region in regions:
    reg_holes=list()
    for [cr,cc] in region:
        for direc in dirs:
            #Elk vakje genereert 4 plekken waar een gat zou kunnen zitten.
            #Als daar een stukje regio zit, of we kennen hem al dan hoeft hij niet in de lijst
            if [cr+direc[0],cc+direc[1]] not in reg_holes and [cr+direc[0],cc+direc[1]] not in region:
                reg_holes.append([cr+direc[0],cc+direc[1]])
    hole_list.append(reg_holes)

###############
#Part 1
total_p1=0           
for region in regions:
    cur_perimeter=0
    for vakje in region:
        cur_perimeter+=4
        for direc in dirs:
            cr = vakje[0]+direc[0]
            cc = vakje[1]+direc[1]
            if [cr,cc] in region:
                cur_perimeter-=1
    total_p1+=cur_perimeter*len(region)

#######
#Part 2
total_p2=0
#Loop- en kijkrichtingen initialiseren, kijk richting is 90 graden verdraaid 
#tov looprichting (bijv: kijk naar rechts,doe een stap omhoog)
ldirs=[[1,0],[0,-1],[-1,0],[0,1]]  #D L U R
wdirs=[[0,1],[1,0],[0,-1],[-1,0]]

#Elke regio en een lijst van mogelijke gaten
for region,hole_options in zip(regions,hole_list):
    n_sides=0
    sr=region[0][0]-1 #start een vakje boven het startpunt
    sc=region[0][1]
    
    lookdir=0
    if [cr,cc] in hole_options:
        hole_options.remove([cr,cc])

    #Elke element van de lijst van mogelijke gaten is een beginpunt van een contour
    #Verwijderen opties uit de lijst zodra we ze tegenkomen.
    while len(hole_options) > 0:
        sr=hole_options[0][0]
        sc=hole_options[0][1]
        cr=sr
        cc=sc
        
        #Determine lookdir, je moet wel naar een vakje kijken voor het algoritme om te beginnen
        while [sr+ldirs[lookdir][0],sc+ldirs[lookdir][1]] not in region:
            lookdir=(lookdir+1)%4
        startdir=lookdir

        while True:
            #Kijk naar het vakje in ldir
            if [cr+ldirs[lookdir][0],cc+ldirs[lookdir][1]] in region: #Als het bekeken vakje in de regio zit
                if [cr+wdirs[lookdir][0],cc+wdirs[lookdir][1]] not in region: #En het volgende vakje in de looprichting vrij is
                    cr+=wdirs[lookdir][0]
                    cc+=wdirs[lookdir][1]
                    
                else: #Volgende loopvakje is niet vrij, draai nog 90 graden door, dus een extra side
                    lookdir=(lookdir-1)%4
                    n_sides+=1
            else: #Beken vakje is leeg, maak een stapje en kijk naar een andere richting, dus een extra side
                lookdir=(lookdir+1)%4
                cr+=wdirs[lookdir][0]
                cc+=wdirs[lookdir][1]
                n_sides+=1
                
            if [cr,cc] in hole_options:
                hole_options.remove([cr,cc])
                
            #Als we rond zijn gelopen en zijn gedraaid    
            if cr==sr and cc==sc and startdir==lookdir:
                break
            
    total_p2+=len(region)*n_sides


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))