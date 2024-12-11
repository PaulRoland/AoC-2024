# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    stones=line.split(' ')
    
f.close()

blinks=75

single_digits=[[0 for d in range(0,11)] for a in range(0,blinks+10)]
offset_digits=[0 for d in range(0,blinks+10)]
#single digits and 16192 describe all loops
#0 geeft na 1: 1x*1
#1 geeft na 3:  2 0 2 4
#2 geeft na 3:  4 0 4 8
#3 geeft na 3: 6 0 7 2
#4 geeft na 3: 8 0 9 6
#0 1,2,3,4,5,6,7,8,9,16192
offsets=[
    [1], #gaat direct naar 1
    [1,2,4],
    [1,2,4],
    [1,2,4],
    [1,2,4],
    [1,1,2,4,8],
    [1,1,2,4,8],
    [1,1,2,4,8],
    [1], #8 gaat naar 16192
    [1,1,2,4,8], #9
    [1,2,4,7]] #16192
    
    
digits_from_loops=[
[0,1,0,0,0,0,0,0,0,0,0],
[1,0,2,0,1,0,0,0,0,0,0],
[1,0,0,0,2,0,0,0,1,0,0],
[1,0,1,0,0,0,1,1,0,0,0],
[1,0,0,0,0,0,1,0,1,1,0],
[2,0,2,0,1,0,0,0,3,0,0],
[0,0,1,0,2,2,1,1,0,1,0],
[1,0,2,1,0,0,2,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1],
[0,1,0,1,1,0,2,0,2,1,0],
[0,0,2,1,0,0,1,2,0,0,1]]


for blink in range(0,blinks):
    new_stones=list()
    for stone in stones:
        #Single digits houden we los bij
        if len(stone)==1:
            single_digits[blink][int(stone)]+=1
            continue
        if stone=='16192':
            single_digits[blink][10]+=1
            continue
        
        if len(stone)%2==0: #even
            new_stones.append(str(int(stone[:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:])))
            continue
        else:
            new_stones.append(str(int(stone)*2024))
    stones=list(new_stones)
    
    #Verwerk de single digits
        
    for digit,aantal in enumerate(single_digits[blink]):
        #Voeg een offset toe aan de hand van de single digits.
        #Tel ze mee voor vandaag blink+0 en voor de komende blinks waar nodig
        for n,offset in enumerate(offsets[digit]):
            offset_digits[blink+n]+=aantal*offset #Houdt rekening met de toekomstige resulterende stenen in de komende blinks.
        
        #Voeg na n blinks een aantal nieuwe single digit stenen toe
    for digit,aantal in enumerate(single_digits[blink]):   
        for n,offset in enumerate(offsets[digit]):
            continue
        for nds,new_digit_stone in enumerate(digits_from_loops[digit]):
            single_digits[blink+n+1][nds]+=aantal*new_digit_stone
            
    #print(single_digits[blink],stones)
    #print(blink+1,':',len(stones),offset_digits[blink],single_digits[blink+1])
    print(blink+1,':',len(stones)+offset_digits[blink])



print("Part 1")
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))