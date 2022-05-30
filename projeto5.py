# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:33:03 2022

@author: user
"""


import re
def Convert(lst):
     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
     return res_dct
local="C:\\Users\\user\\Downloads\\rosalind_gc.txt"
def contents_GC(local):
    with open(local) as f:
        contents = f.read()
        #print(contents)
    
    x=contents.split(">")   
    
    x.remove("")
    
    lista=[]
    for i in range(len(x)):
        z=x[i]
    
        z=z.split("\n") 
        string=""
        for hj  in range (1,len(z)):
            string+=z[hj]
        nome=z[0]    
        lista+=[nome]
        lista+=[string]
    lista
    
    
    dic=Convert(lista)
    maior=0
    chave_=""
    for chave in dic:
        string2=dic[chave]
        soma=0
        por=0
    
        for j in range(len(string2)):
            if string2[j]== "C" or string2[j]== "G":
                soma+=1
        por=(soma/len(string2))*100
        if por > maior:
            maior=por
            chave_=chave
                
    return chave_,maior

print(contents_GC(local))
    
    