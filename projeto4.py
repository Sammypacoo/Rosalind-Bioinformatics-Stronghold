# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:24:23 2022

@author: user
"""

import re

with open("C:\\Users\\user\\Desktop\\rosalind_fib.txt") as f:
    contents = f.read()
    #print(contents)
# Pegar os valores de meses (n) e pares de filhotes formadas a cada geração(k)
n_k = re.findall(r'[0-9]+',contents)
n=n_k[0]
n=int(n)
k=n_k[1]
k=int(k)

filhote=1
madu_rep=0
madu_rece=0

for i in range (1,n+1):
    if i==1:
        pares=1
    else:    
        madu_rep+=madu_rece
        madu_rece=filhote
        filhote=madu_rep*k
        pares=madu_rep+madu_rece+filhote

print(pares)
