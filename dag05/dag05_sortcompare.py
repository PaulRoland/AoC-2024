# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import time
start_time = time.time_ns()

def check_update(update):
    for a,b in zip(update,update[1:]):
        if b in orders[a]:
            continue
        else:
            return 0
    return update[int(len(update)/2)]


def reorder_update(update):
    global comparisons1
    i=0
    while i<len(update)-1:
        comparisons1+=1
        if update[i+1] in orders[update[i]]:
            i+=1
        else:
            #swap twee waardes
            tmp = update[i+1]
            update[i+1] = update[i]
            update[i] = tmp        
            i=max(0,i-1) #Als deze is gewijzigd moet de stap ervoor ook weer gecontroleerd worden
            
    return update[int(len(update)/2)]

def reorder_update_bubblehalf(update):
    global comparisons3
    i=0
    half = int(len(update)/2)
    for a in range(0,half+1):
        i=0
        while i<len(update)-1-a:
            comparisons3+=1
            if update[i+1] not in orders[update[i]]: #Kijk of huidige waarde voor de volgende waarde moet blijven, zo nee:
                #swap twee waardes
                tmp = update[i+1]
                update[i+1] = update[i]
                update[i] = tmp        
            i+=1
            
    return update[half]

def reorder_update_bubble(update):
    global comparisons2
    i=0
    half = int(len(update)/2)
    for a in range(0,len(update)):
        i=0
        while i<len(update)-1-a:
            comparisons2+=1
            if update[i+1] not in orders[update[i]]: #Kijk of huidige waarde voor de volgende waarde moet blijven, zo nee:
                #swap twee waardes
                tmp = update[i+1]
                update[i+1] = update[i]
                update[i] = tmp        
            i+=1
            
    return update[half]

comparisons1=0
comparisons2=0
comparisons3=0
f = open("input.txt", "r")
orders=[ [] for _ in range(100) ]
updates=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    if '|' in line:
        [a,b]=[int(i) for i in line.split('|')]
        orders[a].append(b)
    if ',' in line:
        updates.append([int(i) for i in line.split(',')])  
f.close()

total_1=0
total_2=0
for update in updates:
    page = check_update(update)
    total_1+=page
    
    if page == 0:
        page=reorder_update(update)
        page=reorder_update_bubble(update)
        page=reorder_update_bubblehalf(update)
        total_2+=page
    

print("Part 1",total_1)
print("Part 2",total_2)
print("Gnome/stupid",comparisons1,"vergelijkingen")
print("Bubble-sort ",comparisons2,"vergelijkingen")
print("Bubble-half ",comparisons3,"vergelijkingen")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))