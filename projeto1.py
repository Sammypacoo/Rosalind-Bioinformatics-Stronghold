# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:45:15 2022

@author: saman
"""
x = open("C://Users/saman/Downloads/rosalind_rna (1).txt","r")
#x = open("C://Users/saman/Downloads/teste.txt","r")

linhas= x.readline()
countA=0
countT=0
countC=0
countG=0

for line in linhas:
    if line =="a" or line=="A":
        countA+=1
    elif line =="t" or line=="T":
        countT+=1
    elif line =="c" or line=="C":
        countC+=1
    elif line =="g" or line=="G":
        countG+=1
resul= f"{countA} {countC} {countG} {countT}" 
print(resul)


def count(seq):
    countA=0
    countT=0
    countC=0
    countG=0

    for i in seq:
        if i =="a" or i=="A":
            countA+=1
        elif i =="t" or i=="T":
            countT+=1
        elif i =="c" or i=="C":
            countC+=1
        else:
            countG+=1
    resul= f"{countA} {countC} {countG} {countT}" 
    return resul


