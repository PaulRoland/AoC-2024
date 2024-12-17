# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import time
start_time = time.time_ns()

##Input
reg_A=66752888
reg_B=0
reg_C=0
program=[2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]

def lc(operand,lit_or_combo,registry):
    if lit_or_combo==0: #literal
        return operand
    else:
        if operand<4:
            return operand
        elif operand==7:
            return 0
        elif operand>=4:
            return registry[operand-4] #Return a,b,c


reg=[reg_A,reg_B,reg_C]
operations=list() #[operation, operand, literal(0)/combo(1)
i=0

while i<len(program):
    #print(i)
    #print(operations)
    if program[i]==3 or program[i]==1:
        operations.append([program[i],program[i+1],0])
        i+=2
    elif program[i]==0 or program[i]==2 or program[i]==4 or program[i]==5 or program[i]==6 or program[i]==7:
        operations.append([program[i],program[i+1],1])
        i+=2
        
##########
#Part 1
instr=0                
output=list()
while instr<len(operations):
    [opcode,operand,lci] = operations[instr]
    instr+=1
    
    if opcode==0:
        reg[0] = int(reg[0]/(2**lc(operand,lci,reg))) #adv
    if opcode==1:
        reg[1] = reg[1] ^ lc(operand,lci,reg)
    if opcode==2:
        reg[1] = lc(operand,lci,reg)%8
    if opcode==3:
        if reg[0]==0:
            continue
        instr=lc(operand,lci,reg)
    if opcode==4:
        reg[1] = reg[1] ^ reg[2]
    if opcode==5:
        output.append(lc(operand,lci,reg)%8)
        #print(output)
    if opcode==6:
        reg[1] = int(reg[0]/(2**lc(operand,lci,reg))) #bdv        
    if opcode==7:
        reg[2] = int(reg[0]/(2**lc(operand,lci,reg))) #bdv
        
nstr=''
for n in output:
    nstr+=str(n)
    nstr+=','

#print(output)
############################
#Part 2
        
#Na lang zoeken in het exacte gedrag van de lijn doet hij samengevat:
#B = Neem de laatste drie bits. 
#Kijk naar het drietal bits startend 7-B posities vanaf rechts
#Bepaal de XOR van deze twee sets van drie getallen.
#Dit is dan je output
#Haal drie bits van je input af
#Herhaal tot er geen input meer over is

def bin3str(getal):
    bin_getal=bin(getal)[2:]
    if len(bin_getal)==1: bin_getal='00'+bin_getal
    if len(bin_getal)==2: bin_getal='0'+bin_getal
    return bin_getal

def compare_string(string1,string2):    
    option_string=''
    options=list()
    for optie1 in string1:
        for optie2 in string2:
	#Vergelijk de tekens op elke locatie in de string. Als het beide 1, 0 of X is dan komt dat in de string
            optie=True
            option_string=''
            for a,b in zip(optie1,optie2):
                if a==b:
                    option_string+=a
		#Andere opties waar we mee door kunnen
		#a = x en b is een getal
                elif a=='X':
                    option_string+=b
		#b = x en a is een getal
                elif b=='X':
                    option_string+=a
		#Geen mogelijke string
                else:
                    optie=False
                    break
    
            if optie==True:
                options.append(option_string)
                #print(option_string)
    return options
        

def generate_list(lengte,offset_rechts,getal) :
    options=list()
    
    for off in range(0,8):
        option_string='0b'
        laatste_drie=bin3str(off)
        xor_drie=bin3str(getal ^ off)
        shift=7-off
        
        string_last='X'*(lengte-offset_rechts-3)+laatste_drie+'X'*offset_rechts
        string_xor='X'*(lengte-offset_rechts-shift-3)+xor_drie
        string_xor=string_xor+'X'*(lengte-len(string_xor))
        optie=True
        for a,b in zip(string_xor,string_last):
            if a==b:
                option_string+=a
            elif a=='X':
                option_string+=b
            elif b=='X':
                option_string+=a
            else:
                optie=False
                break
            
        if optie==True:
            options.append(option_string)
    return options


#Genereer voor elk getal wat we willen zien als outputs een lijst van mogelijke strings die deze input zou geven op het juiste moment
#Als een nummer later moet komen, moet hij eerder in de string komen. voeg 3*n XXX toe zodat hij later wordt behandeld
s1=generate_list(16*3,0,program[0])
for i,n in enumerate(program[1:]):
    #Genereer opties voor het volgende getal
    s2=generate_list(16*3,3*i+3,n)

    #Probeer de strings samen te voegen als dat mogelijk is. Als dat niet mogelijk is, zijn het geen geschikte opties.
    s1=compare_string(s1,s2)

total_p2=10**99
for optie in s1:
    total_p2=min(total_p2,int(optie,2))

print("Part 1",nstr[:-1])
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))