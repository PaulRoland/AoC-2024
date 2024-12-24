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
        print(key,graph[key][0])

string ='' 
for n in bits:
    string+=str(n)

Z_org = int(string,2)
total_p1=Z_org


###Part 2
bits_x=[0 for d in range(0,45)]
bits_y=[0 for d in range(0,45)]
for key in graph:
    if key[0]=='x':
        bits_x[-int(key[1:3])-1]=graph[key]
    if key[0]=='y':
        bits_y[-int(key[1:3])-1]=graph[key]

string_x ='' 
string_y ='' 
for x,y in zip(bits_x,bits_y):
    string_x+=str(x)
    string_y+=str(y)

X_start = int(string_x,2)
Y_start = int(string_y,2)
Z_end=X_start+Y_start

print(X_start,Y_start,Z_end)
diff = Z_end ^ Z_org
print(bin(diff))

bit_list=list() 
for i,s in enumerate(bin(diff)[::-1]):
    if s=='1':
        if i<10:
            bit_list.append('z0'+str(i))
        else:
            bit_list.append('z'+str(i))
print(bit_list)

                    

key_list=list()
values_org=dict()
for key in graph:
    
    if key[0]=='x' or key[0]=='y':
        values_org.update({key:graph[key]})
        continue
    
    values_org.update({key:graph[key][0]})
    key_list.append(str(key))



impact=dict()
impact2=dict()
for swap in key_list: 
    graph=dict()
    for key in graph_org:
        if type(graph_org[key])==type(1):
            graph.update({key:int(graph_org[key])})
            continue
        graph.update({key:list(graph_org[key])})
    graph[swap]=(values_org[swap]-1)*(-1)
    
    ##opnieuw alles verbinden
    error=False
    for key in graph:
        a=connect(key,0)
    
    if error==True:
        continue
    
    bits=[0 for d in range(0,50)]
    
    impact.update({swap:[]})
    impact2.update({swap:[]})
    for key in graph:
        if key[0]=='x' or key[0]=='y':
            continue
        
        if key==swap:
            continue
        if graph[key][0]!=values_org[key]:
            if key[0]=='z':                
                impact[swap].append(key) 
                
            impact2[swap].append(key)


oplossingen=list()
def find_keys(keys_left,depth,keys_used):
    global impact
    if depth==1:
        print(keys_left)
    if keys_left==[] and depth==0:
        print("een gevonden")
        oplossingen.append(keys_used)
        return
    
    for key in impact:
        if len(impact[key])>0:
            mogelijk=True
            for value in impact[key]:
                if value not in keys_left:
                    mogelijk=False
            
            new_keys_left=list(keys_left)
            new_keys_used=list(keys_used)
            if mogelijk==True:
                new_keys_used.append(key)
                for value in impact[key]:
                    new_keys_left.remove(value)
                find_keys(new_keys_left,depth-1,new_keys_used)
    return
 


#Binary adder moet aan bepaalde voorwaarden voldoen
#inputs en outputs zitten altijd aan xors,
#xors zitten alleen aan inputs en outputs, hopelijk vinden we daarmee al wat keys
fouten=list()
for key in graph_org:
    if key[0]=='x' or key[0]=='y':
        continue
    if key[0]=='z':
        if graph_org[key][3]!='XOR' and key!='z45':
            print(key)
            fouten.append(key)
    
    if graph_org[key][3]=='XOR':
        if graph_org[key][1][0]=='x' and graph_org[key][2][0]=='y':
            continue
        elif graph_org[key][1][0]=='y' and graph_org[key][2][0]=='x':
            continue
        elif key[0]=='z':
            continue
        print(key)
        fouten.append(key)
        
        
for fout_key in fouten:
    if fout_key[0]=='z':
        bit_list.remove(fout_key)
    else:
        for value in impact[fout_key]:
            bit_list.remove(value)

#De rest van de keys vinden we 
rij = find_keys(bit_list,8-len(fouten),fouten)

filtered_oplossingen=list()
for oplossing in oplossingen:
    oplossing.sort()
    if oplossing in filtered_oplossingen:
        continue
    filtered_oplossingen.append(oplossing)
    

for oplossing in filtered_oplossingen:
    operations = list()
    outputs=list()
    inputs=list()
    for element in oplossing:
        operations.append(graph[element][3])
        in1=graph[element][1]
        in2=graph[element][2]
        input1=[values_org[in1],values_org[in2]]
        if input1==[0,1]:
            input1=[1,0]
        inputs.append(input1)
        outputs.append(values_org[element])
        
print(oplossingen)

##Hier moet ik eigenlijk alle oplossingen testen en dan de enige goede overhouden, misschien heb ik daar later zin in.
#Er zijn nu toch maar 3 unieke mogelijke oplossingen over, dat is nog wel te proberen.            
for i,oplossing in enumerate(oplossingen):
    if oplossing in oplossingen[:i]:
        continue
    oplossing.sort()
    part2=','.join(oplossing)
    print("Part 2",part2)
                                 
    

'''  
print("Part 1",total_p1,string)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
'''