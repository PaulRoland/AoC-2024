# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def connect(key,depth):
    #print(key)
    global error
    if type(graph[key])==type(list()): #actie
    
        #Als deze al eerder bepaald is
        if graph[key][0]!=2:
            return graph[key][0]
        
        if depth>1000:
            #print("dit gaat niet goed!!!")
            error=True
            return 0
        
        a=connect(graph[key][1],depth+1)
        b=connect(graph[key][2],depth+1)
        
        if graph[key][3]=='AND':
            graph[key][0]=a & b

        elif graph[key][3]=='XOR':
            graph[key][0] =a ^ b

        elif graph[key][3]=='OR':
            graph[key][0] =a | b
            

        return graph[key][0]
    
    return graph[key]
        
                  

f = open("input.txt", "r")
part2=False

graph=dict()

for i,line in enumerate(f):
    if line=='\n':
        part2=True
        continue
    
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    keys=line.split(' ')
    if part2==True:        
        key=line.split(' ')
        graph.update({key[4]:[2,key[0],key[2],key[1]]})

    else:
        key=line.split(':')
        graph.update({key[0]:int(key[1])})                      
                    
f.close()
graph_org=dict(graph)
graph_org=dict()
for key in graph:
    if type(graph[key])==type(1):
        graph_org.update({key:int(graph[key])})
        continue
    graph_org.update({key:list(graph[key])})


for key in graph:
    a=connect(key,0)

bits=[0 for d in range(0,50)]
for key in graph:
    if key[0]=='z':
        bits[-int(key[1:3])-1]=graph[key][0]

string ='' 
for n in bits:
    string+=str(n)

Z_org = int(string,2)
total_p1=Z_org


###Part 2
#Ripple Carry Binary adder moet aan bepaalde voorwaarden voldoen
#outputs zitten altijd aan xors (behalve bij je laatste bit)
#output Zn--<--XOR-----------XOR[Xn, Yn]
#               L----- OR---AND[Xn-1,Yn-1]
#Laatste bit is anders
fouten=list()
for key in graph:
    if key[0]=='z':
        if graph[key][3]!='XOR':
            fouten.append(key)
fouten.remove('z45')

#Aan de inputs hangen alleen AND en XOR
for key in graph:
    if key[0]=='x' or key[0]=='y':
        continue
    if 'x' in graph[key][1] or 'x' in graph[key][2]:
        if graph[key][3]=='OR':
            fouten.append(key)


#XOR hangt aan inputs of is deel van een output
for key in graph:
    if key[0]=='x' or key[0]=='y':
        continue
    if graph[key][3]=='XOR':
        if 'x' in graph[key][1] or 'x' in graph[key][2]:
            continue
        if key[0]=='z':
            continue
        fouten.append(key)
        
#Een AND hangt nooit aan een AND, behalve in het begin bij input bits 0
for key in graph:
    if key[0]=='x' or key[0]=='y':
        continue
    if key=='z01':
        continue
    if graph[key][3]=='AND':
        con1=graph[key][1]
        con2=graph[key][2]
        if con1[0]=='x' or con2[0]=='x':
            continue
        if graph[con1][3]=='AND':
            fouten.append(con1)
        if graph[con2][3]=='AND':
            fouten.append(con2)
for key in graph:
    if key[0]=='x' or key[0]=='y':
        continue
    if graph[key][3]=='AND' and ('x00' in graph[key][1] or 'y00' in graph[key][1]):
        fouten.remove(key)

#Een OR krijgt alleen van ANDs
for key in graph:
    if key[0]=='x' or key[0]=='y':
        continue
    if key=='z45':
        continue
    if graph[key][3]=='OR':
        con1=graph[key][1]
        con2=graph[key][2]
        if con1[0]=='x' or con2[0]=='x':
            continue
        if graph[con1][3]!='AND':
            fouten.append(con1)
        if graph[con2][3]!='AND':
            fouten.append(con2)
fouten=list(set(fouten))
fouten.sort()

    
    

print("Dag 24")
print("Part 1",total_p1)
print("Part 2",','.join(fouten))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
