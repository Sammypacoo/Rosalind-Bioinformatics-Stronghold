# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:33:14 2022

@author: saman
"""

x = open("C://Users/saman/Downloads/rosalind_rna.txt","r")
#x = open("C://Users/saman/Downloads/teste.txt","r")
linhas= x.readline()

seq=""
for line in linhas:
    if  line=="T":
        seq=seq + "U"
    else:
        seq=seq+line
print(seq)