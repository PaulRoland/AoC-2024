# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open('test.txt')
for line in f:
    data=[int(s) for s in line.replace('\n','')]
    numbers=data[::2]
    spaces=data[1::2]
f.close()

loc=0
ID=0
back_ID=len(numbers)-1
total_p1=0
numbers_start=list(numbers.copy())
while True:
    #Huidige getal + ID*locatie voor het aantal getallen dat er is
    total_p1+=sum(range(loc,loc+numbers[ID]))*ID
    loc+=numbers[ID]
    
    if numbers[ID+1]==0: #Laatste getal? Dan daarna stoppen
        break
    #Vul de .... op na dit getal, gegeven in spaces[ID]
    for n in range(spaces[ID]):        
        while numbers[back_ID]==0:
            back_ID-=1 #Schuif een getal naar voren als de getallen op zijn in dit ID
        numbers[back_ID]-=1
        total_p1+=loc*back_ID
        loc+=1
    ID+=1
    
     
loc=0
ID=0
total_p2=0
numbers=list(numbers_start.copy())
numbers_available=[1 for _ in numbers]

test_string=''
while True:
    #Huidige getal + ID*locatie voor het aantal getallen dat er is
    if numbers_available[ID]==1: #Dit nummer hebben we nog niet gebruikt in verplaatsing
        total_p2+=sum(range(loc,loc+numbers[ID]))*ID
        for n in range(loc,loc+numbers[ID]):
            test_string+=str(ID)
    loc+=numbers[ID]
    
    #Als er nog getallen over zijn die we niet verplaatst hebben dan gaan we door
    if sum(numbers_available[ID:])==0:
        break
    
    space = spaces[ID]
    space_left=True
    found=True
    while space_left==True and found==True:    
        back_ID=len(numbers)-1
        found=False
        while back_ID>ID: #Probeer alle items na het huidige getal om de spaties te vullen

            if numbers_available[back_ID]==1: #Als het huidige nummer beschikbaar is
                if numbers[back_ID]<=space: #en het past
                    #Maak huidige nummer onbeschikbaar
                    numbers_available[back_ID]=0
                    
                    #Voeg score toe, backID per locatie die het bezet
                    total_p2+=sum(range(loc,loc+numbers[back_ID]))*back_ID
                    
                    for n in range(loc,loc+numbers[back_ID]):
                        test_string+=str(back_ID)
                            
                    space-=numbers[back_ID]
                    loc+=numbers[back_ID]
                    found=True
                    
                    #Stop als er geen ruimte meer is
                    if space==0:
                        space_left=False
                    break                
            back_ID-=1 #Volgende element, van achteren
    loc+=space
    ID+=1
    
    
print("Part 1",total_p1)
print("Part 2",total_p2)
            
    
    


