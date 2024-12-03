# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
import re
start_time = time.time_ns()

total1 =0
total2=0
do=True

f = open("input.txt", "r")
for i,line in enumerate(f):
    a=line.replace('\n','').split('mul(')
      
    for regel in a:  
        m = re.match(r'\d+,\d+\)',regel) #zoek of er nu getal,getal) staat aan het begin van de regel
        if m:
            waardes=m.group().replace(')','').split(',') #haal getal,getal eruit
            total1+=int(waardes[0])*int(waardes[1])
            
            if do==True:
                total2+=int(waardes[0])*int(waardes[1])
        
        # Waneer we dont() of do() tegenkomen moeten we de komende mul( niet/wel meenemen
        if 'don\'t()' in regel:
            do=False
        if 'do()' in regel:
            do=True      
f.close()

print("Part 1",total1)
print("Part 2",total2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))