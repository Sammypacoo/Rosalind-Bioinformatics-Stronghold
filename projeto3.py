# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:23:24 2022

@author: user
"""
x = open("C:\\Users\\user\\Downloads\\rosalind_revc2.txt","r")
#x = open("C://Users/saman/Downloads/teste.txt","r")
line= x.readline()
#line="AAAACCCGGT"

resul=""
print(line)
tam=len(line)-1
for i in range (tam,-1,-1):
    item=line[i]
    item1=""
    if item =="T":
        item1="A"
    elif item=="A":
        item1="T"
    elif item=="C":
        item1="G"
    elif item=="G":
        item1="C"
    resul=resul+item1

print(resul)

'''
x = open("C:\\Users\\user\\Desktop\\rosalind_revc","r")
#x = open("C://Users/saman/Downloads/teste.txt","r")
linhas= x.readline()

seq=""
for line in linhas:
    if  line=="T":
        seq=seq + "U"
    else:
        seq=seq+line
print(seq)
'''