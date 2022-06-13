# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:32:17 2022

@author: user
"""

with open("C:\\Users\\user\\Downloads\\rosalind_hamm (1).txt") as f:
        contents = f.read()
x=contents.split("\n")

x0=x[0]
x1=x[1]
soma=0
for i in range (len(x0)):
    if x0[i] != x1[i]:
        soma+=1
print (soma)
    