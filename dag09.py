# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
data2=list()
cur_id=0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    emptyspace=False
    
    for s in line:
        if emptyspace==False:
            for j in range(0,int(s)):
                data.append(cur_id)
            data2.append([cur_id,int(s)])
            cur_id+=1
            emptyspace=True
        else:
            for j in range(0,int(s)):
                data.append('.')
            data2.append(['.',int(s)])
            emptyspace=False   
f.close()

## sort for p1
i=0 #Index in data
back_c=len(data)-1 #Index van laatste getal
while i<len(data):
    if data[i]=='.': #als de huidige locatie vrij is, vervang hem dan met het laatste getal
        data[i]=data[back_c]
        data[back_c]='.'
        back_c-=1
    i+=1
    while data[back_c]=='.':
        back_c-=1
    if i==back_c:
        break
total_p1=0
for i,s in enumerate(data[:back_c+1]):
    total_p1+=i*s


##sort for p2
i=0
back_c=len(data2)-1

while True:
    if back_c<0:
        break
    if data2[back_c][0]=='.':
        back_c-=1
        continue
    find_l=data2[back_c][1]
    for i in range(0,back_c):
        if data2[i][0]=='.' and find_l<=data2[i][1]: #Hier is plek
            data2[i][1]-=find_l
            data2.insert(i,[int(data2[back_c][0]),int(data2[back_c][1])])
            data2[back_c+1][0]='.'
            back_c+=1
            break
    back_c-=1

##Calculate score for 2
i=0
total_p2=0
for [s,n] in data2:
    for j in range(0,n):
        if s!='.':
            total_p2+=i*s
        i+=1


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))