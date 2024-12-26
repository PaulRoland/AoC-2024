# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import time
start_time = time.time_ns()

def connect(key):
    #Als deze al eerder bepaald is of een input (want 0 of 1)
    if graph[key][0]!=2:
        return graph[key][0]
    
    #Open nieuwe inputs als nodig
    a=connect(graph[key][1])
    b=connect(graph[key][2])
    
    if graph[key][3]=='AND':
        graph[key][0]=a & b
    elif graph[key][3]=='XOR':
        graph[key][0] =a ^ b
    elif graph[key][3]=='OR':
        graph[key][0] =a | b
    return graph[key][0]

graph=dict()                         
f = open("input.txt", "r")
for i,line in enumerate(f):
    keys=line.replace('\n','').split(' ')
    if len(keys)>2:
        graph.update({keys[4]:[2,keys[0],keys[2],keys[1]]})
    elif len(keys)>1:
        graph.update({keys[0][:-1]:[int(keys[1])]})                                    
f.close()

bits=[0 for d in range(0,46)]
#Generate keys and find the value for each corresponding bit
for i in range(0,46):
    bits[-i-1]=connect("z{:02d}".format(i))
#Merge bits into one string and give the decimal value
total_p1=int(''.join([str(n) for n in bits]),2)

##################################################################
###Part 2
#Ripple Carry Binary adder moet aan bepaalde voorwaarden voldoen
fouten=list()

for key in graph:
    #Negeer input wires
    if key[0]=='x' or key[0]=='y':
        continue
    
    #Outputs zitten altijd aan xors (behalve bij je laatste bit)
    if key[0]=='z':
        if graph[key][3]!='XOR' and key!='z45':
            fouten.append(key)

    con1=graph[key][1]
    con2=graph[key][2]
    
    if con1[0]=='x' or con2[0]=='x':
        #Gates die hangen aan een input zijn nooit een OR
        if graph[key][3]=='OR':
            fouten.append(key)
        continue
    
    #######
    #XOR hangt aan inputs of is deel van een output
    if graph[key][3]=='XOR':    
        if key[0]!='z':                
            fouten.append(key)

    ################        
    #Een AND hangt nooit aan een AND, behalve in het begin bij input bits 0
    elif graph[key][3]=='AND':
        if graph[con1][3]=='AND':
            if graph[con1][1]!='x00' and graph[con1][1]!='y00':
                fouten.append(con1)
        if graph[con2][3]=='AND':
            if graph[con2][1]!='x00' and graph[con2][1]!='y00':
                fouten.append(con2)
        
    ###############
    #Een OR krijgt alleen van ANDs, behalve bij je laatste bit
    elif graph[key][3]=='OR':
        if key=='z45':
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
