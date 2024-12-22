# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def nextn(magic_n,digit,depth,n):
    magic_n=((magic_n*64) ^ magic_n)%16777216
    magic_n=((magic_n//32) ^ magic_n)%16777216
    magic_n=((magic_n*2048) ^ magic_n)%16777216

    new_digit=magic_n%10
    changes[n].append(new_digit-digit)
    prices[n].append(new_digit)

    if depth==1: 
        return magic_n
    return nextn(magic_n,new_digit,depth-1,n)


numbers=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    numbers.append(int(line)) 
f.close()

total_p1=0
changes=list([] for _ in range(0,len(numbers)))
prices=list([] for _ in range(0,len(numbers)))
for i,number in enumerate(numbers):
    a = nextn(number,number%10,2000,i)
    total_p1+=a


ptrndict=dict()
ranges=list(range(-9,10))

#Zet alle mogelijke combinaties in een dictionary
for a in ranges:
    for b in ranges:
        for c in ranges:
            for d in ranges:
                key= str(a)+','+str(b)+','+str(c)+','+str(d)
                ptrndict.update({key:[-1,0]})

total_p2=0
for n,nb in enumerate(numbers):
    nb=list(changes[n])
    for i in range(0,2000-3):
        key= str(nb[i])+','+str(nb[i+1])+','+str(nb[i+2])+','+str(nb[i+3])
                
        #Kijk wat de eerste keer dat een sequence voorkomt het oplevert en voeg toe aan dict
        if ptrndict[key][0]==n: #Sequence al eerder tegengekomen bij dit startnummer, dat telt dus niet
            continue
        ptrndict[key][0]=n
        ptrndict[key][1]+=prices[n][i+3]
        total_p2=max(total_p2,ptrndict[key][1])

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))